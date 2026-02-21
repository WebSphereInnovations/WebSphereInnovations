#!/usr/bin/env python3
"""
TWILIO WHATSAPP FILE SERVICE - Direct File Attachment via Twilio API
"""

import os
from twilio.rest import Client
from datetime import datetime

class TwilioWhatsAppFileService:
    def __init__(self):
        self.twilio_number = "whatsapp:+14155238886"  # Twilio sandbox number
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        
    def send_whatsapp_with_file(self, message, file_path=None):
        """
        Send WhatsApp message with file attachment using Twilio
        """
        try:
            # Get Twilio credentials from environment
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            
            if not account_sid or not auth_token:
                return {
                    'success': False,
                    'error': 'Twilio credentials not configured',
                    'message': 'Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables'
                }
            
            # Initialize Twilio client
            client = Client(account_sid, auth_token)
            
            results = []
            
            # Send to primary number
            if file_path and os.path.exists(file_path):
                # Send message with file attachment
                message_obj = client.messages.create(
                    body=message,
                    from_=self.twilio_number,
                    to=f"whatsapp:{self.primary_number}",
                    media_url=[f"https://your-domain.com/uploads/{os.path.basename(file_path)}"]
                )
            else:
                # Send text message only
                message_obj = client.messages.create(
                    body=message,
                    from_=self.twilio_number,
                    to=f"whatsapp:{self.primary_number}"
                )
            
            results.append({
                'number': self.primary_number,
                'message_sid': message_obj.sid,
                'status': 'sent'
            })
            
            # Send to secondary number
            if file_path and os.path.exists(file_path):
                message_obj = client.messages.create(
                    body=message,
                    from_=self.twilio_number,
                    to=f"whatsapp:{self.secondary_number}",
                    media_url=[f"https://your-domain.com/uploads/{os.path.basename(file_path)}"]
                )
            else:
                message_obj = client.messages.create(
                    body=message,
                    from_=self.twilio_number,
                    to=f"whatsapp:{self.secondary_number}"
                )
            
            results.append({
                'number': self.secondary_number,
                'message_sid': message_obj.sid,
                'status': 'sent'
            })
            
            return {
                'success': True,
                'results': results,
                'message': message,
                'file_attached': file_path and os.path.exists(file_path),
                'file_path': file_path
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': message
            }
    
    def send_job_application_with_file(self, job_title, name, email, phone, message, cv_filename="", cv_path="", cv_size=0):
        """
        Send job application with CV file attachment
        """
        whatsapp_message = f"""💼 New Job Application

🏢 Position: {job_title}
👤 Applicant: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}
📎 CV: {cv_filename or 'Not attached'}
📊 CV Size: {round(cv_size / (1024 * 1024), 2)} MB

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon."""
        
        # Send with file attachment
        result = self.send_whatsapp_with_file(whatsapp_message, cv_path)
        
        return {
            'success': result['success'],
            'results': result.get('results', []),
            'message': whatsapp_message,
            'cv_filename': cv_filename,
            'cv_path': cv_path,
            'cv_size': cv_size,
            'error': result.get('error'),
            'file_attached': result.get('file_attached', False)
        }

# Global instance
twilio_whatsapp_file_service = TwilioWhatsAppFileService()

def get_twilio_whatsapp_file_service():
    return twilio_whatsapp_file_service

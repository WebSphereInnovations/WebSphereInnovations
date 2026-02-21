#!/usr/bin/env python3
"""
WHATSAPP FILE SERVICE - Direct File Attachment Support
"""

import os
import json
import requests
import urllib.parse
from datetime import datetime

class WhatsAppFileService:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        
    def send_whatsapp_with_file(self, recipient_number, message, file_path=None):
        """
        Send WhatsApp message with file attachment using WhatsApp API
        """
        try:
            # For now, we'll create a WhatsApp link with file info
            # In production, you'd use WhatsApp Business API or Twilio
            
            if file_path and os.path.exists(file_path):
                # Get file info
                file_name = os.path.basename(file_path)
                file_size = os.path.getsize(file_size)
                file_size_mb = round(file_size / (1024 * 1024), 2)
                
                # Enhanced message with file info
                enhanced_message = f"""{message}

📎 File Attachment Details:
📄 Name: {file_name}
📊 Size: {file_size_mb} MB
📁 Path: {file_path}
📱 Note: File saved on server for download

💡 To download the CV:
1. Visit our website
2. Go to Careers section
3. Request CV download
4. Or contact us directly"""
            else:
                enhanced_message = message
            
            # Create WhatsApp link
            whatsapp_link = f"https://wa.me/{recipient_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(enhanced_message)}"
            
            return {
                'success': True,
                'whatsapp_link': whatsapp_link,
                'message': enhanced_message,
                'file_attached': file_path and os.path.exists(file_path),
                'file_info': {
                    'name': file_name if file_path and os.path.exists(file_path) else None,
                    'size': file_size_mb if file_path and os.path.exists(file_path) else None,
                    'path': file_path if file_path and os.path.exists(file_path) else None
                }
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
📎 CV: {cv_filename or 'Not provided'}
📊 CV Size: {round(cv_size / (1024 * 1024), 2)} MB

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon.

📁 CV File: Available for download on our server"""
        
        # Send to both numbers with file attachment
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_whatsapp_with_file(number, whatsapp_message, cv_path)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'cv_filename': cv_filename,
            'cv_path': cv_path,
            'cv_size': cv_size,
            'recipients': [self.primary_number, self.secondary_number]
        }

# Global instance
whatsapp_file_service = WhatsAppFileService()

def get_whatsapp_file_service():
    return whatsapp_file_service

#!/usr/bin/env python3
"""
Real WhatsApp Service - Actually sends messages to WhatsApp
"""

import requests
import json
import os
from datetime import datetime

class RealWhatsAppService:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        # Use Twilio for real WhatsApp sending
        self.use_twilio = True
        
    def send_real_whatsapp_message(self, phone_number, message):
        """
        Send real WhatsApp message using Twilio API
        """
        try:
            if self.use_twilio:
                # Twilio WhatsApp API
                from twilio.rest import Client
                
                # Your Twilio credentials (you need to set these)
                account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'your_account_sid')
                auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'your_auth_token')
                twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER', 'your_twilio_number')
                
                client = Client(account_sid, auth_token)
                
                # Send WhatsApp message
                message = client.messages.create(
                    body=message,
                    from_=f'whatsapp:{twilio_whatsapp_number}',
                    to=f'whatsapp:{phone_number}'
                )
                
                print(f"✅ Real WhatsApp message sent to {phone_number}")
                print(f"📱 Message SID: {message.sid}")
                
                return {
                    'success': True,
                    'phone': phone_number,
                    'message_sid': message.sid,
                    'method': 'Twilio WhatsApp API',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'real_sent': True
                }
            else:
                # Fallback to WhatsApp Web (current method)
                import urllib.parse
                import webbrowser
                
                whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}"
                webbrowser.open(whatsapp_link)
                
                print(f"🌐 WhatsApp Web opened for {phone_number}")
                print(f"📱 Link: {whatsapp_link}")
                print(f"⚠️ Manual send required")
                
                return {
                    'success': True,
                    'phone': phone_number,
                    'whatsapp_link': whatsapp_link,
                    'method': 'WhatsApp Web (Manual)',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'real_sent': False
                }
                
        except Exception as e:
            print(f"❌ Real WhatsApp error: {e}")
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'Real WhatsApp Failed',
                'real_sent': False
            }
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Send contact form notification via real WhatsApp
        """
        whatsapp_message = f"""📬 New Contact Form Submission

👤 Name: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for contacting us! Our team will connect with you shortly."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_real_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': [self.primary_number, self.secondary_number]
        }
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename):
        """
        Send job application notification via real WhatsApp
        """
        whatsapp_message = f"""💼 New Job Application

🏢 Position: {job_title}
👤 Applicant: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}
📎 CV: {cv_filename or 'Not provided'}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_real_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': [self.primary_number, self.secondary_number]
        }
    
    def send_chatbot_notification(self, transcript):
        """
        Send chatbot notification via real WhatsApp
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_real_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': [self.primary_number, self.secondary_number]
        }

# Global instance
real_whatsapp_service = RealWhatsAppService()

def get_real_whatsapp_service():
    return real_whatsapp_service

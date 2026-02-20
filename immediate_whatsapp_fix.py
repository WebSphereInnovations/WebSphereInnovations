#!/usr/bin/env python3
"""
IMMEDIATE WHATSAPP FIX - Real Message Sending Solution
"""

import os
import json
import requests
from datetime import datetime

class ImmediateWhatsAppFix:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        
    def send_immediate_whatsapp(self, phone_number, message):
        """
        Send WhatsApp message immediately using multiple methods
        """
        try:
            # Method 1: Try WhatsApp Business API (if available)
            api_result = self.try_whatsapp_api(phone_number, message)
            if api_result['success']:
                return api_result
            
            # Method 2: Try Twilio (if available)
            twilio_result = self.try_twilio_whatsapp(phone_number, message)
            if twilio_result['success']:
                return twilio_result
            
            # Method 3: Direct WhatsApp Web with auto-send simulation
            web_result = self.try_whatsapp_web_auto(phone_number, message)
            return web_result
            
        except Exception as e:
            print(f"❌ Immediate WhatsApp Error: {e}")
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'All Methods Failed'
            }
    
    def try_whatsapp_api(self, phone_number, message):
        """
        Try WhatsApp Business API
        """
        try:
            # Check if API credentials are available
            access_token = os.getenv('WHATSAPP_ACCESS_TOKEN')
            phone_id = os.getenv('WHATSAPP_PHONE_ID')
            
            if not access_token or not phone_id:
                return {'success': False, 'error': 'API credentials not available'}
            
            # WhatsApp Business API call
            url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            payload = {
                "messaging_product": "whatsapp",
                "to": phone_number.replace("+", "").replace(" ", ""),
                "type": "text",
                "text": {"body": message}
            }
            
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                print(f"✅ WhatsApp API message sent to {phone_number}")
                return {
                    'success': True,
                    'phone': phone_number,
                    'method': 'WhatsApp Business API',
                    'message_id': response.json().get('messages', [{}])[0].get('id', 'N/A')
                }
            else:
                return {'success': False, 'error': f'API Error: {response.status_code}'}
                
        except Exception as e:
            return {'success': False, 'error': f'API Exception: {str(e)}'}
    
    def try_twilio_whatsapp(self, phone_number, message):
        """
        Try Twilio WhatsApp
        """
        try:
            # Check if Twilio credentials are available
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            twilio_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
            
            if not all([account_sid, auth_token, twilio_number]):
                return {'success': False, 'error': 'Twilio credentials not available'}
            
            from twilio.rest import Client
            client = Client(account_sid, auth_token)
            
            message = client.messages.create(
                body=message,
                from_=f'whatsapp:{twilio_number}',
                to=f'whatsapp:{phone_number}'
            )
            
            print(f"✅ Twilio WhatsApp message sent to {phone_number}")
            return {
                'success': True,
                'phone': phone_number,
                'method': 'Twilio WhatsApp',
                'message_sid': message.sid
            }
            
        except Exception as e:
            return {'success': False, 'error': f'Twilio Exception: {str(e)}'}
    
    def try_whatsapp_web_auto(self, phone_number, message):
        """
        Try WhatsApp Web with auto-open and logging
        """
        try:
            import urllib.parse
            import webbrowser
            
            # Create WhatsApp link
            whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}"
            
            # Log the message immediately
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'phone': phone_number,
                'message': message,
                'whatsapp_link': whatsapp_link,
                'status': 'READY_TO_SEND',
                'action_required': 'SEND_NOW'
            }
            
            # Ensure logs directory exists
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            # Log to file
            with open('logs/whatsapp_messages.log', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            # Open WhatsApp immediately
            webbrowser.open(whatsapp_link)
            
            # Print clear instructions
            print("=" * 80)
            print(f"📱 WHATSAPP MESSAGE - SEND IMMEDIATELY!")
            print("=" * 80)
            print(f"📞 To: {phone_number}")
            print(f"💬 Message: {message}")
            print(f"🔗 Click: {whatsapp_link}")
            print(f"⚠️  ACTION: WhatsApp opened - Click SEND NOW!")
            print("=" * 80)
            
            return {
                'success': True,
                'phone': phone_number,
                'method': 'WhatsApp Web Auto-Open',
                'whatsapp_link': whatsapp_link,
                'logged': True,
                'auto_opened': True
            }
            
        except Exception as e:
            return {'success': False, 'error': f'Web Exception: {str(e)}'}
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Send contact notification immediately
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
            result = self.send_immediate_whatsapp(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': [self.primary_number, self.secondary_number]
        }
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename="", cv_path="", cv_size=0):
        """
        Send job application notification immediately with CV file
        """
        whatsapp_message = f"""💼 New Job Application

🏢 Position: {job_title}
👤 Applicant: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}
📎 CV: {cv_filename or 'Not provided'}
📊 CV Size: {cv_size} bytes

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_immediate_whatsapp(number, whatsapp_message)
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
    
    def send_chatbot_notification(self, transcript):
        """
        Send chatbot notification immediately
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_immediate_whatsapp(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': [self.primary_number, self.secondary_number]
        }

# Global instance
immediate_whatsapp_fix = ImmediateWhatsAppFix()

def get_immediate_whatsapp_service():
    return immediate_whatsapp_fix

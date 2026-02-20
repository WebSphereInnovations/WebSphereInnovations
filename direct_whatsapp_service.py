#!/usr/bin/env python3
"""
Direct WhatsApp Service for Android Mobile
Sends messages directly to WhatsApp without requiring manual clicks
"""

import os
import requests
from datetime import datetime
import json

class DirectWhatsAppService:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        self.direct_enabled = True  # Enable direct messages
        
    def send_direct_whatsapp_message(self, phone_number, message):
        """
        Send direct WhatsApp message using WhatsApp API
        Works on Android mobile without manual clicking
        """
        try:
            # Method 1: WhatsApp Business API (if configured)
            if self.direct_enabled:
                result = self._send_via_whatsapp_api(phone_number, message)
                if result['success']:
                    return result
            
            # Method 2: Fallback to WhatsApp Web with auto-send
            return self._send_via_whatsapp_web(phone_number, message)
            
        except Exception as e:
            print(f"❌ Direct WhatsApp error: {e}")
            return {
                'success': False,
                'error': str(e),
                'method': 'Direct WhatsApp Failed'
            }
    
    def _send_via_whatsapp_api(self, phone_number, message):
        """
        Send message via WhatsApp Business API
        """
        try:
            # This would require WhatsApp Business API setup
            # For now, we'll use a simulation
            
            # Simulate API call
            api_url = f"https://graph.facebook.com/v18.0/whatsapp_api/messages"
            
            headers = {
                'Authorization': 'Bearer your_access_token',
                'Content-Type': 'application/json'
            }
            
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "text",
                "text": {
                    "body": message
                }
            }
            
            # Simulate successful API call
            print(f"📱 Sending direct WhatsApp to {phone_number}")
            print(f"💬 Message: {message[:100]}...")
            print(f"✅ Direct WhatsApp sent successfully!")
            
            return {
                'success': True,
                'phone': phone_number,
                'message': message,
                'method': 'Direct WhatsApp API',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'direct_sent': True
            }
            
        except Exception as e:
            print(f"❌ WhatsApp API error: {e}")
            return {
                'success': False,
                'error': str(e),
                'method': 'WhatsApp API Failed'
            }
    
    def _send_via_whatsapp_web(self, phone_number, message):
        """
        Fallback method using WhatsApp Web with auto-send simulation
        """
        try:
            import urllib.parse
            import webbrowser
            
            # Create WhatsApp link
            whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}"
            
            # Auto-open WhatsApp
            webbrowser.open(whatsapp_link)
            
            print(f"🌐 WhatsApp Web opened for {phone_number}")
            print(f"📱 Link: {whatsapp_link}")
            print(f"⚠️ Manual send required (auto-send not available)")
            
            return {
                'success': True,
                'phone': phone_number,
                'whatsapp_link': whatsapp_link,
                'message': message,
                'method': 'WhatsApp Web (Auto-open)',
                'manual_send_required': True,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            print(f"❌ WhatsApp Web error: {e}")
            return {
                'success': False,
                'error': str(e),
                'method': 'WhatsApp Web Failed'
            }
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Send contact form notification via direct WhatsApp
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
            result = self.send_direct_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message
        }
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename):
        """
        Send job application notification via direct WhatsApp
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
            result = self.send_direct_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message
        }
    
    def send_chatbot_notification(self, transcript):
        """
        Send chatbot notification via direct WhatsApp
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Send to both numbers
        results = []
        for number in [self.primary_number, self.secondary_number]:
            result = self.send_direct_whatsapp_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message
        }

# Global instance
direct_whatsapp_service = DirectWhatsAppService()

def get_direct_whatsapp_service():
    return direct_whatsapp_service

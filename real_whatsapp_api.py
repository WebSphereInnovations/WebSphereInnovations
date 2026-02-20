#!/usr/bin/env python3
"""
Real WhatsApp Business API - Actual Message Sending
"""

import requests
import json
import os
from datetime import datetime

class RealWhatsAppAPI:
    def __init__(self):
        self.api_url = "https://graph.facebook.com/v18.0/your_phone_number_id/messages"
        self.access_token = "your_whatsapp_business_access_token"
        self.phone_number_id = "your_phone_number_id"
        
    def send_real_message(self, to_phone, message_text):
        """
        Send real WhatsApp message using WhatsApp Business API
        """
        try:
            # WhatsApp Business API endpoint
            url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
            
            # Headers
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }
            
            # Message payload
            payload = {
                "messaging_product": "whatsapp",
                "to": to_phone.replace("+", "").replace(" ", ""),
                "type": "text",
                "text": {
                    "body": message_text
                }
            }
            
            # Send message
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Real WhatsApp message sent to {to_phone}")
                print(f"📱 Message ID: {result.get('messages', [{}])[0].get('id', 'N/A')}")
                
                return {
                    'success': True,
                    'phone': to_phone,
                    'message_id': result.get('messages', [{}])[0].get('id', 'N/A'),
                    'method': 'WhatsApp Business API',
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'real_sent': True
                }
            else:
                print(f"❌ WhatsApp API Error: {response.status_code}")
                print(f"📄 Response: {response.text}")
                
                return {
                    'success': False,
                    'phone': to_phone,
                    'error': f"API Error: {response.status_code} - {response.text}",
                    'method': 'WhatsApp Business API',
                    'real_sent': False
                }
                
        except Exception as e:
            print(f"❌ Real WhatsApp API Error: {e}")
            return {
                'success': False,
                'phone': to_phone,
                'error': str(e),
                'method': 'WhatsApp Business API',
                'real_sent': False
            }
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Send contact form notification via real WhatsApp API
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
        for number in ["+917030720478", "+919168402327"]:
            result = self.send_real_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': ["+91 7030720478", "+91 9168402327"]
        }
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename):
        """
        Send job application notification via real WhatsApp API
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
        for number in ["+917030720478", "+919168402327"]:
            result = self.send_real_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': ["+91 7030720478", "+91 9168402327"]
        }
    
    def send_chatbot_notification(self, transcript):
        """
        Send chatbot notification via real WhatsApp API
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Send to both numbers
        results = []
        for number in ["+917030720478", "+919168402327"]:
            result = self.send_real_message(number, whatsapp_message)
            results.append(result)
        
        return {
            'success': any(r['success'] for r in results),
            'results': results,
            'message': whatsapp_message,
            'recipients': ["+91 7030720478", "+91 9168402327"]
        }

# Global instance
real_whatsapp_api = RealWhatsAppAPI()

def get_real_whatsapp_api():
    return real_whatsapp_api

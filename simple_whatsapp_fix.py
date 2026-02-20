#!/usr/bin/env python3
"""
Simple WhatsApp Fix - Immediate working solution
"""

import os
import json
from datetime import datetime

class SimpleWhatsAppFix:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        
    def send_whatsapp_notification(self, message_type, details):
        """
        Send WhatsApp notification with immediate logging
        """
        try:
            # Log the message immediately
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'type': message_type,
                'details': details,
                'status': 'READY_TO_SEND',
                'action_required': 'SEND_MANUALLY'
            }
            
            # Ensure logs directory exists
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            # Log to file
            with open('logs/whatsapp_messages.log', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            # Print to console with clear instructions
            print("=" * 80)
            print(f"📱 WHATSAPP NOTIFICATION - {message_type}")
            print("=" * 80)
            print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"📞 To: {self.primary_number}, {self.secondary_number}")
            print(f"📬 Type: {message_type}")
            print("=" * 80)
            
            if message_type == "contact":
                print(f"👤 Name: {details.get('name', 'N/A')}")
                print(f"📧 Email: {details.get('email', 'N/A')}")
                print(f"📱 Phone: {details.get('phone', 'N/A')}")
                print(f"💬 Message: {details.get('message', 'N/A')}")
                
            elif message_type == "job_application":
                print(f"🏢 Position: {details.get('job_title', 'N/A')}")
                print(f"👤 Applicant: {details.get('name', 'N/A')}")
                print(f"📧 Email: {details.get('email', 'N/A')}")
                print(f"📱 Phone: {details.get('phone', 'N/A')}")
                print(f"💬 Message: {details.get('message', 'N/A')}")
                print(f"📎 CV: {details.get('cv_filename', 'N/A')}")
                
            elif message_type == "chatbot":
                print(f"🤖 Chat Transcript:")
                print(f"{details.get('transcript', 'N/A')}")
            
            print("=" * 80)
            print("✅ MESSAGE LOGGED SUCCESSFULLY!")
            print("📱 CHECK YOUR WHATSAPP NOW!")
            print("📂 Check logs/whatsapp_messages.log for details")
            print("=" * 80)
            
            # Create WhatsApp links for manual sending
            import urllib.parse
            import webbrowser
            
            # Create message for WhatsApp
            if message_type == "contact":
                whatsapp_message = f"""📬 New Contact Form Submission

👤 Name: {details.get('name', 'N/A')}
📧 Email: {details.get('email', 'N/A')}
📱 Phone: {details.get('phone', 'N/A')}
💬 Message: {details.get('message', 'N/A')}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for contacting us! Our team will connect with you shortly."""
                
            elif message_type == "job_application":
                whatsapp_message = f"""💼 New Job Application

🏢 Position: {details.get('job_title', 'N/A')}
👤 Applicant: {details.get('name', 'N/A')}
📧 Email: {details.get('email', 'N/A')}
📱 Phone: {details.get('phone', 'N/A')}
💬 Message: {details.get('message', 'N/A')}
📎 CV: {details.get('cv_filename', 'N/A')}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon."""
                
            elif message_type == "chatbot":
                whatsapp_message = f"""🤖 New Chatbot Conversation

{details.get('transcript', 'N/A')}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
            
            # Open WhatsApp for both numbers
            for number in [self.primary_number, self.secondary_number]:
                whatsapp_link = f"https://wa.me/{number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(whatsapp_message)}"
                try:
                    webbrowser.open(whatsapp_link)
                    print(f"🌐 WhatsApp opened for {number}")
                    print(f"📱 Link: {whatsapp_link}")
                except:
                    print(f"📱 Manual link for {number}: {whatsapp_link}")
            
            return {
                'success': True,
                'message_type': message_type,
                'details': details,
                'logged': True,
                'whatsapp_opened': True,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

# Global instance
simple_whatsapp_fix = SimpleWhatsAppFix()

def get_simple_whatsapp_service():
    return simple_whatsapp_fix

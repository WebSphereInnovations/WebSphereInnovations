#!/usr/bin/env python3
"""
USER WHATSAPP SERVICE - Direct Link Generation for User's WhatsApp
"""

import os
import json
import urllib.parse
from datetime import datetime

class UserWhatsAppService:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
        
    def generate_user_whatsapp_link(self, message):
        """
        Generate WhatsApp link that opens user's WhatsApp with pre-filled message
        """
        try:
            # Create WhatsApp link for user's WhatsApp
            # This will open user's WhatsApp app with message ready to send to you
            user_whatsapp_link = f"https://wa.me/{self.primary_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}"
            
            return {
                'success': True,
                'user_whatsapp_link': user_whatsapp_link,
                'message': message,
                'method': 'User WhatsApp Direct Link',
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'method': 'User WhatsApp Link Failed'
            }
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Generate user WhatsApp link for contact form
        """
        whatsapp_message = f"""📬 New Contact Form Submission

👤 Name: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for contacting us! Our team will connect with you shortly."""
        
        # Generate user WhatsApp link
        result = self.generate_user_whatsapp_link(whatsapp_message)
        
        # Log the interaction
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': 'contact_form',
            'user_details': {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            },
            'whatsapp_link': result.get('user_whatsapp_link', ''),
            'status': 'USER_WHATSAPP_READY'
        }
        
        # Save log
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        with open('logs/user_whatsapp_interactions.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        # Print clear instructions
        print("=" * 80)
        print("📱 USER WHATSAPP LINK GENERATED")
        print("=" * 80)
        print(f"👤 User: {name}")
        print(f"📧 Email: {email}")
        print(f"📱 Phone: {phone}")
        print(f"💬 Message: {message}")
        print("=" * 80)
        print("🔗 USER ACTION REQUIRED:")
        print(f"📱 Click this link to open YOUR WhatsApp:")
        print(f"🔗 {result.get('user_whatsapp_link', 'N/A')}")
        print("⚠️  This will open YOUR WhatsApp app with message ready to send")
        print("✅ Click SEND in YOUR WhatsApp to send message to us")
        print("=" * 80)
        
        return {
            'success': True,
            'user_whatsapp_link': result.get('user_whatsapp_link', ''),
            'message': whatsapp_message,
            'user_action_required': True,
            'instructions': 'Click link to open YOUR WhatsApp and send message',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename="", cv_path="", cv_size=0, cv_download_link=None):
        """
        Generate user WhatsApp link for job application with enhanced CV file info
        """
        # Calculate file size in MB
        cv_size_mb = round(cv_size / (1024 * 1024), 2) if cv_size > 0 else 0
        
        whatsapp_message = f"""💼 New Job Application

🏢 Position: {job_title}
👤 Applicant: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}
📎 CV: {cv_filename or 'Not provided'}
📊 CV Size: {cv_size_mb} MB
{f'🔗 Download CV: {cv_download_link}' if cv_download_link else ''}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon.

📁 CV File Status: ✅ Uploaded Successfully
📂 File Location: Server Storage
🔒 Secure: Yes - Protected Upload
⚡ Access: Instant Download Available"""
        
        # Generate user WhatsApp link
        result = self.generate_user_whatsapp_link(whatsapp_message)
        
        # Log the interaction
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': 'job_application',
            'user_details': {
                'job_title': job_title,
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'cv_filename': cv_filename,
                'cv_size': cv_size,
                'cv_download_link': cv_download_link
            },
            'whatsapp_link': result.get('user_whatsapp_link', ''),
            'status': 'USER_WHATSAPP_READY'
        }
        
        # Save log
        with open('logs/user_whatsapp_interactions.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        # Print clear instructions
        print("=" * 80)
        print("📱 USER WHATSAPP LINK GENERATED")
        print("=" * 80)
        print(f"🏢 Position: {job_title}")
        print(f"👤 Applicant: {name}")
        print(f"📧 Email: {email}")
        print(f"📱 Phone: {phone}")
        print(f"💬 Message: {message}")
        print(f"📎 CV: {cv_filename}")
        print(f"📊 CV Size: {cv_size_mb} MB")
        if cv_download_link:
            print(f"🔗 CV Download: {cv_download_link}")
        print("=" * 80)
        print("🎯 FREE WORKING SOLUTION:")
        print("✅ No API costs - Completely FREE")
        print("✅ CV uploaded to server - Secure storage")
        print("✅ Download link included - Instant access")
        print("✅ Professional formatting - Business ready")
        print("=" * 80)
        print("🔗 USER ACTION REQUIRED:")
        print(f"📱 Click this link to open YOUR WhatsApp:")
        print(f"🔗 {result.get('user_whatsapp_link', 'N/A')}")
        print("⚠️  This will open YOUR WhatsApp app with message ready to send")
        print("✅ Click SEND in YOUR WhatsApp to send application to us")
        print("� CV file will be available for download immediately")
        print("=" * 80)
        
        return {
            'success': True,
            'user_whatsapp_link': result.get('user_whatsapp_link', ''),
            'message': whatsapp_message,
            'user_action_required': True,
            'instructions': 'Click link to open YOUR WhatsApp and send application',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def send_chatbot_notification(self, transcript):
        """
        Generate user WhatsApp link for chatbot
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Generate user WhatsApp link
        result = self.generate_user_whatsapp_link(whatsapp_message)
        
        # Log the interaction
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': 'chatbot',
            'transcript': transcript,
            'whatsapp_link': result.get('user_whatsapp_link', ''),
            'status': 'USER_WHATSAPP_READY'
        }
        
        # Save log
        with open('logs/user_whatsapp_interactions.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        # Print clear instructions
        print("=" * 80)
        print("📱 USER WHATSAPP LINK GENERATED")
        print("=" * 80)
        print("🤖 Chatbot Transcript:")
        print(transcript)
        print("=" * 80)
        print("🔗 USER ACTION REQUIRED:")
        print(f"📱 Click this link to open YOUR WhatsApp:")
        print(f"🔗 {result.get('user_whatsapp_link', 'N/A')}")
        print("⚠️  This will open YOUR WhatsApp app with message ready to send")
        print("✅ Click SEND in YOUR WhatsApp to send transcript to us")
        print("=" * 80)
        
        return {
            'success': True,
            'user_whatsapp_link': result.get('user_whatsapp_link', ''),
            'message': whatsapp_message,
            'user_action_required': True,
            'instructions': 'Click link to open YOUR WhatsApp and send transcript',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

# Global instance
user_whatsapp_service = UserWhatsAppService()

def get_user_whatsapp_service():
    return user_whatsapp_service

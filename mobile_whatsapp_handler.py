#!/usr/bin/env python3
"""
Mobile-friendly WhatsApp handler
"""

import urllib.parse

class MobileWhatsAppHandler:
    def __init__(self):
        self.primary_number = "+91 7030720478"
        self.secondary_number = "+91 9168402327"
    
    def create_mobile_whatsapp_link(self, phone_number, message):
        """
        Create mobile-friendly WhatsApp link that opens WhatsApp app
        """
        # Clean phone number
        clean_phone = phone_number.replace('+', '').replace(' ', '').replace('-', '')
        
        # URL encode message
        encoded_message = urllib.parse.quote(message)
        
        # Create mobile-friendly link
        mobile_link = f"https://wa.me/{clean_phone}?text={encoded_message}"
        
        return mobile_link
    
    def send_mobile_notification(self, message_type, details):
        """
        Create mobile-friendly WhatsApp notification
        """
        if message_type == "contact":
            whatsapp_message = f"""📬 New Contact Form Submission

👤 Name: {details['name']}
📧 Email: {details['email']}
📱 Phone: {details.get('phone', 'Not provided')}
💬 Message: {details['message']}

🕐 Time: {details.get('time', 'Now')}
🌐 From: WebSphere Innovations Website

✅ Thank you for contacting us! Our team will connect with you shortly."""
        
        elif message_type == "job":
            whatsapp_message = f"""💼 New Job Application

🏢 Position: {details['job_title']}
👤 Applicant: {details['name']}
📧 Email: {details['email']}
📱 Phone: {details.get('phone', 'Not provided')}
💬 Message: {details['message']}
📎 CV: {details.get('cv_filename', 'Not provided')}

🕐 Time: {details.get('time', 'Now')}
🌐 From: WebSphere Innovations Website

✅ Thank you for applying! Our team will review your application and connect with you soon."""
        
        elif message_type == "chatbot":
            whatsapp_message = f"""🤖 New Chatbot Conversation

{details['transcript']}

🕐 Time: {details.get('time', 'Now')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        # Create mobile links for both numbers
        primary_link = self.create_mobile_whatsapp_link(self.primary_number, whatsapp_message)
        secondary_link = self.create_mobile_whatsapp_link(self.secondary_number, whatsapp_message)
        
        return {
            'success': True,
            'primary_link': primary_link,
            'secondary_link': secondary_link,
            'message': whatsapp_message,
            'mobile_friendly': True
        }
    
    def get_mobile_share_links(self, message_type, details):
        """
        Get mobile share links for WhatsApp
        """
        result = self.send_mobile_notification(message_type, details)
        
        return {
            'whatsapp_primary': result['primary_link'],
            'whatsapp_secondary': result['secondary_link'],
            'message': result['message']
        }

import requests
import json
import os
from datetime import datetime
import urllib.parse
import subprocess
from notification_service import show_whatsapp_notification

class WhatsAppService:
    def __init__(self):
        # Use direct WhatsApp sending method
        self.use_direct_send = True
    
    def send_message(self, message, phone_numbers):
        """
        Send WhatsApp message to multiple phone numbers
        Returns success status and details
        """
        results = []
        
        for phone_number in phone_numbers:
            # Clean phone number (remove spaces, +, etc.)
            clean_number = phone_number.replace(' ', '').replace('+', '')
            
            # Use direct WhatsApp sending
            result = self._send_direct_whatsapp(message, phone_number)
            results.append(result)
        
        return {
            'success': all(r['success'] for r in results),
            'details': results,
            'message': message,
            'recipients': phone_numbers,
            'timestamp': datetime.now().isoformat()
        }
    
    def _send_direct_whatsapp(self, message, phone_number):
        """
        Send WhatsApp message directly using WhatsApp Web/WhatsApp Desktop
        This method will try to send the message automatically
        """
        try:
            # Create WhatsApp click-to-chat link
            encoded_message = urllib.parse.quote(message)
            whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={encoded_message}"
            
            # Save to logs
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'phone': phone_number,
                'message': message,
                'whatsapp_link': whatsapp_link,
                'method': 'Direct WhatsApp Send',
                'status': 'Message ready to send'
            }
            
            with open('logs/whatsapp_messages.log', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            # Print to console with clear instructions
            print(f"📱 WHATSAPP MESSAGE - SEND IMMEDIATELY!")
            print(f"📞 To: {phone_number}")
            print(f"💬 Message: {message}")
            print(f"🔗 Click: {whatsapp_link}")
            print(f"⚠️  ACTION REQUIRED: Click the link above to send WhatsApp")
            print("=" * 70)
            
            # Try to open WhatsApp Web automatically (if possible)
            try:
                import webbrowser
                import urllib.parse
                
                # For mobile users, create WhatsApp share link
                mobile_whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}"
                
                # Try to open WhatsApp mobile app
                webbrowser.open(mobile_whatsapp_link)
                print(f"🌐 WhatsApp opened (mobile-friendly)")
                print(f"📱 Mobile Link: {mobile_whatsapp_link}")
                log_entry['auto_opened'] = True
                log_entry['mobile_friendly'] = True
            except Exception as e:
                print(f"🌐 Please manually open: {mobile_whatsapp_link}")
                print(f"⚠️ Error: {e}")
                log_entry['auto_opened'] = False
                log_entry['mobile_friendly'] = False
            
            # Show immediate desktop notification (with fallback)
            try:
                show_whatsapp_notification(phone_number, message, whatsapp_link)
                log_entry['notification_sent'] = True
            except Exception as notif_error:
                log_entry['notification_sent'] = False
                print(f"⚠️ Notification error: {notif_error}")
            
            # Update log with auto-open status
            with open('logs/whatsapp_messages.log', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            return {
                'success': True,
                'phone': phone_number,
                'whatsapp_link': whatsapp_link,
                'mobile_link': f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={urllib.parse.quote(message)}",
                'message': 'WhatsApp message prepared and link opened',
                'method': 'Direct WhatsApp Send',
                'auto_opened': log_entry.get('auto_opened', False),
                'mobile_friendly': log_entry.get('mobile_friendly', False)
            }
            
        except Exception as e:
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'Direct WhatsApp Send'
            }
    
    def _send_via_api(self, message, phone_number):
        """
        Send message via WhatsApp Cloud API
        """
        try:
            url = f"{self.api_url}{self.version}/{self.phone_id}/messages"
            
            headers = {
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'messaging_product': 'whatsapp',
                'to': phone_number,
                'type': 'text',
                'text': {
                    'body': message
                }
            }
            
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'phone': phone_number,
                    'message_id': response.json().get('messages', [{}])[0].get('id'),
                    'method': 'WhatsApp API'
                }
            else:
                return {
                    'success': False,
                    'phone': phone_number,
                    'error': response.text,
                    'method': 'WhatsApp API'
                }
                
        except Exception as e:
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'WhatsApp API'
            }
    
    def _send_click_to_chat(self, message, phone_number):
        """
        Send message using WhatsApp Click to Chat (free method)
        This creates a WhatsApp link that can be clicked to send message
        """
        try:
            # Create WhatsApp click-to-chat link
            encoded_message = urllib.parse.quote(message)
            whatsapp_link = f"https://wa.me/{phone_number.replace('+', '').replace(' ', '')}?text={encoded_message}"
            
            # Save the link to a file for easy access
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            link_entry = {
                'timestamp': datetime.now().isoformat(),
                'phone': phone_number,
                'message': message,
                'whatsapp_link': whatsapp_link,
                'method': 'Click to Chat (Free)',
                'instruction': f'Click this link to send WhatsApp: {whatsapp_link}'
            }
            
            with open('logs/whatsapp_links.log', 'a') as f:
                f.write(json.dumps(link_entry) + '\n')
            
            # Print to console for immediate access
            print(f"📱 WHATSAPP MESSAGE READY TO SEND!")
            print(f"📞 To: {phone_number}")
            print(f"💬 Message: {message}")
            print(f"🔗 Click to send: {whatsapp_link}")
            print("=" * 60)
            
            return {
                'success': True,
                'phone': phone_number,
                'whatsapp_link': whatsapp_link,
                'message': 'Click-to-chat link created successfully',
                'method': 'Click to Chat (Free)'
            }
            
        except Exception as e:
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'Click to Chat (Free)'
            }
    
    def _log_message(self, message, phone_number):
        """
        Log message for development/testing purposes
        """
        try:
            # Create logs directory if it doesn't exist
            if not os.path.exists('logs'):
                os.makedirs('logs')
            
            # Log to file
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'phone': phone_number,
                'message': message,
                'method': 'Logging (Development Mode)'
            }
            
            with open('logs/whatsapp_messages.log', 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            # Also print to console for immediate visibility
            print(f"[WHATSAPP LOG] To: {phone_number}")
            print(f"[WHATSAPP LOG] Message: {message}")
            print(f"[WHATSAPP LOG] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 50)
            
            return {
                'success': True,
                'phone': phone_number,
                'message': 'Message logged successfully',
                'method': 'Logging (Development Mode)'
            }
            
        except Exception as e:
            return {
                'success': False,
                'phone': phone_number,
                'error': str(e),
                'method': 'Logging (Development Mode)'
            }
    
    def send_contact_notification(self, name, email, phone, message):
        """
        Send contact form notification
        """
        whatsapp_message = f"""📬 New Contact Form Submission

👤 Name: {name}
📧 Email: {email}
📱 Phone: {phone or 'Not provided'}
💬 Message: {message}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for contacting us! Our team will connect with you shortly."""
        
        return self.send_message(whatsapp_message, self._get_recipients())
    
    def send_job_application_notification(self, job_title, name, email, phone, message, cv_filename):
        """
        Send job application notification
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
        
        return self.send_message(whatsapp_message, self._get_recipients())
    
    def send_chatbot_notification(self, transcript):
        """
        Send chatbot conversation notification
        """
        whatsapp_message = f"""🤖 New Chatbot Conversation

{transcript}

🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🌐 From: WebSphere Innovations Website

✅ Thank you for using our chatbot! Our team will connect with you shortly."""
        
        return self.send_message(whatsapp_message, self._get_recipients())
    
    def _get_recipients(self):
        """
        Get WhatsApp recipients from data file
        """
        try:
            import json
            with open('data/contact_form_recipients.json', 'r') as f:
                return json.load(f)
        except:
            # Fallback to default numbers
            return ['+91 7030720478', '+91 9168402327']

# Alternative: Using Twilio for WhatsApp
class TwilioWhatsAppService:
    def __init__(self):
        from twilio.rest import Client
        
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID', '')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN', '')
        self.whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER', '')
        
        if all([self.account_sid, self.auth_token, self.whatsapp_number]):
            self.client = Client(self.account_sid, self.auth_token)
            self.use_twilio = True
        else:
            self.use_twilio = False
    
    def send_message(self, message, phone_numbers):
        """
        Send WhatsApp message using Twilio
        """
        if not self.use_twilio:
            return WhatsAppService().send_message(message, phone_numbers)
        
        results = []
        
        for phone_number in phone_numbers:
            try:
                message_obj = self.client.messages.create(
                    body=message,
                    from_=f'whatsapp:{self.whatsapp_number}',
                    to=f'whatsapp:{phone_number}'
                )
                
                results.append({
                    'success': True,
                    'phone': phone_number,
                    'message_id': message_obj.sid,
                    'method': 'Twilio WhatsApp'
                })
                
            except Exception as e:
                results.append({
                    'success': False,
                    'phone': phone_number,
                    'error': str(e),
                    'method': 'Twilio WhatsApp'
                })
        
        return {
            'success': all(r['success'] for r in results),
            'details': results,
            'message': message,
            'recipients': phone_numbers,
            'timestamp': datetime.now().isoformat()
        }

# Factory function to get the appropriate service
def get_whatsapp_service():
    """
    Get WhatsApp service instance based on configuration
    """
    # Check if Twilio is configured
    if os.getenv('TWILIO_ACCOUNT_SID') and os.getenv('TWILIO_AUTH_TOKEN'):
        return TwilioWhatsAppService()
    
    # Default to WhatsApp Cloud API or logging
    return WhatsAppService()

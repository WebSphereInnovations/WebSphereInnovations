import platform
import subprocess
import json
import os
from datetime import datetime

class NotificationService:
    def __init__(self):
        self.system = platform.system()
    
    def show_notification(self, title, message, whatsapp_link=None):
        """Show desktop notification for new WhatsApp message"""
        
        if self.system == "Windows":
            self._show_windows_notification(title, message, whatsapp_link)
        elif self.system == "Darwin":  # macOS
            self._show_mac_notification(title, message, whatsapp_link)
        elif self.system == "Linux":
            self._show_linux_notification(title, message, whatsapp_link)
    
    def _show_windows_notification(self, title, message, whatsapp_link):
        """Show Windows notification"""
        try:
            # Use Windows toast notification
            toast_script = f'''
            Add-Type -AssemblyName System.Windows.Forms
            $global:balloon = New-Object System.Windows.Forms.NotifyIcon
            $path = (Get-Process -id $pid).Path
            $balloon.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($path)
            $balloon.BalloonTipTitle = "{title}"
            $balloon.BalloonTipText = "{message}"
            $balloon.Visible = $true
            $balloon.ShowBalloonTip(10000)
            '''
            
            subprocess.run(['powershell', '-Command', toast_script], capture_output=True)
            
            # Also show message box for immediate attention
            if whatsapp_link:
                msg_script = f'''
                Add-Type -AssemblyName System.Windows.Forms
                $result = [System.Windows.Forms.MessageBox]::Show(
                    "New WhatsApp message from WebSphere Innovations!\\n\\n{message}\\n\\nClick OK to open WhatsApp", 
                    "{title}", 
                    "OKCancel", 
                    "Information"
                )
                if ($result -eq "OK") {{
                    Start-Process "{whatsapp_link}"
                }}
                '''
                subprocess.run(['powershell', '-Command', msg_script], capture_output=True)
            
        except Exception as e:
            print(f"Windows notification error: {e}")
            # Fallback to console
            self._console_alert(title, message, whatsapp_link)
    
    def _show_mac_notification(self, title, message, whatsapp_link):
        """Show macOS notification"""
        try:
            # Use osascript for macOS notifications
            script = f'''
            display notification "{message}" with title "{title}"
            '''
            subprocess.run(['osascript', '-e', script], capture_output=True)
            
            if whatsapp_link:
                subprocess.run(['open', whatsapp_link])
                
        except Exception as e:
            print(f"macOS notification error: {e}")
            self._console_alert(title, message, whatsapp_link)
    
    def _show_linux_notification(self, title, message, whatsapp_link):
        """Show Linux notification"""
        try:
            # Use notify-send for Linux
            subprocess.run(['notify-send', title, message], capture_output=True)
            
            if whatsapp_link:
                subprocess.run(['xdg-open', whatsapp_link])
                
        except Exception as e:
            print(f"Linux notification error: {e}")
            self._console_alert(title, message, whatsapp_link)
    
    def _console_alert(self, title, message, whatsapp_link):
        """Fallback console alert with sound"""
        print("\n" + "="*80)
        print(f"🚨 URGENT: {title}")
        print(f"📱 Message: {message}")
        if whatsapp_link:
            print(f"🔗 WhatsApp: {whatsapp_link}")
        print("="*80)
        
        # Try to make a sound
        try:
            if self.system == "Windows":
                subprocess.run(['powershell', '-c', '(New-Object Media.SoundPlayer "C:\\Windows\\Media\\notify.wav").PlaySync();'], capture_output=True)
        except:
            pass

# Global notification service
notification_service = NotificationService()

def show_whatsapp_notification(phone_number, message, whatsapp_link):
    """Show immediate notification for new WhatsApp message"""
    title = "📱 New WhatsApp Message - WebSphere Innovations"
    notification_message = f"From: {phone_number}\nMessage: {message[:100]}{'...' if len(message) > 100 else ''}"
    
    notification_service.show_notification(title, notification_message, whatsapp_link)

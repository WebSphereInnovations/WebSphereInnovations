#!/usr/bin/env python3
"""
Real-time WhatsApp message monitor for WebSphere Innovations
This script monitors for new messages and provides immediate alerts
"""

import time
import json
import os
from datetime import datetime
from notification_service import show_whatsapp_notification
import webbrowser

class MessageMonitor:
    def __init__(self):
        self.log_file = 'logs/whatsapp_messages.log'
        self.last_position = 0
        self.processed_messages = set()
        
    def get_file_size(self):
        """Get current file size"""
        try:
            return os.path.getsize(self.log_file)
        except FileNotFoundError:
            return 0
    
    def read_new_messages(self):
        """Read new messages from log file"""
        try:
            current_size = self.get_file_size()
            
            if current_size < self.last_position:
                # File was truncated, restart from beginning
                self.last_position = 0
                self.processed_messages.clear()
            
            if current_size == self.last_position:
                return []  # No new messages
            
            with open(self.log_file, 'r') as f:
                f.seek(self.last_position)
                new_content = f.read()
                self.last_position = current_size
            
            # Parse new messages
            new_messages = []
            for line in new_content.strip().split('\n'):
                if line and line.strip():
                    try:
                        message_data = json.loads(line)
                        message_id = f"{message_data['timestamp']}_{message_data['phone']}"
                        
                        if message_id not in self.processed_messages:
                            self.processed_messages.add(message_id)
                            new_messages.append(message_data)
                    except json.JSONDecodeError:
                        continue
            
            return new_messages
            
        except FileNotFoundError:
            return []
    
    def process_message(self, message_data):
        """Process a single message and show alert"""
        phone = message_data.get('phone', 'Unknown')
        message = message_data.get('message', '')
        whatsapp_link = message_data.get('whatsapp_link', '')
        
        print("\n" + "="*80)
        print("🚨 NEW WHATSAPP MESSAGE RECEIVED!")
        print(f"📞 From: {phone}")
        print(f"💬 Message: {message}")
        print(f"⏰ Time: {message_data.get('timestamp', '')}")
        print("="*80)
        
        # Show desktop notification
        show_whatsapp_notification(phone, message, whatsapp_link)
        
        # Auto-open WhatsApp if link available
        if whatsapp_link:
            try:
                webbrowser.open(whatsapp_link)
                print(f"🌐 WhatsApp opened automatically!")
            except:
                print(f"🌐 Please manually open: {whatsapp_link}")
    
    def start_monitoring(self):
        """Start monitoring for new messages"""
        print("📱 WhatsApp Message Monitor Started")
        print(f"📁 Monitoring: {self.log_file}")
        print("🔄 Checking for new messages every 2 seconds...")
        print("⚠️  Press Ctrl+C to stop monitoring")
        print("="*80)
        
        # Initialize file position
        self.last_position = self.get_file_size()
        
        try:
            while True:
                new_messages = self.read_new_messages()
                
                for message in new_messages:
                    self.process_message(message)
                
                time.sleep(2)  # Check every 2 seconds
                
        except KeyboardInterrupt:
            print("\n\n👋 Message monitor stopped by user")
        except Exception as e:
            print(f"\n❌ Monitor error: {e}")

def main():
    """Main function to start the message monitor"""
    monitor = MessageMonitor()
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
        print("📁 Created logs directory")
    
    # Start monitoring
    monitor.start_monitoring()

if __name__ == "__main__":
    main()

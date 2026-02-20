#!/usr/bin/env python3
"""
Test WhatsApp messaging system
"""

from whatsapp_service import get_whatsapp_service
import time

def test_whatsapp():
    """Test WhatsApp messaging system"""
    print("🧪 Testing WhatsApp Messaging System")
    print("="*50)
    
    # Get WhatsApp service
    whatsapp_service = get_whatsapp_service()
    
    # Test message
    test_message = """🧪 TEST MESSAGE - WebSphere Innovations

This is a test message from the WhatsApp system.

📞 Test Phone: +91 7030720478
📞 Test Phone: +91 9168402327
⏰ Time: """ + time.strftime('%Y-%m-%d %H:%M:%S') + """
🌐 From: WebSphere Innovations Website Test"""

    # Recipients
    recipients = ["+91 7030720478", "+91 9168402327"]
    
    print(f"📱 Sending test message to: {recipients}")
    print(f"💬 Message: {test_message[:100]}...")
    print()
    
    # Send message
    result = whatsapp_service.send_message(test_message, recipients)
    
    print("📊 Results:")
    print(f"✅ Success: {result['success']}")
    print(f"📞 Recipients: {result['recipients']}")
    print(f"⏰ Time: {result['timestamp']}")
    print()
    
    for detail in result['details']:
        print(f"📱 Phone: {detail['phone']}")
        print(f"✅ Status: {detail['success']}")
        print(f"🔗 Method: {detail['method']}")
        if 'whatsapp_link' in detail:
            print(f"🌐 Link: {detail['whatsapp_link']}")
        print()
    
    print("🎯 Test completed!")
    print("💡 Check for desktop notifications and browser windows")
    print("📱 WhatsApp links should open automatically")

if __name__ == "__main__":
    test_whatsapp()

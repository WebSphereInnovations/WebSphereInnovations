#!/usr/bin/env python3
"""
Debug WhatsApp functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from whatsapp_service import get_whatsapp_service

def debug_whatsapp():
    print("🔍 DEBUGGING WHATSAPP FUNCTIONALITY")
    print("=" * 50)
    
    # Test WhatsApp service
    try:
        whatsapp_service = get_whatsapp_service()
        print("✅ WhatsApp service loaded successfully")
    except Exception as e:
        print(f"❌ WhatsApp service error: {e}")
        return
    
    # Test contact form
    print("\n📬 Testing Contact Form...")
    try:
        result = whatsapp_service.send_contact_notification(
            name="Test User",
            email="test@example.com",
            phone="+91 9876543210",
            message="This is a test message"
        )
        print(f"✅ Contact form result: {result['success']}")
        if result['success']:
            print(f"📞 Phone: {result.get('phone', 'N/A')}")
            print(f"🔗 Link: {result.get('whatsapp_link', 'N/A')}")
            print(f"📱 Mobile Link: {result.get('mobile_link', 'N/A')}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"❌ Contact form test error: {e}")
    
    # Test job application
    print("\n💼 Testing Job Application...")
    try:
        result = whatsapp_service.send_job_application_notification(
            job_title="Full Stack Developer",
            name="Test Applicant",
            email="applicant@example.com",
            phone="+91 9876543210",
            message="I am interested",
            cv_filename="test_resume.pdf"
        )
        print(f"✅ Job application result: {result['success']}")
        if result['success']:
            print(f"📞 Phone: {result.get('phone', 'N/A')}")
            print(f"🔗 Link: {result.get('whatsapp_link', 'N/A')}")
            print(f"📱 Mobile Link: {result.get('mobile_link', 'N/A')}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"❌ Job application test error: {e}")
    
    # Test chatbot
    print("\n🤖 Testing Chatbot...")
    try:
        result = whatsapp_service.send_chatbot_notification(
            transcript="User: Hello\nBot: Hi! How can I help you?\nUser: I need help\nBot: I'm here to help!"
        )
        print(f"✅ Chatbot result: {result['success']}")
        if result['success']:
            print(f"📞 Phone: {result.get('phone', 'N/A')}")
            print(f"🔗 Link: {result.get('whatsapp_link', 'N/A')}")
            print(f"📱 Mobile Link: {result.get('mobile_link', 'N/A')}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"❌ Chatbot test error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 DEBUGGING COMPLETE")
    print("📱 Check your WhatsApp for messages")
    print("📂 Check logs/whatsapp_messages.log for details")

if __name__ == "__main__":
    debug_whatsapp()

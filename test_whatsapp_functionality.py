#!/usr/bin/env python3
"""
Test WhatsApp functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from whatsapp_service import get_whatsapp_service

def test_whatsapp():
    print("🧪 Testing WhatsApp Functionality...")
    print("=" * 50)
    
    # Get WhatsApp service
    whatsapp_service = get_whatsapp_service()
    
    # Test 1: Contact Form
    print("\n📬 Testing Contact Form Notification...")
    contact_result = whatsapp_service.send_contact_notification(
        name="Test User",
        email="test@example.com", 
        phone="+91 9876543210",
        message="This is a test message from contact form"
    )
    
    print(f"✅ Contact Form Result: {contact_result['success']}")
    if contact_result['success']:
        print(f"📞 Phone: {contact_result.get('phone', 'N/A')}")
        print(f"🔗 WhatsApp Link: {contact_result.get('whatsapp_link', 'N/A')}")
    
    # Test 2: Job Application
    print("\n💼 Testing Job Application Notification...")
    job_result = whatsapp_service.send_job_application_notification(
        job_title="Full Stack Developer",
        name="Test Applicant",
        email="applicant@example.com",
        phone="+91 9876543210", 
        message="I am interested in this position",
        cv_filename="test_resume.pdf"
    )
    
    print(f"✅ Job Application Result: {job_result['success']}")
    if job_result['success']:
        print(f"📞 Phone: {job_result.get('phone', 'N/A')}")
        print(f"🔗 WhatsApp Link: {job_result.get('whatsapp_link', 'N/A')}")
    
    # Test 3: Chatbot
    print("\n🤖 Testing Chatbot Notification...")
    chatbot_result = whatsapp_service.send_chatbot_notification(
        transcript="User: Hello\nBot: Hi! How can I help you?\nUser: I need information about services\nBot: We offer cybersecurity, software development, data analytics, and cloud solutions."
    )
    
    print(f"✅ Chatbot Result: {chatbot_result['success']}")
    if chatbot_result['success']:
        print(f"📞 Phone: {chatbot_result.get('phone', 'N/A')}")
        print(f"🔗 WhatsApp Link: {chatbot_result.get('whatsapp_link', 'N/A')}")
    
    print("\n" + "=" * 50)
    print("🎉 WhatsApp Functionality Test Complete!")
    print("📱 Check your WhatsApp for messages (if auto-open worked)")
    print("📂 Check logs/whatsapp_messages.log for all messages")

if __name__ == "__main__":
    test_whatsapp()

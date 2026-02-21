#!/usr/bin/env python3
"""
Logo Setup Script
"""

import os
import shutil

def setup_logo():
    """Setup logo file"""
    
    logo_path = "static/images/websphere-logo.png"
    
    # Check if logo file exists
    if os.path.exists(logo_path):
        file_size = os.path.getsize(logo_path)
        print(f"📋 Current logo file: {logo_path}")
        print(f"📊 File size: {file_size} bytes")
        
        if file_size == 0:
            print("❌ Logo file is empty (0 bytes)")
            print("🔧 Please replace with your actual logo image")
            print()
            print("📋 INSTRUCTIONS:")
            print("1. Copy your logo image file")
            print("2. Rename it to 'websphere-logo.png'")
            print("3. Paste it in 'static/images/' folder")
            print("4. Replace the existing empty file")
            print()
            print("🎯 LOGO REQUIREMENTS:")
            print("- Format: PNG (recommended) or JPG")
            print("- Size: 200x40 pixels (recommended)")
            print("- Background: Transparent (PNG) preferred")
            print("- Quality: High resolution")
        else:
            print("✅ Logo file exists and has content")
            print("🎯 Logo should be visible on website")
    else:
        print("❌ Logo file not found")
        print("🔧 Creating placeholder logo file")
        
        # Create a simple text-based placeholder
        with open(logo_path, 'w') as f:
            f.write("# Logo placeholder - replace with actual image")
        
        print("✅ Placeholder created")
        print("📋 Please replace with your actual logo image")

if __name__ == "__main__":
    setup_logo()

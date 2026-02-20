#!/usr/bin/env python3
"""
Deploy WebSphere Innovations to Koyeb
This script will deploy the website to Koyeb free hosting
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🚀 {description}")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success: {result.stdout}")
            return True
        else:
            print(f"❌ Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    print("🌟 WebSphere Innovations - Koyeb Deployment")
    print("=" * 50)
    
    # Check if koyeb CLI is installed
    if not run_command("koyeb version", "Checking Koyeb CLI"):
        print("\n❌ Koyeb CLI not found!")
        print("Please install Koyeb CLI:")
        print("1. Visit: https://www.koyeb.com/docs/getting-started/install-cli")
        print("2. Download and install Koyeb CLI")
        print("3. Run: koyeb login")
        print("4. Run this script again")
        return
    
    print("\n✅ Koyeb CLI found!")
    
    # Deploy to Koyeb
    deploy_command = "koyeb deploy --name websphere-innovations --github-repo WebSphereInnovations/WebSphereInnovations --branch master --port 5000 --env PORT=5000"
    
    if run_command(deploy_command, "Deploying to Koyeb"):
        print("\n🎉 Deployment successful!")
        print("\n📱 Your website will be available at:")
        print("   https://websphere-innovations.koyeb.app")
        print("   https://websphere-innovations-admin.koyeb.app (for admin panel)")
        print("\n🔄 Auto-deployment enabled!")
        print("   Any push to GitHub will automatically update your live site!")
        
        print("\n📋 Next Steps:")
        print("1. Wait 2-3 minutes for deployment to complete")
        print("2. Visit: https://websphere-innovations.koyeb.app")
        print("3. Test admin panel: https://websphere-innovations-admin.koyeb.app")
        print("4. Any future changes to GitHub will auto-deploy!")
        
    else:
        print("\n❌ Deployment failed!")
        print("Please check the error message above and try again.")
        print("You can also deploy manually at: https://app.koyeb.com")

if __name__ == "__main__":
    main()

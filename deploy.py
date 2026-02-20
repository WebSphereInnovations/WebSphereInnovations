#!/usr/bin/env python3
"""
Deployment script for WebSphere Innovations website
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*50}")
    print(f"Executing: {description}")
    print(f"Command: {command}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Success: {description}")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description}")
        print(f"Error message: {e.stderr}")
        return False

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("Checking prerequisites...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    else:
        print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check required files
    required_files = [
        'app.py',
        'requirements.txt',
        'whatsapp_service.py',
        'templates/base.html',
        'static/css/style.css',
        'static/js/script.js'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Required file missing: {file}")
            return False
        else:
            print(f"✅ Found: {file}")
    
    return True

def setup_git():
    """Initialize Git repository and push to GitHub"""
    print("\n🚀 Setting up Git repository...")
    
    commands = [
        ("git init", "Initialize Git repository"),
        ("git add .", "Add all files to staging"),
        ("git commit -m 'Initial commit: WebSphere Innovations website'", "Create initial commit"),
        ("git branch -M main", "Set main branch"),
        ("git remote add origin https://github.com/WebSphereInnovations/WebSphereInnovations.git", "Add remote origin"),
        ("git push -u origin main", "Push to GitHub")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            print(f"⚠️  Failed to execute: {description}")
            print("   You may need to run this manually or check your Git setup")
            return False
    
    return True

def create_deployment_instructions():
    """Create deployment instructions file"""
    instructions = """
# Deployment Instructions for WebSphere Innovations Website

## Local Development Setup

1. **Install Python 3.8+**
   ```bash
   # Download from https://python.org
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/WebSphereInnovations/WebSphereInnovations.git
   cd WebSphereInnovations
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python app.py
   ```

5. **Access Website**
   - Main Site: http://localhost:5000
   - Admin Panel: http://localhost:5000/admin

## Production Deployment

### Option 1: Heroku
1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variables:
   ```bash
   heroku config:set WHATSAPP_PHONE_ID="your_phone_id"
   heroku config:set WHATSAPP_ACCESS_TOKEN="your_access_token"
   ```
5. Deploy: `git push heroku main`

### Option 2: PythonAnywhere
1. Create account on PythonAnywhere
2. Create new Web app
3. Upload code via Git or manual upload
4. Install requirements in virtual environment
5. Configure WSGI file
6. Set environment variables

### Option 3: VPS/Dedicated Server
1. Install Python and pip
2. Install Nginx as reverse proxy
3. Install Gunicorn WSGI server
4. Configure systemd service
5. Set up SSL certificate

## WhatsApp Configuration

### Development Mode (Default)
- Messages logged to `logs/whatsapp_messages.log`
- No API keys required

### Production Mode
Set environment variables:

**WhatsApp Cloud API:**
```bash
export WHATSAPP_PHONE_ID="your_phone_id"
export WHATSAPP_ACCESS_TOKEN="your_access_token"
```

**Twilio WhatsApp:**
```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_WHATSAPP_NUMBER="your_twilio_number"
```

## Admin Access

- **URL**: http://your-domain.com/admin
- **Username**: WebSphereInnovations
- **Password**: R@hul#1999

## Important Notes

1. **Change Default Password**: Update admin password after first login
2. **Configure WhatsApp**: Set up API credentials for production
3. **Backup Data**: Regularly backup the `data/` directory
4. **Monitor Logs**: Check `logs/` directory for WhatsApp message logs
5. **Update Content**: Use admin panel to manage all website content

## Troubleshooting

### Common Issues

1. **Port 5000 already in use**
   ```bash
   # Kill existing process
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```

2. **Dependencies not found**
   ```bash
   pip install -r requirements.txt
   ```

3. **WhatsApp messages not sending**
   - Check API credentials
   - Verify phone number format
   - Check logs for errors

4. **Admin panel not accessible**
   - Clear browser cache
   - Verify credentials
   - Check session configuration

## Support

For technical support:
- Email: info@websphereinnovations.com
- Phone: +91 7030720478
- WhatsApp: +91 7030720478
"""
    
    with open('DEPLOYMENT.md', 'w') as f:
        f.write(instructions)
    
    print("✅ Created DEPLOYMENT.md with deployment instructions")

def main():
    """Main deployment function"""
    print("🌐 WebSphere Innovations Website Deployment")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites check failed. Please fix the issues above.")
        return False
    
    # Create deployment instructions
    create_deployment_instructions()
    
    # Ask user if they want to setup Git
    try:
        response = input("\n🚀 Do you want to setup Git and push to GitHub? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            if setup_git():
                print("\n🎉 Successfully deployed to GitHub!")
                print("📁 Repository: https://github.com/WebSphereInnovations/WebSphereInnovations")
            else:
                print("\n⚠️  Git setup failed. Please check your Git configuration.")
        else:
            print("\n✅ Skipping Git setup. You can manually push to GitHub later.")
    except KeyboardInterrupt:
        print("\n\n👋 Deployment cancelled by user.")
        return False
    
    print("\n🎯 Next Steps:")
    print("1. Review DEPLOYMENT.md for detailed instructions")
    print("2. Configure WhatsApp API credentials for production")
    print("3. Deploy to your preferred hosting platform")
    print("4. Test all functionality including WhatsApp notifications")
    print("5. Update admin password for security")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

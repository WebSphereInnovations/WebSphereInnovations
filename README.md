# WebSphere Innovations - Dynamic Website

A modern, responsive, and dynamic website for WebSphere Innovations, an IT company specializing in Cybersecurity, Software Development, Data Analytics, and Cloud Solutions.

## Features

### Main Website
- **Responsive Design**: Mobile-friendly layout with dark theme
- **Dynamic Content**: All content manageable through admin panel
- **Interactive Chatbot**: Service selection with WhatsApp notifications
- **Contact Forms**: Direct WhatsApp notifications to admin
- **Job Applications**: CV upload with instant WhatsApp alerts
- **Modern UI**: Professional corporate look with smooth animations

### Admin Panel
- **Secure Authentication**: Username/password protected admin area
- **Content Management**: Edit all website content dynamically
- **Job Management**: Add, edit, delete job postings
- **WhatsApp Configuration**: Manage notification recipients
- **Real-time Updates**: Changes reflected immediately on website

### WhatsApp Integration
- **Contact Form Notifications**: Instant alerts for new inquiries
- **Job Application Alerts**: Immediate notifications with CV details
- **Chatbot Conversations**: Full transcript sent via WhatsApp
- **Multiple Recipients**: Support for multiple admin numbers
- **Fallback Logging**: Development mode with message logging

## Technology Stack

### Backend
- **Python Flask**: Web framework
- **JSON Storage**: File-based data management (no database required)
- **WhatsApp API**: Cloud API or Twilio integration
- **File Upload**: CV and document handling

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Font Awesome**: Icon library
- **Vanilla JavaScript**: Interactive features and chatbot
- **CSS3**: Custom styling with animations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or Download the Project**
   ```bash
   # If using Git
   git clone https://github.com/WebSphereInnovations/WebSphereInnovations.git
   cd WebSphereInnovations
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Website**
   - Main Website: http://localhost:5000
   - Admin Panel: http://localhost:5000/admin

### Default Admin Credentials
- **Username**: WebSphereInnovations
- **Password**: R@hul#1999

## WhatsApp Configuration

### Option 1: Development Mode (Default)
- Messages are logged to `logs/whatsapp_messages.log`
- Console output for immediate visibility
- No API keys required

### Option 2: WhatsApp Cloud API
Set these environment variables:
```bash
export WHATSAPP_PHONE_ID="your_phone_id"
export WHATSAPP_ACCESS_TOKEN="your_access_token"
```

### Option 3: Twilio WhatsApp
Set these environment variables:
```bash
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export TWILIO_WHATSAPP_NUMBER="your_twilio_whatsapp_number"
```

## Project Structure

```
WebSphereInnovations/
├── app.py                 # Main Flask application
├── whatsapp_service.py    # WhatsApp integration service
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/                 # JSON data files
│   ├── company_info.json
│   ├── services.json
│   ├── projects.json
│   ├── jobs.json
│   ├── contact_form_recipients.json
│   └── admin_credentials.json
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── services.html
│   ├── projects.html
│   ├── contact.html
│   ├── jobs.html
│   └── admin/
│       ├── login.html
│       └── dashboard.html
├── static/              # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── uploads/             # File uploads (CVs)
└── logs/               # WhatsApp message logs
```

## Admin Panel Features

### Company Information Management
- Edit company name, tagline, description
- Update contact details (phone, email, WhatsApp)
- Modify address and copyright year

### Services Management
- Update service titles and descriptions
- Modify service offerings
- Real-time website updates

### Jobs Management
- Add new job postings
- Edit existing job details
- Delete outdated positions
- Track posting dates

### WhatsApp Configuration
- Add/remove notification recipients
- Configure multiple admin numbers
- Test message delivery

## Chatbot Features

### Service Selection Flow
1. **Initial Greeting**: "How can I help you today regarding our services?"
2. **Service Categories**: Cybersecurity, Software Development, Data Analytics, Cloud Solutions
3. **Sub-Service Options**: Detailed service-specific choices
4. **Requirements Collection**: Free text input for detailed queries
5. **Contact Information**: Provides contact details for follow-up

### WhatsApp Integration
- Full conversation transcript sent to admin
- Immediate notification without user action
- Includes all user selections and messages
- Timestamp and session details

## File Storage System

### Data Management
- **JSON Files**: All content stored in JSON format
- **No Database**: File-based storage for simplicity
- **Automatic Backups**: Easy to backup and migrate
- **Version Control**: Track changes with Git

### Upload Handling
- **CV Storage**: Uploaded resumes saved to `/uploads`
- **File Security**: Filename sanitization
- **Storage Management**: Organized file structure

## Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. **Set Environment Variables**
2. **Configure WhatsApp API**
3. **Use WSGI Server** (Gunicorn, uWSGI)
4. **Set Up Reverse Proxy** (Nginx, Apache)
5. **Enable HTTPS** (SSL Certificate)

### Environment Variables
```bash
export FLASK_ENV=production
export SECRET_KEY="your_secret_key"
export WHATSAPP_PHONE_ID="your_phone_id"
export WHATSAPP_ACCESS_TOKEN="your_access_token"
```

## Security Features

### Authentication
- Session-based admin authentication
- Secure password handling
- Session timeout protection

### Input Validation
- Form validation on all inputs
- File upload security
- XSS protection

### Data Protection
- No sensitive data in client-side code
- Secure file handling
- Input sanitization

## Customization

### Branding
- Update company information via admin panel
- Modify colors in CSS variables
- Add custom logos and images

### Features
- Add new services via admin panel
- Modify chatbot conversation flow
- Extend WhatsApp notifications

### Integration
- Add analytics tracking
- Integrate CRM systems
- Connect to marketing tools

## Troubleshooting

### Common Issues

1. **WhatsApp Messages Not Sending**
   - Check API credentials
   - Verify phone number format
   - Check logs for errors

2. **Admin Panel Not Accessible**
   - Verify credentials
   - Clear browser cache
   - Check session configuration

3. **File Uploads Not Working**
   - Check uploads directory permissions
   - Verify file size limits
   - Check file format restrictions

### Debug Mode
Enable debug mode for development:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

## Support

For technical support or questions:
- **Email**: info@websphereinnovations.com
- **Phone**: +91 7030720478
- **WhatsApp**: +91 7030720478

## License

This project is proprietary to WebSphere Innovations. All rights reserved.

---

**WebSphere Innovations** - Innovative IT Solutions
Established 2024
© 2024 WebSphere Innovations. All rights reserved.

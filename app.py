from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
import json
import os
import requests
from datetime import datetime
from werkzeug.utils import secure_filename
import secrets
from whatsapp_service import get_whatsapp_service

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Data storage files
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Initialize default data
def init_data():
    default_data = {
        "company_info": {
            "name": "WebSphere Innovations",
            "tagline": "Innovative IT Solutions",
            "description": "WebSphere Innovations, established in 2024, is an IT company specializing in Cybersecurity, Software Development, Data Analytics, and Cloud Solutions.",
            "phone": "+91 7030720478",
            "email": "info@websphereinnovations.com",
            "whatsapp": "+91 7030720478",
            "address": "Your Address Here",
            "copyright_year": "2024"
        },
        "services": {
            "cybersecurity": {
                "title": "Cybersecurity",
                "description": "Protect your business from digital threats with advanced security solutions.",
                "icon": "shield"
            },
            "software_development": {
                "title": "Software Development",
                "description": "Custom software solutions tailored to your business needs.",
                "icon": "code"
            },
            "data_analytics": {
                "title": "Data Analytics",
                "description": "Transform data into actionable insights with advanced analytics.",
                "icon": "chart"
            },
            "cloud_solutions": {
                "title": "Cloud Solutions",
                "description": "Scalable cloud infrastructure for your digital transformation.",
                "icon": "cloud"
            }
        },
        "projects": [],
        "jobs": [
            {
                "id": 1,
                "title": "Full Stack Developer",
                "experience": "5 years experience",
                "description": "Looking for experienced full stack developer with expertise in modern web technologies.",
                "posted_date": "2024-01-15"
            },
            {
                "id": 2,
                "title": "Software Developer",
                "experience": "3+ years experience",
                "description": "Join our team to develop innovative software solutions for clients.",
                "posted_date": "2024-01-10"
            },
            {
                "id": 3,
                "title": "Tester",
                "experience": "2+ years experience",
                "description": "Quality assurance professional to ensure product excellence.",
                "posted_date": "2024-01-05"
            }
        ],
        "contact_form_recipients": ["+91 7030720478", "+91 9168402327"],
        "admin_credentials": {
            "username": "WebSphereInnovations",
            "password": "R@hul#1999"
        }
    }
    
    for filename, data in default_data.items():
        filepath = os.path.join(DATA_DIR, f"{filename}.json")
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

init_data()

def load_data(filename):
    filepath = os.path.join(DATA_DIR, f"{filename}.json")
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    filepath = os.path.join(DATA_DIR, f"{filename}.json")
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def send_whatsapp_message(message, recipients=None):
    """Send WhatsApp message to recipients"""
    if recipients is None:
        recipients = ["+91 7030720478", "+91 9168402327"]
    
    try:
        whatsapp_service = get_whatsapp_service()
        result = whatsapp_service.send_message(message, recipients)
        
        # Log result
        print(f"WhatsApp message sent: {result['success']}")
        return result
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return {'success': False, 'error': str(e)}

# Routes
@app.route('/')
def home():
    company_info = load_data('company_info')
    services = load_data('services')
    return render_template('index.html', company_info=company_info, services=services)

@app.route('/services')
def services():
    company_info = load_data('company_info')
    services = load_data('services')
    return render_template('services.html', company_info=company_info, services=services)

@app.route('/projects')
def projects():
    company_info = load_data('company_info')
    projects = load_data('projects')
    return render_template('projects.html', company_info=company_info, projects=projects)

@app.route('/team')
def team():
    company_info = load_data('company_info')
    try:
        team_data = load_data('team')
    except FileNotFoundError:
        team_data = {
            'ceo': {'enabled': False},
            'md': {'enabled': False},
            'members': []
        }
    
    return render_template('team.html', company_info=company_info, team=team_data)

@app.route('/contact')
def contact():
    company_info = load_data('company_info')
    return render_template('contact.html', company_info=company_info)

@app.route('/jobs')
def jobs():
    company_info = load_data('company_info')
    jobs_data = load_data('jobs')
    return render_template('jobs.html', company_info=company_info, jobs=jobs_data)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        if not all([name, email, message]):
            return jsonify({'success': False, 'message': 'Please fill in all required fields'})
        
        # Use WhatsApp service to send notification
        try:
            # Use user WhatsApp service for direct link generation
            from user_whatsapp_service import get_user_whatsapp_service
            whatsapp_service = get_user_whatsapp_service()
            
            # Generate user WhatsApp link
            result = whatsapp_service.send_contact_notification(name, email, phone, message)
            
            if result['success']:
                print(f"✅ User WhatsApp link generated successfully")
                return jsonify({
                    'success': True, 
                    'message': 'Thank you for contacting us! Click the WhatsApp link to send us your message directly.',
                    'whatsapp_link': result.get('user_whatsapp_link', ''),
                    'user_action_required': True
                })
            else:
                print(f"❌ User WhatsApp link generation failed: {result}")
                return jsonify({'success': False, 'message': 'Error generating WhatsApp link. Please try again.'})
                
        except Exception as whatsapp_error:
            print(f"❌ WhatsApp service error: {whatsapp_error}")
            # Still return success even if WhatsApp fails
            return jsonify({'success': True, 'message': 'Thank you for contacting us! We will get back to you soon.'})
    
    except Exception as e:
        print(f"Contact form error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'})

@app.route('/apply_job', methods=['POST'])
def apply_job():
    try:
        job_id = request.form.get('job_id')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        if not all([job_id, name, email, message]):
            return jsonify({'success': False, 'message': 'Please fill in all required fields'})
        
        # Handle file upload
        cv_file = request.files.get('cv')
        cv_info = {'success': False}
        
        if cv_file:
            # Use CV file handler
            from cv_file_handler import get_cv_handler
            cv_handler = get_cv_handler()
            cv_info = cv_handler.save_cv_file(cv_file, name)
        
        # Use WhatsApp service to send notification
        try:
            # Use user WhatsApp service for direct link generation
            from user_whatsapp_service import get_user_whatsapp_service
            whatsapp_service = get_user_whatsapp_service()
            
            # Generate user WhatsApp link for job application
            result = whatsapp_service.send_job_application_notification(
                job_id, name, email, phone, message, 
                cv_info.get('filename', ''), 
                cv_info.get('file_path', ''), 
                cv_info.get('file_size', 0)
            )
            
            if result['success']:
                print(f"✅ User WhatsApp link generated for job application")
                return jsonify({
                    'success': True, 
                    'message': 'Thank you for applying! Click the WhatsApp link to send us your application directly.',
                    'whatsapp_link': result.get('user_whatsapp_link', ''),
                    'user_action_required': True
                })
            else:
                print(f"❌ User WhatsApp link generation failed: {result}")
                return jsonify({'success': False, 'message': 'Error generating WhatsApp link. Please try again.'})
                
        except Exception as whatsapp_error:
            print(f"❌ WhatsApp service error: {whatsapp_error}")
            # Still return success even if WhatsApp fails
            return jsonify({'success': True, 'message': 'Thank you for applying! We will review your application and get back to you soon.'})
    
    except Exception as e:
        print(f"Job application error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'})

@app.route('/chatbot_submit', methods=['POST'])
def chatbot_submit():
    try:
        chat_transcript = request.form.get('transcript')
        
        if not chat_transcript:
            return jsonify({'success': False, 'message': 'No transcript provided'})
        
        # Use WhatsApp service to send notification
        try:
            # Use user WhatsApp service for direct link generation
            from user_whatsapp_service import get_user_whatsapp_service
            whatsapp_service = get_user_whatsapp_service()
            
            # Generate user WhatsApp link for chatbot
            result = whatsapp_service.send_chatbot_notification(chat_transcript)
            
            if result['success']:
                print(f"✅ User WhatsApp link generated for chatbot")
                return jsonify({
                    'success': True, 
                    'message': 'Thank you for using our chatbot! Click the WhatsApp link to send us the conversation directly.',
                    'whatsapp_link': result.get('user_whatsapp_link', ''),
                    'user_action_required': True
                })
            else:
                print(f"❌ User WhatsApp link generation failed: {result}")
                return jsonify({'success': False, 'message': 'Error generating WhatsApp link. Please try again.'})
                
        except Exception as whatsapp_error:
            print(f"❌ WhatsApp service error: {whatsapp_error}")
            # Still return success even if WhatsApp fails
            return jsonify({'success': True, 'message': 'Chat transcript sent successfully'})
    
    except Exception as e:
        print(f"Chatbot submission error: {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again.'})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    try:
        return send_from_directory('uploads', filename)
    except FileNotFoundError:
        return "File not found", 404

@app.route('/whatsapp-links')
def whatsapp_links():
    """Serve WhatsApp links page for easy access to send messages"""
    try:
        with open('whatsapp_links.html', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "WhatsApp links page not found", 404

@app.route('/logs/whatsapp_links.log')
def whatsapp_links_log():
    """Serve WhatsApp links log file"""
    try:
        with open('logs/whatsapp_links.log', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "No links found", 404

# Admin Routes
@app.route('/admin')
def admin():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    return render_template('admin/dashboard.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        credentials = load_data('admin_credentials')
        
        if username == credentials['username'] and password == credentials['password']:
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/api/company_info', methods=['GET', 'POST'])
def api_company_info():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        save_data('company_info', data)
        return jsonify({'success': True})
    
    return jsonify(load_data('company_info'))

@app.route('/api/services', methods=['GET', 'POST'])
def api_services():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        save_data('services', data)
        return jsonify({'success': True})
    
    return jsonify(load_data('services'))

@app.route('/api/projects', methods=['GET', 'POST'])
def api_projects():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        save_data('projects', data)
        return jsonify({'success': True})
    
    return jsonify(load_data('projects'))

@app.route('/api/team', methods=['GET', 'POST'])
def api_team():
    if request.method == 'GET':
        try:
            team_data = load_data('team')
            return jsonify(team_data)
        except FileNotFoundError:
            default_team = {
                'ceo': {'enabled': False},
                'md': {'enabled': False},
                'members': []
            }
            save_data('team', default_team)
            return jsonify(default_team)
    
    elif request.method == 'POST':
        team_data = request.json
        save_data('team', team_data)
        return jsonify({'success': True, 'message': 'Team data saved successfully'})

@app.route('/api/jobs', methods=['GET', 'POST'])
def api_jobs():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        # Add posting date if not present
        if isinstance(data, list):
            for job in data:
                if 'posted_date' not in job:
                    job['posted_date'] = datetime.now().strftime('%Y-%m-%d')
        elif isinstance(data, dict):
            if 'posted_date' not in data:
                data['posted_date'] = datetime.now().strftime('%Y-%m-%d')
        
        save_data('jobs', data)
        return jsonify({'success': True})
    
    jobs = load_data('jobs')
    # Add posting date if missing
    if isinstance(jobs, list):
        for job in jobs:
            if 'posted_date' not in job:
                job['posted_date'] = datetime.now().strftime('%Y-%m-%d')
    
    return jsonify(jobs)

@app.route('/api/settings', methods=['GET', 'POST'])
def api_settings():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        
        # Handle password change
        if 'current_password' in data and 'new_password' in data:
            current_password = data.get('current_password')
            new_password = data.get('new_password')
            
            # Load current credentials
            credentials = load_data('admin_credentials')
            
            if credentials.get('password') == current_password:
                credentials['password'] = new_password
                save_data('admin_credentials', credentials)
                return jsonify({'success': True, 'message': 'Password changed successfully'})
            else:
                return jsonify({'success': False, 'message': 'Current password is incorrect'})
        
        # Handle WhatsApp mode
        if 'whatsapp_mode' in data:
            settings = load_data('settings') if os.path.exists('data/settings.json') else {}
            settings['whatsapp_mode'] = data.get('whatsapp_mode', 'direct')
            save_data('settings', settings)
            return jsonify({'success': True, 'message': 'Settings saved successfully'})
        
        return jsonify({'success': False, 'message': 'Invalid request'})
    
    else:  # GET request
        settings = load_data('settings') if os.path.exists('data/settings.json') else {}
        return jsonify(settings)

@app.route('/api/recipients', methods=['GET', 'POST'])
def api_recipients():
    if 'admin_logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    if request.method == 'POST':
        data = request.get_json()
        save_data('contact_form_recipients', data)
        return jsonify({'success': True})
    
    return jsonify(load_data('contact_form_recipients'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

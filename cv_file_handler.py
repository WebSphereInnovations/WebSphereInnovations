#!/usr/bin/env python3
"""
CV File Handler - Resume File Management
"""

import os
import shutil
from datetime import datetime

class CVFileHandler:
    def __init__(self):
        self.upload_folder = 'uploads'
        self.ensure_upload_folder()
    
    def ensure_upload_folder(self):
        """Ensure upload folder exists"""
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)
    
    def save_cv_file(self, cv_file, applicant_name):
        """Save CV file with proper naming"""
        try:
            if cv_file:
                # Get file extension
                filename = cv_file.filename
                if filename:
                    # Create safe filename with applicant name and timestamp
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    safe_name = f"{applicant_name.replace(' ', '_')}_{timestamp}_{filename}"
                    safe_name = safe_name.replace('/', '_').replace('\\', '_')
                    
                    # Save file
                    file_path = os.path.join(self.upload_folder, safe_name)
                    cv_file.save(file_path)
                    
                    # Get file size
                    file_size = os.path.getsize(file_path)
                    
                    return {
                        'success': True,
                        'filename': safe_name,
                        'original_filename': filename,
                        'file_path': file_path,
                        'file_size': file_size,
                        'file_size_kb': round(file_size / 1024, 2)
                    }
            
            return {'success': False, 'error': 'No file provided'}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_cv_info(self, file_path):
        """Get CV file information"""
        try:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                file_extension = os.path.splitext(file_path)[1].lower()
                
                return {
                    'exists': True,
                    'file_size': file_size,
                    'file_size_kb': round(file_size / 1024, 2),
                    'file_extension': file_extension,
                    'file_path': file_path
                }
            else:
                return {'exists': False}
                
        except Exception as e:
            return {'exists': False, 'error': str(e)}
    
    def create_cv_download_link(self, file_path, base_url="https://websphere-innovations.onrender.com"):
        """Create download link for CV file"""
        try:
            if os.path.exists(file_path):
                filename = os.path.basename(file_path)
                download_url = f"{base_url}/uploads/{filename}"
                return download_url
            else:
                return None
        except:
            return None
    
    def format_cv_message(self, cv_info):
        """Format CV information for WhatsApp message"""
        if cv_info['success']:
            return f"""📎 CV File Details:
📄 Name: {cv_info['original_filename']}
💾 Size: {cv_info['file_size_kb']} KB
📂 Path: {cv_info['filename']}
🕐 Uploaded: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""
        else:
            return "📎 CV: Not provided"

# Global instance
cv_handler = CVFileHandler()

def get_cv_handler():
    return cv_handler

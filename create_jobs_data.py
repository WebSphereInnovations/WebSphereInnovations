#!/usr/bin/env python3
"""
Create Jobs Data Script
"""

import json
import os

def create_jobs_data():
    """Create proper jobs data"""
    
    jobs_data = {
        "positions": [
            {
                "id": "job_1",
                "title": "Software Developer",
                "description": "We are looking for a skilled Software Developer to join our team. You will work on cutting-edge projects and develop innovative solutions.",
                "experience": "2-3 years",
                "posted_date": "2024-01-15"
            },
            {
                "id": "job_2",
                "title": "Full Stack Developer",
                "description": "Join our team as a Full Stack Developer and work on exciting projects. You will be responsible for end-to-end web application development.",
                "experience": "3-5 years",
                "posted_date": "2024-01-10"
            },
            {
                "id": "job_3",
                "title": "Data Scientist",
                "description": "We are seeking a talented Data Scientist to help us analyze complex data and build machine learning models.",
                "experience": "2-4 years",
                "posted_date": "2024-01-08"
            }
        ]
    }
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Write to jobs.json
    with open('data/jobs.json', 'w') as f:
        json.dump(jobs_data, f, indent=4)
    
    print("✅ Jobs data created successfully!")
    print(f"📊 Created {len(jobs_data['positions'])} job positions")
    
    return jobs_data

if __name__ == "__main__":
    create_jobs_data()

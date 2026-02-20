// Chatbot functionality
class Chatbot {
    constructor() {
        this.isOpen = false;
        this.currentStep = 'services';
        this.userSelections = {
            services: [],
            subServices: [],
            requirements: ''
        };
        this.transcript = [];
        
        this.serviceOptions = {
            'Cybersecurity': ['Penetration Testing', 'Security Audit', 'Risk Assessment', 'Incident Response', 'Compliance Consulting'],
            'Software Development': ['Custom Software', 'Mobile Apps', 'Web Applications', 'API Development', 'Testing & QA'],
            'Data Analytics': ['Data Visualization', 'Predictive Analytics', 'Big Data Processing', 'Reporting & Dashboards', 'Data Warehousing'],
            'Cloud Solutions': ['Cloud Migration', 'Infrastructure Setup', 'Cloud Security', 'Managed Services', 'Backup & Recovery']
        };
        
        this.init();
    }
    
    init() {
        // DOM elements
        this.bubble = document.getElementById('chatbotBubble');
        this.window = document.getElementById('chatbotWindow');
        this.closeBtn = document.getElementById('chatbotClose');
        this.messagesContainer = document.getElementById('chatbotMessages');
        this.input = document.getElementById('chatbotInput');
        this.sendBtn = document.getElementById('chatbotSend');
        
        // Event listeners
        this.bubble.addEventListener('click', () => this.toggle());
        this.closeBtn.addEventListener('click', () => this.close());
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        
        // Add initial message
        this.addMessage('bot', 'How can I help you today regarding our services? Please choose an option:');
        this.showServiceOptions();
    }
    
    toggle() {
        this.isOpen = !this.isOpen;
        this.window.classList.toggle('active', this.isOpen);
    }
    
    close() {
        this.isOpen = false;
        this.window.classList.remove('active');
    }
    
    addMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `${sender}-message`;
        messageDiv.textContent = message;
        this.messagesContainer.appendChild(messageDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
        
        // Add to transcript
        this.transcript.push(`${sender === 'bot' ? 'Bot' : 'User'}: ${message}`);
    }
    
    showServiceOptions() {
        const optionsDiv = document.createElement('div');
        optionsDiv.className = 'chatbot-options';
        
        Object.keys(this.serviceOptions).forEach(service => {
            const option = document.createElement('div');
            option.className = 'chatbot-option';
            option.textContent = service;
            option.addEventListener('click', () => this.selectService(service));
            optionsDiv.appendChild(option);
        });
        
        this.messagesContainer.appendChild(optionsDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
    
    selectService(service) {
        this.userSelections.services.push(service);
        this.addMessage('user', service);
        
        // Remove options
        const optionsDiv = this.messagesContainer.querySelector('.chatbot-options');
        if (optionsDiv) {
            optionsDiv.remove();
        }
        
        // Show sub-services
        this.addMessage('bot', `Great choice! What specific ${service} services are you interested in? You can select multiple options:`);
        this.showSubServiceOptions(service);
    }
    
    showSubServiceOptions(service) {
        const optionsDiv = document.createElement('div');
        optionsDiv.className = 'chatbot-options';
        
        this.serviceOptions[service].forEach(subService => {
            const option = document.createElement('div');
            option.className = 'chatbot-option';
            option.textContent = subService;
            option.addEventListener('click', () => this.selectSubService(subService));
            optionsDiv.appendChild(option);
        });
        
        // Add "Done" button
        const doneOption = document.createElement('div');
        doneOption.className = 'chatbot-option';
        doneOption.textContent = 'Done with selections';
        doneOption.style.background = 'var(--accent-color)';
        doneOption.addEventListener('click', () => this.finishSubServiceSelection());
        optionsDiv.appendChild(doneOption);
        
        this.messagesContainer.appendChild(optionsDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
    
    selectSubService(subService) {
        if (!this.userSelections.subServices.includes(subService)) {
            this.userSelections.subServices.push(subService);
            this.addMessage('user', subService);
        }
    }
    
    finishSubServiceSelection() {
        // Remove options
        const optionsDiv = this.messagesContainer.querySelector('.chatbot-options');
        if (optionsDiv) {
            optionsDiv.remove();
        }
        
        this.addMessage('bot', 'Please describe your requirements or questions in detail:');
        this.currentStep = 'requirements';
    }
    
    sendMessage() {
        const message = this.input.value.trim();
        if (!message) return;
        
        this.addMessage('user', message);
        this.input.value = '';
        
        if (this.currentStep === 'requirements') {
            this.userSelections.requirements = message;
            this.endConversation();
        } else {
            // Handle unexpected input
            this.addMessage('bot', "I don't understand. Please choose from the available options or describe your requirements.");
        }
    }
    
    endConversation() {
        const contactInfo = `Thank you for reaching out! Please connect with our team through Get in Touch:

📞 Phone: +91 7030720478

📧 Email: info@websphereinnovations.com

📱 WhatsApp: +91 7030720478, +91 9168402327

🌐 Website: https://websphere-innovations.onrender.com/contact`;
        
        this.addMessage('bot', contactInfo);
        
        // Send transcript to admin via WhatsApp
        this.sendTranscriptToAdmin();
        
        // Reset after delay
        setTimeout(() => {
            this.reset();
        }, 5000);
    }
    
    sendTranscriptToAdmin() {
        const transcriptText = this.transcript.join('\n');
        
        fetch('/chatbot_submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `transcript=${encodeURIComponent(transcriptText)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                if (data.user_action_required && data.whatsapp_link) {
                    // Show success message with WhatsApp link
                    console.log('Transcript sent successfully');
                    showAlert(data.message, 'success');
                    
                    // Open WhatsApp link in new tab
                    setTimeout(() => {
                        window.open(data.whatsapp_link, '_blank');
                    }, 1000);
                } else {
                    console.log('Transcript sent successfully');
                    showAlert(data.message, 'success');
                }
            } else {
                console.error('Error sending transcript:', data.message);
                showAlert(data.message || 'Error sending transcript', 'error');
            }
        })
        .catch(error => {
            console.error('Error sending transcript:', error);
        });
    }
    
    reset() {
        this.currentStep = 'services';
        this.userSelections = {
            services: [],
            subServices: [],
            requirements: ''
        };
        this.transcript = [];
        
        // Clear messages except the first one
        while (this.messagesContainer.children.length > 1) {
            this.messagesContainer.removeChild(this.messagesContainer.lastChild);
        }
        
        // Show service options again
        this.showServiceOptions();
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const chatbot = new Chatbot();
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Form submissions
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner"></span> Sending...';
            
            fetch('/submit_contact', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (data.user_action_required && data.whatsapp_link) {
                        // Show success message with WhatsApp link
                        showAlert(data.message, 'success');
                        
                        // Open WhatsApp link in new tab
                        setTimeout(() => {
                            window.open(data.whatsapp_link, '_blank');
                        }, 1000);
                    } else {
                        showAlert(data.message, 'success');
                    }
                    this.reset();
                } else {
                    showAlert(data.message || 'Error sending message', 'error');
                }
            })
            .catch(error => {
                showAlert('Error sending message. Please try again.', 'error');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            });
        });
    }
    
    // Job application forms
    document.querySelectorAll('.job-application-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner"></span> Applying...';
            
            fetch('/apply_job', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert(data.message, 'success');
                    this.reset();
                } else {
                    showAlert(data.message || 'Error submitting application', 'error');
                }
            })
            .catch(error => {
                showAlert('Error submitting application. Please try again.', 'error');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            });
        });
    });
    
    // Add active navigation state
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});

// Utility functions
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 100px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.parentNode.removeChild(alertDiv);
        }
    }, 5000);
}

// Admin panel JavaScript
if (window.location.pathname.includes('/admin')) {
    document.addEventListener('DOMContentLoaded', function() {
        // Load data into admin forms
        loadAdminData();
        
        // Save data handlers
        document.querySelectorAll('.admin-save-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const section = this.dataset.section;
                saveAdminData(section);
            });
        });
        
        // Add job handler
        const addJobBtn = document.getElementById('addJobBtn');
        if (addJobBtn) {
            addJobBtn.addEventListener('click', addNewJob);
        }
        
        // Delete job handlers
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('delete-job-btn')) {
                const jobId = e.target.dataset.jobId;
                deleteJob(jobId);
            }
        });
    });
}

function loadAdminData() {
    // Load company info
    fetch('/api/company_info')
    .then(response => response.json())
    .then(data => {
        Object.keys(data).forEach(key => {
            const input = document.getElementById(`company_${key}`);
            if (input) {
                input.value = data[key];
            }
        });
    });
    
    // Load services
    fetch('/api/services')
    .then(response => response.json())
    .then(data => {
        Object.keys(data).forEach(key => {
            const titleInput = document.getElementById(`service_${key}_title`);
            const descInput = document.getElementById(`service_${key}_description`);
            
            if (titleInput) titleInput.value = data[key].title;
            if (descInput) descInput.value = data[key].description;
        });
    });
    
    // Load jobs
    fetch('/api/jobs')
    .then(response => response.json())
    .then(data => {
        const jobsContainer = document.getElementById('jobsContainer');
        if (jobsContainer) {
            jobsContainer.innerHTML = '';
            data.forEach(job => {
                addJobToContainer(job);
            });
        }
    });
    
    // Load recipients
    fetch('/api/recipients')
    .then(response => response.json())
    .then(data => {
        const recipientsInput = document.getElementById('whatsapp_recipients');
        if (recipientsInput) {
            recipientsInput.value = data.join(', ');
        }
    });
}

function saveAdminData(section) {
    let data = {};
    let endpoint = '';
    
    switch(section) {
        case 'company':
            data = {
                name: document.getElementById('company_name').value,
                tagline: document.getElementById('company_tagline').value,
                description: document.getElementById('company_description').value,
                phone: document.getElementById('company_phone').value,
                email: document.getElementById('company_email').value,
                whatsapp: document.getElementById('company_whatsapp').value,
                address: document.getElementById('company_address').value,
                copyright_year: document.getElementById('company_copyright_year').value
            };
            endpoint = '/api/company_info';
            break;
            
        case 'services':
            data = {
                cybersecurity: {
                    title: document.getElementById('service_cybersecurity_title').value,
                    description: document.getElementById('service_cybersecurity_description').value,
                    icon: 'shield'
                },
                software_development: {
                    title: document.getElementById('service_software_development_title').value,
                    description: document.getElementById('service_software_development_description').value,
                    icon: 'code'
                },
                data_analytics: {
                    title: document.getElementById('service_data_analytics_title').value,
                    description: document.getElementById('service_data_analytics_description').value,
                    icon: 'chart'
                },
                cloud_solutions: {
                    title: document.getElementById('service_cloud_solutions_title').value,
                    description: document.getElementById('service_cloud_solutions_description').value,
                    icon: 'cloud'
                }
            };
            endpoint = '/api/services';
            break;
            
        case 'recipients':
            const recipientsText = document.getElementById('whatsapp_recipients').value;
            data = recipientsText.split(',').map(r => r.trim());
            endpoint = '/api/recipients';
            break;
    }
    
    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Data saved successfully!', 'success');
        } else {
            showAlert('Error saving data', 'error');
        }
    })
    .catch(error => {
        showAlert('Error saving data', 'error');
    });
}

function addNewJob() {
    const title = document.getElementById('new_job_title').value;
    const experience = document.getElementById('new_job_experience').value;
    const description = document.getElementById('new_job_description').value;
    
    if (!title || !experience || !description) {
        showAlert('Please fill all job fields', 'error');
        return;
    }
    
    fetch('/api/jobs')
    .then(response => response.json())
    .then(jobs => {
        const newJob = {
            id: jobs.length > 0 ? Math.max(...jobs.map(j => j.id)) + 1 : 1,
            title: title,
            experience: experience,
            description: description,
            posted_date: new Date().toISOString().split('T')[0]
        };
        
        jobs.push(newJob);
        
        return fetch('/api/jobs', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jobs)
        });
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Job added successfully!', 'success');
            document.getElementById('new_job_title').value = '';
            document.getElementById('new_job_experience').value = '';
            document.getElementById('new_job_description').value = '';
            loadAdminData(); // Reload jobs
        } else {
            showAlert('Error adding job', 'error');
        }
    })
    .catch(error => {
        showAlert('Error adding job', 'error');
    });
}

function addJobToContainer(job) {
    const container = document.getElementById('jobsContainer');
    const jobDiv = document.createElement('div');
    jobDiv.className = 'job-item mb-3';
    jobDiv.innerHTML = `
        <div class="card">
            <div class="card-body">
                <div class="row">
                    <div class="col-md-8">
                        <h6>${job.title}</h6>
                        <p class="text-muted">${job.experience}</p>
                        <p>${job.description}</p>
                        <small class="text-muted">Posted: ${job.posted_date}</small>
                    </div>
                    <div class="col-md-4 text-end">
                        <button class="btn btn-sm btn-danger delete-job-btn" data-job-id="${job.id}">
                            <i class="fas fa-trash"></i> Delete
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
    container.appendChild(jobDiv);
}

function deleteJob(jobId) {
    if (!confirm('Are you sure you want to delete this job?')) return;
    
    fetch('/api/jobs')
    .then(response => response.json())
    .then(jobs => {
        const updatedJobs = jobs.filter(job => job.id !== parseInt(jobId));
        
        return fetch('/api/jobs', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedJobs)
        });
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Job deleted successfully!', 'success');
            loadAdminData(); // Reload jobs
        } else {
            showAlert('Error deleting job', 'error');
        }
    })
    .catch(error => {
        showAlert('Error deleting job', 'error');
    });
}

# 🚀 WebSphere Innovations - Deployment Guide

## 🌟 Free Hosting with Auto-Deployment

### 📋 Step-by-Step Deployment to Koyeb

#### 1️⃣ **Create Koyeb Account**
1. Visit: https://www.koyeb.com
2. Click "Sign up" 
3. Sign up with GitHub (recommended)
4. Verify your email

#### 2️⃣ **Deploy Your Application**
1. After login, click "Create Service"
2. Choose "GitHub" as source
3. Select your repository: `WebSphereInnovations/WebSphereInnovations`
4. Select branch: `master`
5. Configure deployment:
   - **Name**: `websphere-innovations`
   - **Instance Type**: `nano` (Free tier)
   - **Port**: `5000`
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `gunicorn --bind :$PORT app:app`
   - **Environment Variables**: `PORT=5000`

#### 3️⃣ **Enable Auto-Deployment**
1. In deployment settings, enable "Deploy on push"
2. This will automatically update your site when you push to GitHub

#### 4️⃣ **Access Your Website**
After deployment (2-3 minutes):
- **Main Website**: `https://websphere-innovations-xxxx.koyeb.app`
- **Admin Panel**: `https://websphere-innovations-xxxx.koyeb.app/admin`

### 🔄 **Automatic Updates**

Any time you push changes to GitHub:
```bash
git add .
git commit -m "Your changes"
git push origin master
```

Your website will automatically update within 2-3 minutes!

### 📱 **Features Available on Live Site**

✅ **WhatsApp Integration**: Both numbers working  
✅ **Team Management**: CEO, MD, Team members  
✅ **Admin Panel**: Full content management  
✅ **Contact Forms**: With WhatsApp notifications  
✅ **Jobs System**: With posting dates  
✅ **Responsive Design**: Works on all devices  
✅ **Dark Theme**: Professional design  

### 🎯 **Admin Access**

- **URL**: `https://websphere-innovations-xxxx.koyeb.app/admin`
- **Username**: `WebSphereInnovations`
- **Password**: `R@hul#1999`

### 📞 **WhatsApp Numbers**

Both numbers will receive messages:
- +91 7030720478
- +91 9168402327

### 🌐 **Free Tier Benefits**

- **Always Free**: No credit card required
- **Auto-Scaling**: Scale to zero when not in use
- **HTTPS**: Free SSL certificate
- **Global CDN**: Fast loading worldwide
- **Custom Domain**: Add your own domain later

### 🚀 **Alternative Free Hosting Options**

If Koyeb doesn't work, try:

#### **Render.com**
1. Visit: https://render.com
2. Connect GitHub
3. Select `WebSphereInnovations/WebSphereInnovations`
4. Web Service → Python → Free tier

#### **PythonAnywhere**
1. Visit: https://www.pythonanywhere.com
2. Create free account
3. Upload files manually
4. Configure web app

#### **Vercel**
1. Visit: https://vercel.com
2. Import GitHub repository
3. Auto-detect Python framework

### 🎉 **Your Website is Ready!**

Once deployed, you'll have:
- Professional business website
- WhatsApp messaging system
- Team management
- Admin panel
- Auto-deployment from GitHub

**🌟 Your complete business solution is live!**

---

*WebSphere Innovations - Transforming Businesses Through Technology Innovation*

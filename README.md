# Specc Studio Website

A modern, accessible, and performant website for Specc Studio - a web development agency focused on building simple, fast, and thoughtful sites.

## 🌟 Features

- **Modern Design**: Clean, gradient-based design with smooth animations
- **Fully Responsive**: Optimized for all screen sizes and devices
- **SEO Optimized**: Comprehensive meta tags, Open Graph, Twitter Cards, and structured data
- **Accessible**: WCAG compliant with skip links, ARIA labels, and keyboard navigation
- **Performance First**: Optimized CSS, minimal dependencies, smooth scrolling
- **Google OAuth**: Integrated authentication with django-allauth
- **Security Hardened**: Production-ready security settings

## 🚀 Tech Stack

- **Backend**: Django 6.0.2
- **Authentication**: django-allauth with Google OAuth
- **Database**: SQLite (dev), PostgreSQL ready (prod)
- **Frontend**: Vanilla HTML/CSS with modern CSS features
- **Font**: Space Grotesk from Google Fonts

## 📋 Prerequisites

- Python 3.12+
- pip
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/brar-karamjit/specc_app.git
   cd specc_app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django django-allauth python-dotenv
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser**
   
   Navigate to `http://localhost:8000`

## 📁 Project Structure

```
specc_app/
├── accounts/           # User authentication app
│   ├── templates/     # Login/signup templates
│   ├── views.py       # Authentication views
│   └── urls.py        # Auth URL patterns
├── core/              # Main website app
│   ├── static/        # Static files (CSS, images)
│   ├── templates/     # HTML templates
│   ├── views.py       # Page views
│   └── urls.py        # URL patterns
├── specc/             # Project settings
│   ├── settings.py    # Django settings
│   ├── urls.py        # Root URL config
│   └── wsgi.py        # WSGI config
├── manage.py          # Django management script
└── db.sqlite3         # Database (dev)
```

## 🎨 Key Pages

- **Home** (`/`) - Main landing page with services, work, testimonials, and contact
- **Login** (`/accounts/login/`) - Google OAuth authentication
- **Admin** (`/admin/`) - Django admin panel

## 🔒 Security Features

The website includes production-ready security settings:

- SSL redirect enforcement (production)
- Secure session and CSRF cookies
- HTTP Strict Transport Security (HSTS)
- X-Frame-Options protection
- Content type nosniff
- XSS filter
- Environment-based configuration

## 🚀 Deployment

### Environment Variables for Production

```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=specc.ca,www.specc.ca
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### Steps

1. Set `DEBUG=False` in production
2. Configure `ALLOWED_HOSTS` with your domain
3. Set up a production database (PostgreSQL recommended)
4. Configure static file serving (WhiteNoise or CDN)
5. Set up HTTPS/SSL certificates
6. Run `python manage.py collectstatic`
7. Run migrations: `python manage.py migrate`

## 🧪 Testing

```bash
python manage.py test
```

## 📝 License

Copyright © 2026 Specc Studio. All rights reserved.

## 🤝 Contributing

This is a private project. For inquiries, contact hello@specc.studio

## 📧 Contact

- **Email**: hello@specc.studio
- **Phone**: +1 (555) 123-4567
- **Website**: https://specc.ca

## 🎯 Recent Improvements

- ✅ Comprehensive SEO with meta tags and structured data
- ✅ Enhanced accessibility features
- ✅ New testimonials section
- ✅ Process workflow visualization
- ✅ Custom error pages (404, 500)
- ✅ Production-ready security settings
- ✅ Smooth animations and hover effects
- ✅ Mobile-responsive design

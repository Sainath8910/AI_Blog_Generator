# 🤖 AI Blog Generator

A full-stack web application that leverages artificial intelligence to generate, manage, and publish blog content. Built with Django backend and modern web technologies, this application provides a seamless platform for AI-powered content creation.

---

## ✨ Features

- **AI-Powered Blog Generation** - Automatically generate high-quality blog posts using Google's Generative AI models
- **Blog Management** - Create, edit, view, and manage blog posts with an intuitive interface
- **User Dashboard** - Personalized dashboard displaying user statistics and recent blog activity
- **Multiple Export Formats** - Export blog content in multiple formats (PDF, DOCX, etc.)
- **Responsive Design** - Mobile-friendly interface for seamless user experience across all devices
- **Content Customization** - Advanced settings for controlling blog generation parameters
- **User Profiles** - Personalized user profiles with bio and preferences
- **Settings Management** - Configure application settings and user preferences
- **AI Pipeline Architecture** - Modular AI pipeline for content generation, validation, and processing

---

## 🏗️ Project Structure

```
AI_Blog_Generator/
├── AI_Blog_Generator/          # Django project configuration
│   ├── settings.py             # Django settings and configuration
│   ├── urls.py                 # URL routing configuration
│   ├── wsgi.py                 # WSGI application entry point
│   └── asgi.py                 # ASGI application entry point
│
├── ai_pipeline/                # AI content generation pipeline
│   ├── config/                 # Configuration modules
│   ├── models/                 # ML models management
│   ├── pipeline/               # Main pipeline logic
│   ├── providers/              # AI provider integrations (Google Generative AI, etc.)
│   ├── schemas/                # Pydantic schemas for data validation
│   ├── prompts/                # AI prompt templates
│   ├── utils/                  # Utility functions
│   ├── validators/             # Content and data validators
│   └── requirements.txt         # AI pipeline dependencies
│
├── blogs/                      # Blog management application
│   ├── models.py               # Blog data models
│   ├── views.py                # Blog views and logic
│   ├── urls.py                 # Blog URL routes
│   └── migrations/             # Database migrations
│
├── core/                       # Core application modules
│   ├── models.py               # Core data models
│   ├── views.py                # Core views
│   ├── urls.py                 # Core URL routes
│   ├── supabase.py             # Supabase integration
│   ├── context_processors.py   # Django context processors
│   ├── admin.py                # Django admin configuration
│   └── migrations/             # Database migrations
│
├── dashboard/                  # User dashboard application
│   ├── models.py               # Dashboard models
│   ├── views.py                # Dashboard views
│   └── migrations/             # Database migrations
│
├── profile_app/                # User profile management
│   ├── models.py               # Profile models
│   ├── views.py                # Profile views
│   └── migrations/             # Database migrations
│
├── settings_app/               # Application settings
│   ├── models.py               # Settings models
│   ├── views.py                # Settings views
│   └── migrations/             # Database migrations
│
├── export_app/                 # Export functionality
│   ├── views.py                # Export views
│   ├── utils.py                # Export utilities (PDF, DOCX support)
│   └── migrations/             # Database migrations
│
├── static/                     # Static files
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   └── images/                 # Image assets
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── index.html              # Home page
│   ├── dashboard/              # Dashboard templates
│   ├── blogs/                  # Blog templates
│   ├── profile/                # Profile templates
│   ├── settings/               # Settings templates
│   └── export/                 # Export templates
│
├── manage.py                   # Django management script
├── requirements.txt            # Main project dependencies
└── build.sh                    # Production build script

```

---

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core backend development
- **Django 6.0.6** - Web framework for robust application structure
- **Google Generative AI** - AI-powered content generation
- **Supabase** - Backend-as-a-service for authentication and database
- **Celery** - Task queue for async operations
- **Redis** - In-memory data store and message broker
- **PostgreSQL** - Primary database (via psycopg2)
- **Gunicorn** - WSGI HTTP Server for production

### AI/ML Pipeline
- **Pydantic** - Data validation and schema management
- **JSON Schema** - Schema validation
- **Python-slugify** - URL slug generation
- **Markdown** - Content formatting
- **WeasyPrint** - PDF generation
- **python-docx** - Word document generation

### Frontend
- **HTML5** - Markup and structure
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive features and client-side logic
- **Responsive Design** - Mobile-first approach

### Development & Deployment
- **Whitenoise** - Static file serving in production
- **python-dotenv** - Environment variable management
- **Gunicorn** - Production WSGI server

---

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (strongly recommended)
- PostgreSQL database
- Redis server (for Celery task queue)
- Google Generative AI API Key
- Supabase account (optional, for authentication)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sainath8910/AI_Blog_Generator.git
cd AI_Blog_Generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root with the following variables:
```bash
# Django
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_blog_db

# AI Services
GOOGLE_API_KEY=your-google-generative-ai-key

# Supabase (Optional)
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key

# Redis
REDIS_URL=redis://localhost:6379/0
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Start Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

---

## 📦 Dependencies

### Core Dependencies
- **Django** - Web framework
- **google-genai** - Google Generative AI integration
- **supabase** - Backend services
- **celery** - Async task processing
- **redis** - Message broker and caching
- **psycopg2-binary** - PostgreSQL adapter
- **pydantic** - Data validation
- **gunicorn** - Production server
- **whitenoise** - Static file serving
- **python-dotenv** - Environment management

### Export & Content Processing
- **weasyprint** - PDF generation
- **python-docx** - Word document generation
- **Markdown** - Markdown processing
- **reportlab** - PDF library
- **pillow** - Image processing

For a complete list of all dependencies, refer to `requirements.txt` and `ai_pipeline/requirements.txt`

---

## 🎯 Usage Guide

### 1. **Sign Up / Log In**
   - Create a new account or log in to your existing account
   - Set up your user profile with bio and preferences

### 2. **Generate Blog Content**
   - Navigate to the Blog Generator
   - Provide topic, keywords, and tone preferences
   - AI will generate high-quality blog content
   - Review and refine the generated content

### 3. **Manage Blogs**
   - View all your published and drafted blogs
   - Edit existing blog posts
   - Update metadata (title, tags, categories)
   - Organize by sorting and filtering options

### 4. **Dashboard Overview**
   - Monitor your blog statistics
   - View recent activity
   - Track content performance

### 5. **Customize Your Profile**
   - Update personal information
   - Set content preferences
   - Manage notification settings

### 6. **Export Content**
   - Export individual blogs in multiple formats:
     - PDF with professional formatting
     - DOCX for further editing
     - HTML for web publication
   - Batch export multiple blogs

### 7. **Settings Management**
   - Configure AI generation parameters
   - Set content preferences
   - Manage API integrations
   - Control privacy settings

---

## 🏗️ Building for Production

### Using Build Script
```bash
bash build.sh
```

This script will:
1. Install all dependencies from requirements.txt
2. Collect static files
3. Run database migrations

### Manual Production Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Start with Gunicorn
gunicorn AI_Blog_Generator.wsgi:application --bind 0.0.0.0:8000
```

---

## 📁 Key Modules Reference

| Module | Purpose | Key Components |
|--------|---------|-----------------|
| `AI_Blog_Generator/` | Django project config | Settings, URLs, WSGI, ASGI |
| `ai_pipeline/` | AI content generation | Providers, validators, prompts, schemas |
| `blogs/` | Blog CRUD operations | Models, views, URL routes |
| `core/` | Core functionality | Settings, context processors, Supabase integration |
| `dashboard/` | User statistics | Blog overview, analytics |
| `profile_app/` | User management | Profile models, customization |
| `export_app/` | Content export | PDF/DOCX generation, formatting |
| `settings_app/` | Configuration | User settings, preferences |

---

## 🔌 API Pipeline Architecture

The `ai_pipeline` module provides a modular, extensible architecture for AI content generation:

### Configuration
- Environment and provider configuration management
- Model selection and parameters

### Providers
- Google Generative AI integration
- Extensible provider interface for multiple AI services

### Pipeline
- Content generation workflow orchestration
- Input processing and output handling
- Error handling and fallbacks

### Schemas & Validators
- Pydantic models for strict data validation
- Content quality validators
- Schema enforcement throughout the pipeline

### Prompts
- Reusable prompt templates
- Dynamic prompt generation based on user preferences

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines
- Tests are included for new features
- Documentation is updated

---

## 📄 License

This project is currently unlicensed. Please contact the repository owner for licensing information.

---

## 👤 Author

**Sainath8910** - [GitHub Profile](https://github.com/Sainath8910)

---

## 📞 Support & Issues

For support, issues, or questions:
- Open an issue on the [GitHub repository](https://github.com/Sainath8910/AI_Blog_Generator/issues)
- Check existing issues and discussions for similar problems
- Provide detailed information about your setup and the issue encountered

---

## 🔮 Future Enhancements

- [ ] Multi-language support for blog generation
- [ ] Advanced analytics and content performance insights
- [ ] Social media sharing integration
- [ ] Collaborative blog writing features
- [ ] SEO optimization tools and recommendations
- [ ] Email notification system for blog updates
- [ ] Content scheduling and auto-publishing
- [ ] Multiple AI provider support (OpenAI, Anthropic, etc.)
- [ ] Content plagiarism detection
- [ ] Advanced search and filtering capabilities
- [ ] Blog versioning and revision history
- [ ] Team collaboration features

---

## 🚀 Quick Links

- [Installation Guide](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Technology Stack](#-technology-stack)
- [Contributing Guidelines](#-contributing)
- [Issue Tracker](https://github.com/Sainath8910/AI_Blog_Generator/issues)

---

**Happy blogging with AI! 🚀**

*Last Updated: July 2026*

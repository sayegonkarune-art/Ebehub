# Ebehub - Professional E-Commerce Platform

A comprehensive, full-stack e-commerce platform built with Django, React, and PostgreSQL.

## 🚀 Features

### Phase 1 (Current)
- **Admin Dashboard**: Complete product, order, and customer management
- **Landing Page**: Professional homepage with product showcase
- **E-Commerce Core**: Product browsing, search, filtering, cart, checkout
- **User Authentication**: Sign up, login, password reset, email verification
- **Product Management**: Categories, filters, reviews, ratings
- **Order Management**: Order tracking, status updates
- **Payment Integration**: Stripe integration (ready for setup)

### Future Phases
- Multi-vendor marketplace
- Advanced inventory management
- Mobile app
- AI chatbot support
- Loyalty program
- Advanced analytics

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.x
- **API**: Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT + Django Auth
- **Payment**: Stripe API

### Frontend
- **Framework**: React 18.x
- **State Management**: Redux Toolkit
- **Styling**: Tailwind CSS + Bootstrap
- **HTTP Client**: Axios
- **Build Tool**: Vite

### DevOps
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- PostgreSQL
- Redis (caching)

## 📁 Project Structure

```
ebehub/
├── backend/                 # Django backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── config/             # Django settings
│   ├── apps/
│   │   ├── users/         # User authentication
│   │   ├── products/      # Product management
│   │   ├── orders/        # Order management
│   │   ├── payments/      # Payment processing
│   │   └── dashboard/     # Admin dashboard
│   └── utils/
├── frontend/                # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── redux/
│   │   ├── services/
│   │   └── styles/
│   ├── package.json
│   └── .env.example
├── docker-compose.yml
├── .gitignore
└── docs/
```

## 🚦 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- PostgreSQL 12+
- Docker (optional)

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Docker Setup
```bash
docker-compose up --build
```

## 📚 Documentation

- [Backend Setup Guide](docs/BACKEND_SETUP.md)
- [Frontend Setup Guide](docs/FRONTEND_SETUP.md)
- [API Documentation](docs/API.md)
- [Database Schema](docs/DATABASE.md)

## 🔐 Security

- SSL/TLS encryption
- CSRF protection
- XSS prevention
- Secure password hashing
- JWT authentication
- Rate limiting

## 📝 License

MIT License

---

**Built with ❤️ for modern e-commerce**

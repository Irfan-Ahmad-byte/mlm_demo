# 🔗 URL Shortener API (FastAPI + PostgreSQL + Docker)

A simple and efficient URL shortening service built with **FastAPI**, **PostgreSQL**, and **Docker**.

---

## 🚀 Features

- Shorten long URLs  
- Redirect using short codes  
- Auto-generates unique short codes  
- Dockerized with PostgreSQL  
- Ready for production deployment with Gunicorn  

---

## 🧱 Tech Stack

- 🐍 FastAPI  
- 🐘 PostgreSQL  
- 🐳 Docker & Docker Compose  
- 🔥 Gunicorn + Uvicorn  
- 🐍 SQLAlchemy + Alembic (optional migrations)  

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Create `.env` file 
Follow `.env.example` file to add Environment Variables.


### 3. Build and run with Docker
```bash
docker-compose up --build
```

API will be available at: http://localhost:8000


## 🔍 API Endpoints
### ➕ POST /shorten

Request:

```json
{
  "original_url": "https://example.com"
}
```

Response:

```json
{
  "id": 1,
  "original_url": "https://example.com",
  "short_code": "Ab3dE9",
  "created_at": "2025-04-06T12:00:00Z"
}
```

### 🔁 GET /{short_code}

Redirects to the original URL.

Example:
GET /Ab3dE9 → 302 Redirect to https://example.com

## 🧪 Testing
You can use:

- Postman
- cURL
- Or simple browser for redirection

## 📌 Future Improvements
- Expiry time for URLs
- Click count tracking
- Rate limiting
- Admin dashboard
- Rust version (🚧 coming soon)

## 👨‍💻 Author
Built with ❤️ by [Irfan Ahmad](!https://github.com/irfan-ahmad-byte)
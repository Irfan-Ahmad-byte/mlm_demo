# 💼 MLM Demo — Microservices + Flutter Frontend

**MLM Demo** is a complete multi-level marketing (MLM) system featuring a fully containerized FastAPI-based microservices backend and a Flutter-based mobile frontend — all in one repository. Designed to showcase modern backend architecture, frontend integration, and DevOps orchestration.

---

## 🔧 Architecture Overview

This project contains the following services:

- **[Authentication Service](https://github.com/irfan-ahmad-byte/jwt_authentication_service)** – Handles user registration, login, verification, and tokens
- **[MLM Service](https://github.com/irfan-ahmad-byte/mlm_service)** – Manages MLM trees, spillover logic, bonus distribution, rank evaluations
- **[URL Shortener Service](https://github.com/irfan-ahmad-byte/url_shortener)** – Lightweight service to generate and resolve short URLs
- **[Gateway API](https://github.com/irfan-ahmad-byte/mlm_api_gateway)** – Central entry point for frontend clients; routes to appropriate microservices
- **[Flutter Frontend App](https://github.com/irfan-ahmad-byte/mlm_demo_frontend_flutter)** – Cross-platform mobile app that connects via Gateway

Each microservice runs as an isolated FastAPI app on Docker with its own PostgreSQL database and optional Redis cache.

---

## 📁 Directory Layout

```
.
├── authentication/               # Authentication microservice
├── mlm_service/                # MLM tree and bonus microservice
├── url_shortener/      # URL shortening microservice
├── mlm_api_gateway/            # API gateway for frontend
├── mlm_demo_frontend_flutter/           # 📱 Flutter frontend app
│   ├── lib/
│   ├── android/
│   ├── ios/
│   └── pubspec.yaml
├── frontend/mlm_demo.apk  # Android build of the app (APK)
├── compose.yml     # Microservices orchestration
```

---

## 🐳 Running Backend Services

Ensure Docker & Docker Compose are installed, then run:

```bash
docker compose up --build
```

This will:
- Build and start all backend microservices
- Automatically manage database and redis health checks
- Launch the API Gateway **after** all other services are healthy

---

## 🌐 Service URLs

| Service         | URL                     | Description                        |
|-----------------|--------------------------|------------------------------------|
| Auth            | `http://localhost:8000`  | User registration/login etc.       |
| MLM             | `http://localhost:11000` | MLM tree, bonus logic, ranks       |
| URL Shortener   | `http://localhost:9000`  | Short link creation & redirection |
| Gateway         | `http://localhost:10000` | Unified API endpoint for frontend  |

---

## 📱 Flutter Frontend

The frontend is built with Flutter and located at:

```
/frontend
```

### 📦 APK Build

An Android APK (`mlm_demo.apk`) is already included in:

```
/frontend/mlm_demo.apk
```

You can install and test it directly using:

```bash
adb install frontend/mlm_demo.apk
```

Or open it on a physical/emulated Android device.

### 📲 Flutter Setup

To run the Flutter app locally:

```bash
cd frontend
flutter pub get
flutter run
```

Make sure `flutter doctor` is ✅ and your device/emulator is running.

---

## ✅ Backend Features (MLM)

- 🌳 Forced matrix tree with spillover logic
- 💸 Multi-level bonus distribution engine
- 🎖 Dynamic rank calculation (Bronze → Diamond)
- 📅 Weekly earnings reports
- ⚡ Redis caching for fast downline traversal
- 🚥 Microservice health checks and startup order
- 🛡️ JWT-compatible user auth via Auth service

---

## 🧪 Tech Stack

- **Backend**: FastAPI (Python 3.11), PostgreSQL, Redis
- **Frontend**: Flutter 3.x (Dart)
- **Orchestration**: Docker Compose
- **Communication**: REST via API Gateway

---

## 📜 License

Built by **[Irfan Ahmad](https://github.com/irfan-ahmad-byte)** as a demo project for full-stack microservices + mobile app integration.

For questions, collaboration, or improvements — feel free to reach out!


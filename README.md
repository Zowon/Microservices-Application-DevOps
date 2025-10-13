# 📚 Bookstore Microservices Application

A complete microservices-based application demonstrating containerization, orchestration, and DevOps best practices using Docker and Docker Compose.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

---

## 📋 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Services](#services)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project is a **microservices-based bookstore application** built to demonstrate:
- **Containerization** using Docker
- **Service orchestration** with Docker Compose
- **Microservices architecture** principles
- **RESTful API** design
- **Database integration** with MySQL
- **DevOps best practices**

The application consists of **10 services** (9 microservices + 1 database) that work together to provide a complete bookstore platform.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Frontend Service (8080)                 │
│              User Interface & Service Dashboard          │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼────────┐  ┌──────▼──────┐  ┌───────▼────────┐
│  Auth Service  │  │ User Service │  │  Book Service  │
│   (Port 5001)  │  │  (Port 5002) │  │  (Port 5003)   │
└────────────────┘  └──────────────┘  └────────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼──────┐
                    │  MySQL DB   │
                    │ (Port 3306) │
                    └─────────────┘
```

---

## 🧩 Services

| Service | Port | Description |
|---------|------|-------------|
| **Frontend** | 8080 | Web interface with links to all services |
| **Auth** | 5001 | Authentication and authorization |
| **User** | 5002 | User management and profiles |
| **Book** | 5003 | Book catalog and inventory |
| **Review** | 5004 | Book reviews and ratings |
| **Cart** | 5005 | Shopping cart management |
| **Order** | 5006 | Order processing and tracking |
| **Payment** | 5007 | Payment processing |
| **Notification** | 5008 | Email and notification service |
| **MySQL** | 3306 | Database for persistent storage |

---

## ✅ Prerequisites

Before running this application, ensure you have the following installed:

- **Docker** (version 20.10 or higher)
- **Docker Compose** (version 2.0 or higher)
- **Git** (for cloning the repository)

### Installation Links:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Zowon/Microservices-Application-DevOps.git
cd Microservices-Application-DevOps/bookstore-app
```

### 2. Build and Start All Services
```bash
docker compose up --build
```

Or run in detached mode:
```bash
docker compose up --build -d
```

### 3. Verify All Containers are Running
```bash
docker ps
```

You should see 10 containers running.

---

## 💻 Usage

### Access the Application

#### Frontend Dashboard
Open your browser and navigate to:
```
http://localhost:8080
```

The frontend displays links to all microservices for easy testing.

#### Individual Services
- **Auth Service**: http://localhost:5001
- **User Service**: http://localhost:5002
- **Book Service**: http://localhost:5003
- **Review Service**: http://localhost:5004
- **Cart Service**: http://localhost:5005
- **Order Service**: http://localhost:5006
- **Payment Service**: http://localhost:5007
- **Notification Service**: http://localhost:5008

### Stop the Application
```bash
docker compose down
```

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f auth-service
```

### Rebuild After Changes
```bash
docker compose up --build
```

---

## 📡 API Endpoints

Each microservice exposes a simple REST API:

### Example Response
```bash
curl http://localhost:5001
```

**Response:**
```json
{
  "service": "auth-service",
  "message": "auth-service is running"
}
```

All services follow the same response format for the root endpoint (`/`).

---

## 📁 Project Structure

```
bookstore-app/
│
├── docker-compose.yml              # Orchestration configuration
├── README.md                       # Project documentation
├── DEPLOYMENT_STATUS.md            # Deployment guide
│
├── auth-service/
│   ├── app.py                      # Flask application
│   ├── requirements.txt            # Python dependencies
│   └── Dockerfile                  # Container configuration
│
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── book-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── review-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── cart-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── order-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── payment-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── notification-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── frontend-service/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

---

## 🛠️ Technologies Used

- **Backend Framework**: Flask (Python)
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Database**: MySQL 5.7
- **Language**: Python 3.10
- **Architecture**: Microservices

---

## 🧪 Testing

### Manual Testing
```bash
# Test frontend
curl http://localhost:8080

# Test all services
for port in {5001..5008}; do
  echo "Testing port $port:"
  curl http://localhost:$port
  echo -e "\n"
done
```

### Health Check
```bash
docker compose ps
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Zowon**
- GitHub: [@Zowon](https://github.com/Zowon)

---

## 📞 Support

If you encounter any issues or have questions:
- Open an [Issue](https://github.com/Zowon/Microservices-Application-DevOps/issues)
- Contact via GitHub

---

## 🙏 Acknowledgments

- Built as part of DevOps Assignment 1
- Demonstrates microservices architecture patterns
- Uses industry-standard containerization practices

---

**⭐ If you find this project helpful, please give it a star!**
import os

def create_microservice(service_name, port):
    # Create service directory
    os.makedirs(service_name, exist_ok=True)
    
    # Create app.py
    app_py = f"""from flask import Flask, jsonify
import os

app = Flask(__name__)
SERVICE_NAME = os.getenv("SERVICE_NAME", "{service_name}")

@app.route("/")
def index():
    return jsonify({{
        "service": SERVICE_NAME,
        "message": f"{{SERVICE_NAME}} is running"
    }})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)"""
    
    with open(f"{service_name}/app.py", 'w') as f:
        f.write(app_py)
    
    # Create requirements.txt
    with open(f"{service_name}/requirements.txt", 'w') as f:
        f.write("flask")
    
    # Create Dockerfile
    dockerfile = """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]"""
    
    with open(f"{service_name}/Dockerfile", 'w') as f:
        f.write(dockerfile)

def create_frontend():
    service_name = "frontend-service"
    os.makedirs(service_name, exist_ok=True)
    
    # Create app.py for frontend
    frontend_py = """from flask import Flask, render_template_string

app = Flask(__name__)
services = [
  ("Auth", "http://localhost:5001/"),
  ("User", "http://localhost:5002/"),
  ("Book", "http://localhost:5003/"),
  ("Review", "http://localhost:5004/"),
  ("Cart", "http://localhost:5005/"),
  ("Order", "http://localhost:5006/"),
  ("Payment", "http://localhost:5007/"),
  ("Notification", "http://localhost:5008/")
]

TEMPLATE = '''<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Bookstore Frontend</title>
  </head>
  <body>
    <h1>Bookstore Frontend</h1>
    <p>Click on any service to test it:</p>
    <ul>
    {% for name, url in services %}
      <li><a href="{{ url }}" target="_blank">{{ name }}</a></li>
    {% endfor %}
    </ul>
  </body>
</html>'''

@app.route("/")
def index():
    return render_template_string(TEMPLATE, services=services)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)"""
    
    with open(f"{service_name}/app.py", 'w') as f:
        f.write(frontend_py)
    
    # Create requirements.txt for frontend
    with open(f"{service_name}/requirements.txt", 'w') as f:
        f.write("flask")
    
    # Create Dockerfile for frontend
    dockerfile = """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]"""
    
    with open(f"{service_name}/Dockerfile", 'w') as f:
        f.write(dockerfile)

# Create all microservices
services = [
    ("auth-service", 5001),
    ("user-service", 5002),
    ("book-service", 5003),
    ("review-service", 5004),
    ("cart-service", 5005),
    ("order-service", 5006),
    ("payment-service", 5007),
    ("notification-service", 5008)
]

for service, port in services:
    create_microservice(service, port)

# Create frontend service
create_frontend()

# Create README.md
readme = """# Bookstore Microservices Application (DevOps Assignment 1)

### Run Instructions
1. Install Docker and Docker Compose.
2. In terminal, navigate to the project root:
   ```bash
   docker compose up --build
   ```
3. Open the following URLs:
   - Frontend: http://localhost:8080
   - Auth: http://localhost:5001
   - User: http://localhost:5002
   - Book: http://localhost:5003
   - Review: http://localhost:5004
   - Cart: http://localhost:5005
   - Order: http://localhost:5006
   - Payment: http://localhost:5007
   - Notification: http://localhost:5008
4. Stop containers:
   ```bash
   docker compose down
   """

with open("README.md", 'w') as f:
    f.write(readme)

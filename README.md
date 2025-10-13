# Bookstore Microservices Application (DevOps Assignment 1)

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
   
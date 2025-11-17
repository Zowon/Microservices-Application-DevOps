# Screenshots Directory

This directory contains screenshots for the Assignment-2 submission.

## Required Screenshots

Please add the following screenshots after deploying the application:

### 1. Kubernetes Cluster Status
- **File**: `cluster-status.png`
- **Content**: `kubectl get pods -n microservices-app` showing all pods running
- **Command**: `kubectl get pods -n microservices-app`

### 2. Services Status
- **File**: `services-status.png`
- **Content**: `kubectl get services -n microservices-app` showing all services
- **Command**: `kubectl get services -n microservices-app`

### 3. Ingress Configuration
- **File**: `ingress-status.png`
- **Content**: `kubectl get ingress -n microservices-app` showing ingress rules
- **Command**: `kubectl get ingress -n microservices-app`

### 4. Application Frontend
- **File**: `frontend-app.png`
- **Content**: Browser view of the frontend application
- **URL**: `http://<minikube-ip>/frontend`

### 5. Individual Service Example
- **File**: `service-example.png`
- **Content**: Browser view of any microservice (e.g., auth service)
- **URL**: `http://<minikube-ip>/auth`

### 6. Database Verification
- **File**: `database-verification.png`
- **Content**: Terminal showing successful database connection
- **Command**: `kubectl exec -it deployment/mysql-deployment -n microservices-app -- mysql -u root -proot -e "SHOW DATABASES;"`

## How to Take Screenshots

### Linux Terminal Screenshots
```bash
# Install scrot if not available
sudo apt install scrot

# Take screenshot after running command
kubectl get pods -n microservices-app
scrot -s cluster-status.png
```

### Browser Screenshots
1. Open the application URL in browser
2. Use built-in screenshot tools or browser extensions
3. Save as PNG in this directory

## File Naming Convention

- Use descriptive names: `cluster-status.png`, `frontend-app.png`
- Use PNG format for better quality
- Ensure screenshots are clear and readable

## Verification

After adding screenshots, ensure:
- All screenshots are clear and readable
- Command outputs show successful deployment
- Browser screenshots show the actual application
- File names match the requirements above

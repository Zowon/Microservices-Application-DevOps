# Microservices Bookstore Application - Kubernetes Deployment

## 🚀 Kubernetes Deployment Guide

This guide provides complete instructions for deploying the microservices bookstore application to a Kubernetes cluster.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Kubernetes Commands Guide](#kubernetes-commands-guide)
4. [Verification Steps](#verification-steps)
5. [Troubleshooting](#troubleshooting)
6. [Architecture Overview](#architecture-overview)

---

## 🔧 Prerequisites

Before deploying to Kubernetes, ensure you have:

- **Minikube** or **Kind** cluster installed
- **kubectl** configured and working
- **Docker** installed and running
- **Ingress controller** enabled

### Installation Commands

```bash
# Install Minikube (if not already installed)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Install kubectl (if not already installed)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

---

## ⚡ Quick Start

### 1. Start the Cluster

```bash
# Start Minikube
minikube start

# Enable ingress addon
minikube addons enable ingress

# Verify cluster is running
kubectl cluster-info
```

### 2. Deploy the Application

```bash
# Apply all Kubernetes manifests
kubectl apply -f k8s/

# Or apply step by step
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/mysql-deployment.yaml
kubectl apply -f k8s/mysql-service.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### 3. Build and Load Docker Images

```bash
# Build all service images
docker build -t auth-service:latest ./auth-service
docker build -t user-service:latest ./user-service
docker build -t book-service:latest ./book-service
docker build -t review-service:latest ./review-service
docker build -t cart-service:latest ./cart-service
docker build -t order-service:latest ./order-service
docker build -t payment-service:latest ./payment-service
docker build -t notification-service:latest ./notification-service
docker build -t frontend-service:latest ./frontend-service

# Load images into Minikube
minikube image load auth-service:latest
minikube image load user-service:latest
minikube image load book-service:latest
minikube image load review-service:latest
minikube image load cart-service:latest
minikube image load order-service:latest
minikube image load payment-service:latest
minikube image load notification-service:latest
minikube image load frontend-service:latest
```

### 4. Access the Application

```bash
# Get Minikube IP
minikube ip

# Access application in browser
http://<minikube-ip>/frontend
```

---

## 📚 Kubernetes Commands Guide

### Essential Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `kubectl get pods` | List all pods | `kubectl get pods -n microservices-app` |
| `kubectl get services` | List services | `kubectl get svc -n microservices-app` |
| `kubectl get deployments` | List deployments | `kubectl get deploy -n microservices-app` |
| `kubectl get ingress` | List ingress rules | `kubectl get ingress -n microservices-app` |
| `kubectl get pvc` | List persistent volumes | `kubectl get pvc -n microservices-app` |
| `kubectl get secrets` | List secrets | `kubectl get secrets -n microservices-app` |
| `kubectl get configmaps` | List configmaps | `kubectl get cm -n microservices-app` |

### Monitoring Commands

```bash
# Watch pod status in real-time
watch kubectl get pods -n microservices-app

# View logs for a specific service
kubectl logs -f deployment/auth-service -n microservices-app

# View logs for all services
kubectl logs -f --all-namespaces --selector=app

# Describe a pod for detailed information
kubectl describe pod <pod-name> -n microservices-app

# Describe a service
kubectl describe service auth-service -n microservices-app

# Check resource usage
kubectl top pods -n microservices-app
```

### Debugging Commands

```bash
# Execute a command in a pod
kubectl exec -it <pod-name> -n microservices-app -- bash

# Port forward to access service locally
kubectl port-forward svc/frontend-service 8080:8080 -n microservices-app

# Check events in namespace
kubectl get events -n microservices-app --sort-by='.lastTimestamp'

# Get service endpoints
kubectl get endpoints -n microservices-app
```

### Scaling Commands

```bash
# Scale a deployment
kubectl scale deployment auth-service --replicas=3 -n microservices-app

# Scale all services
for deployment in $(kubectl get deployments -n microservices-app -o name); do
    kubectl scale $deployment --replicas=3 -n microservices-app
done

# Auto-scale a deployment (requires metrics server)
kubectl autoscale deployment auth-service --min=2 --max=5 --cpu-percent=70 -n microservices-app
```

### Update and Rollback Commands

```bash
# Update deployment image
kubectl set image deployment/auth-service auth-service=auth-service:v2 -n microservices-app

# Check rollout status
kubectl rollout status deployment/auth-service -n microservices-app

# View rollout history
kubectl rollout history deployment/auth-service -n microservices-app

# Rollback to previous version
kubectl rollout undo deployment/auth-service -n microservices-app

# Restart a deployment
kubectl rollout restart deployment/auth-service -n microservices-app
```

### Cleanup Commands

```bash
# Delete all resources
kubectl delete -f k8s/

# Delete specific resources
kubectl delete deployment auth-service -n microservices-app
kubectl delete service auth-service -n microservices-app

# Delete namespace (removes all resources)
kubectl delete namespace microservices-app

# Force delete stuck pods
kubectl delete pod <pod-name> -n microservices-app --force --grace-period=0
```

---

## ✅ Verification Steps

### 1. Verify All Components are Running

```bash
# Check all pods
kubectl get pods -n microservices-app

# Expected output: All pods should be in "Running" state
# NAME                               READY   STATUS    RESTARTS   AGE
# auth-service-xxxxxxxxxx-yyyy       2/2     Running   0          2m
# user-service-xxxxxxxxxx-yyyy       2/2     Running   0          2m
# book-service-xxxxxxxxxx-yyyy       2/2     Running   0          2m
# review-service-xxxxxxxxxx-yyyy     2/2     Running   0          2m
# cart-service-xxxxxxxxxx-yyyy       2/2     Running   0          2m
# order-service-xxxxxxxxxx-yyyy      2/2     Running   0          2m
# payment-service-xxxxxxxxxx-yyyy    2/2     Running   0          2m
# notification-service-xxxxxxxxxx-yyyy 2/2     Running   0          2m
# frontend-service-xxxxxxxxxx-yyyy   2/2     Running   0          2m
# mysql-deployment-xxxxxxxxxx-yyyy   1/1     Running   0          3m
```

### 2. Verify Services

```bash
# Check all services
kubectl get services -n microservices-app

# Expected output: All services should have ClusterIP
# NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
# auth-service        ClusterIP   10.100.200.10   <none>        5001/TCP   2m
# user-service        ClusterIP   10.100.200.11   <none>        5002/TCP   2m
# book-service        ClusterIP   10.100.200.12   <none>        5003/TCP   2m
# review-service      ClusterIP   10.100.200.13   <none>        5004/TCP   2m
# cart-service        ClusterIP   10.100.200.14   <none>        5005/TCP   2m
# order-service       ClusterIP   10.100.200.15   <none>        5006/TCP   2m
# payment-service     ClusterIP   10.100.200.16   <none>        5007/TCP   2m
# notification-service ClusterIP  10.100.200.17   <none>        5008/TCP   2m
# frontend-service    ClusterIP   10.100.200.18   <none>        8080/TCP   2m
# mysql-service       ClusterIP   10.100.200.19   <none>        3306/TCP   3m
```

### 3. Verify Ingress

```bash
# Check ingress
kubectl get ingress -n microservices-app

# Expected output: Ingress should have an address
# NAME                    CLASS    HOSTS                ADDRESS   PORTS   AGE
# microservices-ingress   nginx    microservices.local   192.168.49.2   80      5m
```

### 4. Test Application Access

```bash
# Get Minikube IP
MINIKUBE_IP=$(minikube ip)

# Test frontend
curl http://$MINIKUBE_IP/frontend

# Test individual services
curl http://$MINIKUBE_IP/auth
curl http://$MINIKUBE_IP/users
curl http://$MINIKUBE_IP/books
curl http://$MINIKUBE_IP/reviews
curl http://$MINIKUBE_IP/cart
curl http://$MINIKUBE_IP/orders
curl http://$MINIKUBE_IP/payments
curl http://$MINIKUBE_IP/notifications
```

### 5. Verify Database Connectivity

```bash
# Test database connection
kubectl exec -it deployment/mysql-deployment -n microservices-app -- mysql -u root -proot -e "SHOW DATABASES;"

# Expected output: Should see "bookstore" database
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | bookstore          |
# | mysql              |
# | performance_schema |
# | sys                |
# +--------------------+
```

### 6. Check Persistent Storage

```bash
# Verify PVC is bound
kubectl get pvc -n microservices-app

# Expected output: PVC should be in "Bound" state
# NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
# mysql-pvc   Bound    pvc-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx   5Gi        RWO            standard       10m
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Pods Not Starting

**Problem**: Pods are stuck in `Pending` or `CrashLoopBackOff` state

**Solutions**:
```bash
# Check pod events
kubectl describe pod <pod-name> -n microservices-app

# Check if images exist
kubectl get pods -n microservices-app -o jsonpath='{.items[*].spec.containers[*].image}'

# Check node resources
kubectl describe nodes

# View pod logs
kubectl logs <pod-name> -n microservices-app
```

#### Services Not Accessible

**Problem**: Services are created but not reachable

**Solutions**:
```bash
# Check service endpoints
kubectl get endpoints -n microservices-app

# Verify pod labels match service selector
kubectl get pods -n microservices-app --show-labels
kubectl get service -n microservices-app --show-labels

# Test service connectivity
kubectl exec -it <pod-name> -n microservices-app -- curl http://service-name:port
```

#### Ingress Not Working

**Problem**: External traffic not reaching services

**Solutions**:
```bash
# Check ingress controller
kubectl get pods -n ingress-nginx

# Check ingress rules
kubectl describe ingress microservices-ingress -n microservices-app

# Check ingress controller logs
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller

# Test ingress directly
kubectl exec -it ingress-nginx-controller-xxxx -n ingress-nginx -- curl http://service-name:port
```

#### Database Connection Issues

**Problem**: Services cannot connect to MySQL

**Solutions**:
```bash
# Check MySQL pod status
kubectl get pods -n microservices-app -l app=mysql

# Check MySQL service
kubectl get service mysql-service -n microservices-app

# Test MySQL connection
kubectl exec -it deployment/mysql-deployment -n microservices-app -- mysql -u root -proot -e "SELECT 1;"

# Check PVC status
kubectl get pvc mysql-pvc -n microservices-app
```

#### Resource Issues

**Problem**: Pods failing due to insufficient resources

**Solutions**:
```bash
# Check node resource usage
kubectl top nodes

# Check pod resource usage
kubectl top pods -n microservices-app

# Describe node for detailed resource info
kubectl describe nodes
```

### Recovery Commands

```bash
# Restart all deployments
for deployment in $(kubectl get deployments -n microservices-app -o name); do
    kubectl rollout restart $deployment -n microservices-app
done

# Force delete stuck pods
kubectl delete pods --all -n microservices-app --force --grace-period=0

# Recreate all resources
kubectl delete namespace microservices-app
kubectl apply -f k8s/
```

---

## 🏗️ Architecture Overview

### Kubernetes Components

| Component | Purpose | Configuration |
|-----------|---------|---------------|
| **Namespace** | Resource isolation | `microservices-app` |
| **ConfigMap** | Non-sensitive config | Service names, DB host |
| **Secret** | Sensitive data | DB passwords, API keys |
| **PVC** | Persistent storage | 5Gi for MySQL |
| **Deployment** | Pod management | 2 replicas per service |
| **Service** | Network endpoints | ClusterIP type |
| **Ingress** | External access | NGINX controller |
| **MySQL** | Database | Stateful with PVC |

### Request Flow

```
User → Ingress Controller → Service → Pod → Container → Response
                     ↓
               MySQL Database (via PVC)
```

### High Availability Features

- **Multi-replica deployments** (2 replicas per service)
- **Load balancing** through Kubernetes Services
- **Persistent storage** for database
- **Health checks** and self-healing
- **Rolling updates** for zero-downtime deployments

---

## 📖 Additional Resources

### Documentation

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)

### Useful Tools

```bash
# Install kubectl plugins
kubectl krew install view-serviceaccount-kubeconfig
kubectl krew install get-all

# Install stern for better log viewing
curl -L https://github.com/wercker/stern/releases/download/1.21.0/stern_linux_amd64.tar.gz | tar xz
sudo mv stern /usr/local/bin/

# Use stern to watch logs
stern -n microservices-app.*
```

---

## 🎯 Next Steps

After successful deployment, consider:

1. **Monitoring**: Set up Prometheus and Grafana
2. **Logging**: Implement ELK stack or Loki
3. **Security**: Add network policies and RBAC
4. **CI/CD**: Create GitOps pipeline with ArgoCD
5. **Backup**: Implement database backup strategy

---

## 📞 Support

For issues with this Kubernetes deployment:

1. Check the troubleshooting section above
2. Review Kubernetes events: `kubectl get events -n microservices-app`
3. Check pod logs: `kubectl logs -f deployment/<service-name> -n microservices-app`
4. Open an issue on the GitHub repository

---

**🎉 Congratulations!** Your microservices application is now running on Kubernetes!

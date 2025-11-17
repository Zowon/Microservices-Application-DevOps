from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import os

def create_pdf_report():
    # Create PDF document
    doc = SimpleDocTemplate(
        "/home/maaz/semester7/Microservices-Application-DevOps/docs/report.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=10,
        textColor=colors.black
    )
    
    content = []
    
    # Title Page
    content.append(Paragraph("Microservices Bookstore Application", title_style))
    content.append(Paragraph("Kubernetes Deployment Guide", title_style))
    content.append(Paragraph("Assignment-2 Report", title_style))
    content.append(Spacer(1, 50))
    content.append(Paragraph("DevOps Microservices Application", heading_style))
    content.append(Paragraph("Kubernetes Orchestration & Deployment", heading_style))
    content.append(PageBreak())
    
    # Table of Contents
    content.append(Paragraph("Table of Contents", heading_style))
    toc_content = [
        "1. Application Overview",
        "2. Architecture Diagram",
        "3. Kubernetes Components",
        "4. YAML Files Explanation",
        "5. Deployment Steps",
        "6. Kubernetes Commands Guide",
        "7. Verification Steps"
    ]
    
    for item in toc_content:
        content.append(Paragraph(f"• {item}", styles['Normal']))
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Application Overview
    content.append(Paragraph("1. Application Overview", heading_style))
    
    app_overview = """
    <b>What the Application Does:</b><br/>
    This is a comprehensive microservices-based bookstore application consisting of 9 interconnected services:
    <br/><br/>
    • <b>Frontend Service</b> - User interface and web application<br/>
    • <b>Auth Service</b> - Authentication and authorization management<br/>
    • <b>User Service</b> - User profile and account management<br/>
    • <b>Book Service</b> - Book catalog and inventory management<br/>
    • <b>Review Service</b> - Book reviews and ratings system<br/>
    • <b>Cart Service</b> - Shopping cart functionality<br/>
    • <b>Order Service</b> - Order processing and management<br/>
    • <b>Payment Service</b> - Payment processing and transactions<br/>
    • <b>Notification Service</b> - Email and push notifications<br/>
    • <b>MySQL Database</b> - Centralized data storage for persistence
    """
    
    content.append(Paragraph(app_overview, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Request Flow
    flow_content = """
    <b>Request Flow Inside Kubernetes:</b><br/><br/>
    <b>External User Request:</b><br/>
    1. User sends HTTP request through browser<br/>
    2. Ingress Controller routes based on path/host rules<br/>
    3. Service Layer load balances to available pods<br/>
    4. Pod/Container processes the request<br/>
    5. Database access if needed (MySQL)<br/>
    6. Response returns through same path<br/><br/>
    
    <b>Internal Service Communication:</b><br/>
    1. Service discovery through DNS resolution<br/>
    2. Load balancing across healthy pods<br/>
    3. HTTP/REST API communication between services<br/>
    4. Direct connection to MySQL service for data
    """
    
    content.append(Paragraph(flow_content, styles['Normal']))
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Architecture Diagram
    content.append(Paragraph("2. Architecture Diagram", heading_style))
    
    # Add the architecture diagram if it exists
    diagram_path = "/home/maaz/semester7/Microservices-Application-DevOps/docs/architecture-diagram.png"
    if os.path.exists(diagram_path):
        img = Image(diagram_path, width=6*inch, height=4*inch)
        content.append(img)
    else:
        content.append(Paragraph("[Architecture Diagram Placeholder]", styles['Normal']))
    
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Kubernetes Components
    content.append(Paragraph("3. Kubernetes Components", heading_style))
    
    components_data = [
        ['Component', 'Purpose', 'Configuration'],
        ['Namespace', 'Resource isolation', 'microservices-app'],
        ['ConfigMap', 'Non-sensitive config', 'Service names, DB host'],
        ['Secret', 'Sensitive data', 'DB passwords, API keys'],
        ['PVC', 'Persistent storage', '5Gi for MySQL'],
        ['Deployment', 'Pod management', '2 replicas per service'],
        ['Service', 'Network endpoints', 'ClusterIP type'],
        ['Ingress', 'External access', 'NGINX controller'],
        ['MySQL', 'Database', 'Stateful with PVC']
    ]
    
    components_table = Table(components_data, hAlign='LEFT')
    components_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    
    content.append(components_table)
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # YAML Files Explanation
    content.append(Paragraph("4. YAML Files Explanation", heading_style))
    
    yaml_explanations = """
    <b>namespace.yaml:</b><br/>
    Creates logical separation for all application resources.<br/><br/>
    
    <b>configmap.yaml:</b><br/>
    Stores configuration data like service names and database host.<br/><br/>
    
    <b>secret.yaml:</b><br/>
    Securely stores sensitive information like database passwords.<br/><br/>
    
    <b>pvc.yaml:</b><br/>
    Provides persistent storage for MySQL database (5Gi).<br/><br/>
    
    <b>mysql-deployment.yaml:</b><br/>
    Deploys MySQL database with persistent volume mounting.<br/><br/>
    
    <b>mysql-service.yaml:</b><br/>
    Creates internal service endpoint for MySQL database.<br/><br/>
    
    <b>deployment.yaml:</b><br/>
    Deploys all 9 microservices with 2 replicas each.<br/><br/>
    
    <b>service.yaml:</b><br/>
    Creates ClusterIP services for all microservices.<br/><br/>
    
    <b>ingress.yaml:</b><br/>
    Configures external access routing to internal services.
    """
    
    content.append(Paragraph(yaml_explanations, styles['Normal']))
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Deployment Steps
    content.append(Paragraph("5. Deployment Steps", heading_style))
    
    deployment_steps = """
    <b>Prerequisites:</b><br/>
    • Minikube or Kind cluster installed<br/>
    • kubectl configured<br/>
    • Docker installed<br/>
    • Ingress controller enabled<br/><br/>
    
    <b>Step-by-Step Deployment:</b><br/><br/>
    
    1. <b>Start Minikube:</b><br/>
    <code>minikube start</code><br/><br/>
    
    2. <b>Enable Ingress:</b><br/>
    <code>minikube addons enable ingress</code><br/><br/>
    
    3. <b>Create Namespace:</b><br/>
    <code>kubectl apply -f k8s/namespace.yaml</code><br/><br/>
    
    4. <b>Apply Configuration:</b><br/>
    <code>kubectl apply -f k8s/configmap.yaml</code><br/>
    <code>kubectl apply -f k8s/secret.yaml</code><br/><br/>
    
    5. <b>Setup Storage:</b><br/>
    <code>kubectl apply -f k8s/pvc.yaml</code><br/><br/>
    
    6. <b>Deploy Database:</b><br/>
    <code>kubectl apply -f k8s/mysql-deployment.yaml</code><br/>
    <code>kubectl apply -f k8s/mysql-service.yaml</code><br/><br/>
    
    7. <b>Deploy Services:</b><br/>
    <code>kubectl apply -f k8s/deployment.yaml</code><br/>
    <code>kubectl apply -f k8s/service.yaml</code><br/><br/>
    
    8. <b>Configure Ingress:</b><br/>
    <code>kubectl apply -f k8s/ingress.yaml</code><br/><br/>
    
    9. <b>Build Docker Images:</b><br/>
    <code>docker build -t auth-service ./auth-service</code><br/>
    (Repeat for all services)<br/><br/>
    
    10. <b>Load Images to Minikube:</b><br/>
    <code>minikube image load auth-service:latest</code><br/>
    (Repeat for all services)
    """
    
    content.append(Paragraph(deployment_steps, styles['Normal']))
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Kubernetes Commands Guide
    content.append(Paragraph("6. Kubernetes Commands Guide", heading_style))
    
    commands_data = [
        ['Command', 'Purpose', 'Example'],
        ['kubectl get pods', 'List all pods', 'kubectl get pods -n microservices-app'],
        ['kubectl get services', 'List services', 'kubectl get svc -n microservices-app'],
        ['kubectl get deployments', 'List deployments', 'kubectl get deploy -n microservices-app'],
        ['kubectl logs', 'View pod logs', 'kubectl logs -f deployment/auth-service -n microservices-app'],
        ['kubectl describe', 'Resource details', 'kubectl describe pod <pod-name> -n microservices-app'],
        ['kubectl exec', 'Execute in pod', 'kubectl exec -it <pod-name> -n microservices-app -- bash'],
        ['kubectl port-forward', 'Port forwarding', 'kubectl port-forward svc/frontend-service 8080:8080 -n microservices-app'],
        ['kubectl scale', 'Scale replicas', 'kubectl scale deployment auth-service --replicas=3 -n microservices-app'],
        ['kubectl apply', 'Apply manifests', 'kubectl apply -f k8s/ -n microservices-app'],
        ['kubectl delete', 'Delete resources', 'kubectl delete -f k8s/ -n microservices-app']
    ]
    
    commands_table = Table(commands_data, hAlign='LEFT')
    commands_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    
    content.append(commands_table)
    content.append(Spacer(1, 20))
    content.append(PageBreak())
    
    # Verification Steps
    content.append(Paragraph("7. Verification Steps", heading_style))
    
    verification_steps = """
    <b>Pod Verification:</b><br/>
    <code>kubectl get pods -n microservices-app</code><br/>
    Expected: All pods in Running state<br/><br/>
    
    <b>Service Verification:</b><br/>
    <code>kubectl get services -n microservices-app</code><br/>
    Expected: All services with ClusterIP type<br/><br/>
    
    <b>Ingress Verification:</b><br/>
    <code>kubectl get ingress -n microservices-app</code><br/>
    Expected: Ingress with proper address<br/><br/>
    
    <b>Application Access:</b><br/>
    <code>minikube ip</code> - Get cluster IP<br/>
    Access via: http://<minikube-ip>/frontend<br/><br/>
    
    <b>Database Connectivity:</b><br/>
    <code>kubectl exec -it deployment/mysql-deployment -n microservices-app -- mysql -u root -p</code><br/>
    Expected: Successful database connection<br/><br/>
    
    <b>Service Communication:</b><br/>
    <code>kubectl exec -it deployment/auth-service -n microservices-app -- curl http://mysql-service:3306</code><br/>
    Expected: Services can communicate with database<br/><br/>
    
    <b>Logs Verification:</b><br/>
    <code>kubectl logs -f deployment/frontend-service -n microservices-app</code><br/>
    Expected: No error messages in logs
    """
    
    content.append(Paragraph(verification_steps, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Troubleshooting Section
    content.append(Paragraph("Troubleshooting", subheading_style))
    
    troubleshooting = """
    <b>Common Issues:</b><br/><br/>
    
    <b>Pods not starting:</b><br/>
    • Check image availability: <code>kubectl describe pod <pod-name></code><br/>
    • Verify resources: <code>kubectl get nodes</code><br/><br/>
    
    <b>Service not accessible:</b><br/>
    • Check service endpoints: <code>kubectl get endpoints</code><br/>
    • Verify pod labels: <code>kubectl get pods --show-labels</code><br/><br/>
    
    <b>Ingress not working:</b><br/>
    • Check ingress controller: <code>kubectl get pods -n ingress-nginx</code><br/>
    • Verify ingress rules: <code>kubectl describe ingress</code><br/><br/>
    
    <b>Database connection issues:</b><br/>
    • Check PVC status: <code>kubectl get pvc</code><br/>
    • Verify secrets: <code>kubectl get secrets</code>
    """
    
    content.append(Paragraph(troubleshooting, styles['Normal']))
    
    # Build PDF
    doc.build(content)
    print("PDF report generated successfully!")

if __name__ == "__main__":
    create_pdf_report()

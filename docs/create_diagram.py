from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_architecture_diagram():
    # Create a new image with white background
    width, height = 1200, 800
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()
    
    # Title
    draw.text((width//2 - 150, 20), "Microservices Kubernetes Architecture", fill='black', font=title_font)
    
    # User
    draw.rectangle([width//2 - 60, 60, width//2 + 60, 100], fill='lightblue', outline='black')
    draw.text((width//2 - 30, 75), "USER", fill='black', font=font)
    
    # Arrow from User to Ingress
    draw.line([width//2, 100, width//2, 140], fill='black', width=2)
    draw.polygon([width//2-5, 140, width//2+5, 140, width//2, 150], fill='black')
    
    # Ingress Controller
    draw.rectangle([width//2 - 80, 150, width//2 + 80, 190], fill='lightgreen', outline='black')
    draw.text((width//2 - 60, 165), "Ingress", fill='black', font=font)
    
    # Arrows from Ingress to Services
    draw.line([width//2, 190, width//2, 230], fill='black', width=2)
    draw.polygon([width//2-5, 230, width//2+5, 230, width//2, 240], fill='black')
    
    # Services Layer
    services = [
        ("Frontend", 150, 250),
        ("Auth", 350, 250),
        ("User", 550, 250),
        ("Book", 750, 250),
        ("Review", 950, 250),
        ("Cart", 150, 350),
        ("Order", 350, 350),
        ("Payment", 550, 350),
        ("Notification", 750, 350)
    ]
    
    for service, x, y in services:
        draw.rectangle([x, y, x+120, y+40], fill='lightyellow', outline='black')
        draw.text((x+30, y+12), service, fill='black', font=font)
        # Arrow to pods
        draw.line([x+60, y+40, x+60, y+70], fill='black', width=1)
        draw.polygon([x+57, y+70, x+63, y+70, x+60, y+77], fill='black')
        
        # Pods
        draw.rectangle([x+20, y+80, x+100, y+110], fill='lightcoral', outline='black')
        draw.text((x+40, y+90), "Pods (2x)", fill='black', font=font)
    
    # MySQL Database at bottom
    draw.rectangle([width//2 - 100, 500, width//2 + 100, 540], fill='lightgray', outline='black')
    draw.text((width//2 - 40, 515), "MySQL DB", fill='black', font=font)
    
    # PVC
    draw.rectangle([width//2 - 80, 560, width//2 + 80, 600], fill='orange', outline='black')
    draw.text((width//2 - 50, 575), "PVC (5Gi)", fill='black', font=font)
    
    # Connections from services to MySQL
    mysql_services = ["Auth", "User", "Book", "Order"]
    for service_name in mysql_services:
        for service, x, y in services:
            if service == service_name:
                draw.line([x+60, y+110, x+60, y+130], fill='blue', width=1)
                draw.line([x+60, y+130, width//2, y+130], fill='blue', width=1)
                draw.line([width//2, y+130, width//2, 500], fill='blue', width=1)
                break
    
    # Legend
    legend_items = [
        ("User", "lightblue"),
        ("Ingress", "lightgreen"),
        ("Services", "lightyellow"),
        ("Pods", "lightcoral"),
        ("Database", "lightgray"),
        ("Storage", "orange")
    ]
    
    legend_y = 650
    for i, (label, color) in enumerate(legend_items):
        x = 50 + (i * 150)
        draw.rectangle([x, legend_y, x+30, legend_y+20], fill=color, outline='black')
        draw.text((x+35, legend_y+2), label, fill='black', font=font)
    
    # Save the image
    img.save('/home/maaz/semester7/Microservices-Application-DevOps/docs/architecture-diagram.png')
    print("Architecture diagram created successfully!")

if __name__ == "__main__":
    create_architecture_diagram()

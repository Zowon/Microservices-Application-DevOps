from flask import Flask, render_template_string

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
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CloudOps Sentinel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            text-align: center;
            padding-top: 100px;
        }

        .container {
            background: white;
            width: 500px;
            margin: auto;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        h1 {
            color: #222;
        }

        .status {
            color: green;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>CloudOps Sentinel</h1>
        <p>Automated DevSecOps Deployment Platform</p>
        <p class="status">● Application is Running</p>
        <p>Version: 1.0</p>
        <p>Environment: Development</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloudops-sentinel",
        "version": "1.0"
    })


@app.route("/api/info")
def info():
    return jsonify({
        "application": "CloudOps Sentinel",
        "version": "1.1",
        "environment": "development",
        "status": "running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
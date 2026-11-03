
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Flask App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #eaf2f8;
                padding: 100px;
            }
            h1 {
                color: #0078d4;
            }
            p {
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Azure Flask App!</h1>
        <p>Python Flask application deployed successfully.</p>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return "This is a Python Flask application running on Azure."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

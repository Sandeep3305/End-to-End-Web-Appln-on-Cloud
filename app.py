import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Cloud DevOps Project</title>
      </head>
      <body>
        <h1>My cloud application is running!</h1>
        <p>This web app will be containerized with Docker and deployed to AWS EC2.</p>
      </body>
    </html>
    """


@app.get("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)

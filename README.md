# 📦 CI‑CD-App

![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Python](https://img.shields.io/badge/Python-3.12-green)

**CI/CD Pipeline Demo: Python Flask App → Docker → AWS EC2**

This repository demonstrates a full **CI/CD pipeline** for a simple Flask web application.  
Commits pushed to the `main` branch trigger automatic Docker builds and pushes via **GitHub Actions**.

---

## 🚀 Features

- Simple **Python Flask App**
- **Dockerized** for consistent deployment
- **CI/CD pipeline** using GitHub Actions
- Ready for deployment to **AWS EC2** or any Docker host
- Easy to extend with automated tests and infrastructure-as-code

---

## 📁 Repository Structure

| File / Folder | Description |
|---------------|-------------|
| `.github/workflows/ci-cd.yml` | GitHub Actions pipeline configuration |
| `Dockerfile` | Containerization instructions |
| `app.py` | Flask web application |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## 🧩 Flask Application

```python
from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<h1>Ajay Nikam | DevOps Engineer</h1>
<p>Portfolio App Demonstration</p>
<p>Built with Flask + Docker + GitHub Actions</p>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
```

---

## ⚙️ GitHub Actions CI/CD

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker Image
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/ci-cd-app .

      - name: Push Docker Image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/ci-cd-app
```

---

## 🚀 Deployment Instructions

```bash
# Pull image on server
docker pull <docker_user>/ci-cd-app

# Run container
docker run -p 80:5000 <docker_user>/ci-cd-app

# Open browser at http://<server-ip>
```

---

## 📈 Architecture Diagram

```text
[GitHub Repository]
        |
        v
 [GitHub Actions CI/CD]
        |
        v
    [Docker Hub]
        |
        v
      [EC2 Server]
        |
        v
      [Flask App]
```

---

## 🤝 Contributing

- Add automated tests (Pytest / Unittest)  
- Extend CI/CD (linting, security scanning)  
- Deploy to multiple cloud providers  
- Improve Flask app UI/UX  

---

## 📜 License

MIT License © Ajay Nikam

---

### ✅ List of all custom code markers

| Marker | Description |
|--------|-------------|
| ```python | Python code (`app.py`) |
| ```dockerfile | Dockerfile code |
| ```yaml | GitHub Actions workflow |
| ```bash | Deployment commands |
| ```text | ASCII architecture diagram |

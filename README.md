# Sandeep Yadav — Cloud & DevOps Portfolio

A multi-page personal portfolio built with Flask. It is containerized with Docker and built by a GitHub Actions workflow. AWS deployment is planned as a later project phase.

## Pages

Home · About · Experience · Projects · Skills · Education · Contact

## Technology

Python, Flask, HTML, CSS, Docker, Git, GitHub, and GitHub Actions.

## Run with Python

Install dependencies and start the app:

    pip install -r requirements.txt
    python app.py

Open `http://localhost:5000`.

## Run with Docker

    docker build -t portfolio .
    docker run --rm -p 5000:5000 portfolio

Open `http://localhost:5000`.

## Health endpoint

The `/health` endpoint returns a simple status response.

## Project status

The portfolio app and Docker image build are implemented. AWS EC2 deployment is planned; the app is not deployed to AWS yet.
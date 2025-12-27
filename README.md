# Github Gist App

## Overview
This project is a lightweight HTTP web server API built using Python. The application integrates with the public GitHub Gists API and provides guidance at the root endpoint (/) on how to retrieve publicly available gists for a specific GitHub user via the /<user> endpoint.

## Key Features

1. **HTTP API:**
   - Developed a simple and reliable HTTP API using the Flask framework.
   - Exposes endpoints to access public GitHub gists for a given user.

2. **Automated Testing:**
   - Implemented automated tests to verify API behavior and ensure reliability.
   - Tests use the sample GitHub user octocat for demonstration and validation.

3. **Dockerization:**
   - Containerized the application using Docker for consistent and portable deployment.
   - Includes a Dockerfile for building the application image.
   - The API runs inside a Docker container and listens on port 8080.

## Running the application Locally Using Python

### Prerequisites
Python 3.12 and pip installed on your machine.

### Instructions
1. **Clone Repository**
   - Run the command: **git clone git@github.com:EqualExperts-Assignments/equal-experts-eager-hospitable-invigorating-complement-f17f63678cbd.git**
2. **Navigate to gist-app folder**
   - Change directory: **cd gist-app**
3. **Create a virtual environment**
   - Run this command to create a virtual environment: **python3 -m venv venv**
   - Activate the virtual environment:
     - On macOS/Linux: **source venv/bin/activate**
     - On Windows: **venv\Scripts\activate**
4. **Install dependencies**
   - Run this command to install required packages: **pip install -r requirements.txt**
5. **Run tests**
   - Run this command to execute tests: **pytest -v**
6. **Run the application**
   - Start the Flask application: **python gist_app.py**

Once the application starts, you can access GitHub Gists API at http://localhost:8080

## Running the application Locally Using Docker

### Prerequisites
Docker and git installed on your machine.

### Instructions
1. **Clone Repository**
   - Run the command: **git clone git@github.com:EqualExperts-Assignments/equal-experts-eager-hospitable-invigorating-complement-f17f63678cbd.git**
2. **Navigate to gist-app folder**
   - Change directory: **cd gist-app**
3. **Build the Docker image**
   - Run this command to build the application image: **docker build -t <<image-name:tag>> .**
4. **Run the Docker Container**
   - Run this command to run the application: **docker run -p 8080:8080 --name gist-app <<image-name:tag>>**

Once container starts, you can access GitHub Gists API at http://localhost:8080

## API Endpoints
- `GET /`: Provides guidance on how to use the API.
- `GET /<user>`: Retrieves the list of publicly available gists for the specified GitHub user.
  `<user>`: Replace with the GitHub username whose gists you want to retrieve.
  Example: `/octocat` to get gists for the user "octocat".
  Response: A JSON array containing the user's public gists.

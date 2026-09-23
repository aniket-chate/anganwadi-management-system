# Anganwadi Management System

A Flask-based management application for organizing Anganwadi beneficiary information, reporting, and related administrative workflows.

## Overview

The system provides a structured web application for beneficiary management and reporting. It uses Flask for the application layer and MySQL for persistent data storage.

## Features

- Beneficiary registration and management
- Beneficiary search and update workflows
- Dashboard and home views
- Report generation
- Structured Flask blueprints
- MySQL database integration
- Environment-based configuration
- Error pages for common application failures
- Excel/report support through Python libraries

## Architecture

The application is organized into separate layers:

```text
Flask App
   │
   ├── Routes
   │   ├── Home
   │   ├── Beneficiary
   │   └── Reports
   │
   ├── Services
   │   ├── Beneficiary Service
   │   └── Report Service
   │
   ├── Models
   │   └── Beneficiary
   │
   └── Database
       └── MySQL
```

## Project Structure

```text
anganwadi-management-system/
├── app.py
├── config.py
├── .env.example
├── requirements.txt
├── database/
├── models/
├── routes/
├── services/
├── static/
└── templates/
```

## Tech Stack

- Python
- Flask 3
- MySQL
- mysql-connector-python
- Pandas
- python-dotenv
- OpenPyXL
- Gunicorn
- HTML/CSS/JavaScript

## Configuration

Create a local `.env` file using `.env.example` as the reference.

Typical configuration includes:

```env
SECRET_KEY=your_secret_key
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=AnganwadiDB
FLASK_DEBUG=False
```

Do not commit real credentials or secrets.

## Run Locally

```bash
git clone https://github.com/aniket-chate/anganwadi-management-system.git
cd anganwadi-management-system

python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the database and environment variables, then run:

```bash
python app.py
```

The application listens on port **5000** for local development.

## Deployment Safety

This README only documents the existing application. It does not modify routes, database logic, deployment configuration, or runtime behavior.

## Author

**Aniket Ganesh Chate**  
B.Tech — Computer Science & Engineering (Data Science)

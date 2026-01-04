# CMS Backend
Backend project for CMS website.

## Technologies
- Python
- Django
- PostgreSQL

## Prerequisite
- Python 3.10 or above

## Install
### Clone the project
```bash
git clone git@github.com:KrystalSoftwareBangladesh/CMS-Backend.git
```
Navigate to the project directory
```bash
cd CMS-Backend
```

### Install Dependency
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Environment Setup
```bash
cp .env.example CMS_Backend/env.py
```

And then update values based on your environment.

## Run Project
### Migration
```bash
python manage.py migrate
```

### Create Super Admin
```bash
python manage.py createsuperuser
```

### Run the Server
```bash
python manage.py runserver
```

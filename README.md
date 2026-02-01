
# Sticky Notes Application

A Django-based web application for creating and managing sticky notes.

##  Features

- Create, read, update, and delete sticky notes
- Beautiful, responsive UI with gradient background
- Clean and intuitive interface
- Mobile-friendly design

##  Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

##  Installation & Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run Development Server
```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and go to:
- **Main App:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/

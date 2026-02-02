
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

### 1. Clone the repository 
```bash
git clone https://github.com/reacoda/sticky_notes_app.git
cd sticky-notes-app
```

### 2. Create Virtual Environment
```bash
python -m venv myvenv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
myvenv\Scripts\activate
```

**Mac/Linux:**
```bash
source myvenv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Navigate to project directory 
```bash
cd sticky_notes
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

## Software Design

This project includes comprehensive UML diagrams:
- **Use Case Diagram:** Shows user interactions with the system
- **Sequence Diagram:** Illustrates the flow of operations
- **Class Diagram:** Details the system architecture

All diagrams are available in the `/diagrams` folder.  

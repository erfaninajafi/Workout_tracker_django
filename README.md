# IronTracker: Workout Scheduling & Tracking System

IronTracker is a robust, monolithic web application built on Django that allows multiple users to schedule, track, and analyze their custom workout routines. It features a clean, date-sorted dashboard and detailed progress tracking.

## Core Features

* **Secure Authentication:** Utilizes Django's custom user model with JWTs secured via HttpOnly cookies for safe, multi-user access.
* **Workout Management (CRUD):** Complete functionality for creating, editing, and deleting scheduled workout sessions, associated with a specific date and time.
* **Dynamic Tracking:** Implements Django Formsets for dynamic exercise entry and **AJAX/JavaScript** for checking off individual exercises without page reloads.
* **Progress Reporting:** Calculates and displays the overall completion percentage of finished workouts on the dashboard.
* **Relational Data Model:** Uses a four-table relationship (`User -> Workout -> WorkoutExercise <- Exercise`) to efficiently manage fitness data.
* **Database:** Configured to run using **MySQL** for robust, production-ready data persistence.

## Setup and Installation

These instructions assume you have **Python 3.10+** and a running **MySQL Server** instance.

### 1. Clone the Repository & Setup Environment

```bash
# Clone the repository
git clone [https://github.com/erfaninajafi/Workout_tracker_django.git](https://github.com/erfaninajafi/Workout_tracker_django.git)
cd Workout_tracker_django

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

You must update the database settings in core/settings.py to match your local MySQL credentials. Ensure the target database (e.g., workout_tracker_db) is already created on your server.

```bash
# workout_tracker/settings.py snippet
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'workout_tracker_db', 
        'USER': 'YOUR_MYSQL_USER', # <--- Update this
        'PASSWORD': 'YOUR_MYSQL_PASSWORD', # <--- Update this
        'HOST': 'localhost',
        'PORT': '3306',
        # ...
    }
}
```
### 4. Migrate and Seed Data

Run migrations to create the tables in MySQL, create an administrative user, and populate the list of basic exercises.

```bash
# Apply database migrations
python manage.py makemigrations 
python manage.py migrate

# Create an administrator user
python manage.py createsuperuser

# Populate the predefined Exercise list (requires seed.py)
python seed.py
```

### 5. Run the Application

```bash
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/. You will be automatically redirected to the login screen.

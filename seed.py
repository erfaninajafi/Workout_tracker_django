import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workout_tracker.settings')
django.setup()

from workouts.models import Exercise

def create_initial_exercises():
    exercises = [
        "Bench Press", "Squat", "Deadlift", "Overhead Press", 
        "Barbell Row", "Pull-up", "Bicep Curl", "Triceps Extension",
        "Leg Press", "Lateral Raise", "Plank", "Crunch"
    ]
    
    for name in exercises:
        Exercise.objects.update_or_create(name=name, defaults={'description': f'A foundational {name.split()[0]} exercise.'})

    print(f"--- Successfully seeded {Exercise.objects.count()} exercises. ---")

if __name__ == '__main__':
    create_initial_exercises()
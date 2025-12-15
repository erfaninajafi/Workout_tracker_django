from django.shortcuts import render
from django.db.models import Count, Q
from .models import Workout

def dashboard(request):
    # Fetch active/pending workouts for current user
    active_workouts = Workout.objects.filter(user=request.user).order_index('scheduled_date')
    
    # Logic for Report
    total_workouts = Workout.objects.filter(user=request.user).count()
    completed_workouts = Workout.objects.filter(user=request.user, is_completed=True).count()
    
    completion_rate = (completed_workouts / total_workouts * 100) if total_workouts > 0 else 0
    
    return render(request, 'workouts/dashboard.html', {
        'workouts': active_workouts,
        'completion_rate': completion_rate
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from datetime import date
from .models import Workout, WorkoutExercise
from .forms import WorkoutForm, WorkoutExerciseFormSet

@login_required
def root_redirect(request):
    from django.shortcuts import redirect
    return redirect('dashboard')

@login_required
def dashboard(request):

    active_workouts = Workout.objects.filter(
        user=request.user, 
        scheduled_date__gte=date.today()
    ).order_by('scheduled_date')
    
    total_workouts = Workout.objects.filter(user=request.user).count()
    completed_workouts = Workout.objects.filter(user=request.user, is_completed=True).count()
    
    completion_rate = round((completed_workouts / total_workouts * 100)) if total_workouts > 0 else 0
    
    return render(request, 'workouts/dashboard.html', {
        'workouts': active_workouts,
        'completion_rate': completion_rate
    })

@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        formset = WorkoutExerciseFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            
            instances = formset.save(commit=False)
            for instance in instances:
                instance.workout = workout
                instance.save()
            
            formset.save_m2m() 
            return redirect('dashboard')
    else:
        form = WorkoutForm()
        formset = WorkoutExerciseFormSet()
    
    return render(request, 'workouts/workout_form.html', {'form': form, 'formset': formset})

@login_required
def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        formset = WorkoutExerciseFormSet(request.POST, instance=workout)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('dashboard')
    else:
        form = WorkoutForm(instance=workout)
        formset = WorkoutExerciseFormSet(instance=workout)
        
    return render(request, 'workouts/workout_form.html', {'form': form, 'formset': formset, 'is_update': True, 'workout': workout})

@login_required
def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('dashboard')
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})

@login_required
@require_POST
def toggle_exercise_done(request, pk):
    try:
        we = WorkoutExercise.objects.get(
            pk=pk, 
            workout__user=request.user
        )
        
        we.is_done = not we.is_done
        we.save()

        parent_workout = we.workout
        all_done = not parent_workout.exercises.filter(is_done=False).exists()
        
        parent_workout.is_completed = all_done
        parent_workout.save()
        
        return JsonResponse({'status': 'success', 'is_done': we.is_done, 'workout_completed': all_done})
        
    except WorkoutExercise.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Exercise not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
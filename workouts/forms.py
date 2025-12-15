from django import forms
from django.forms.models import inlineformset_factory
from .models import Workout, WorkoutExercise, Exercise
from crispy_forms.helper import FormHelper

class WorkoutForm(forms.ModelForm):
    scheduled_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        input_formats=['%Y-%m-%dT%H:%M'],
        label='Schedule Date and Time'
    )
    class Meta:
        model = Workout
        fields = ['title', 'scheduled_date']

class WorkoutExerciseForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), label='Exercise')
    
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'user_remarks']
        widgets = {
            'user_remarks': forms.Textarea(attrs={'rows': 2})
        }

WorkoutExerciseFormSet = inlineformset_factory(
    Workout, 
    WorkoutExercise, 
    form=WorkoutExerciseForm, 
    extra=1, 
    can_delete=True
)
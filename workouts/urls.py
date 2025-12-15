from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.workout_create, name='workout_create'),
    path('<int:pk>/edit/', views.workout_update, name='workout_update'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),
    path('toggle-exercise/<int:pk>/', views.toggle_exercise_done, name='toggle_exercise_done'), 
]
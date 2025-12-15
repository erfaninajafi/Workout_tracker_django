from django.contrib import admin
from django.urls import path, include
from workouts import views as workout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', workout_views.root_redirect, name='home'), 
    
    path('dashboard/', workout_views.dashboard, name='dashboard'),
    
    path('accounts/', include('accounts.urls')),
    path('workouts/', include('workouts.urls')), 
]
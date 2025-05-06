from django.urls import path
from . import views
app_name = 'users'  # Define the app name for namespacing

urlpatterns = [
    path('register/', views.register_view, name='register'),  # URL for the users page
    path('login/', views.login_view, name='login'),  # URL for the login page
    path('logout/', views.logout_view, name='logout'), 
]
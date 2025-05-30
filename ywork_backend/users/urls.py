

from django.urls import path
from .views import google_auth_success, get_token_for_logged_in_user, get_user_profile

urlpatterns = [
    path('welcome/', google_auth_success),                 
    path('token/', get_token_for_logged_in_user),          
    path('me/', get_user_profile),                         
]

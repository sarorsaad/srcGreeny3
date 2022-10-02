from django.urls import path
# from .views import ProfileList
from .views import profile,signup,user_activate

app_name='accounts'
urlpatterns = [
    # Add this
    
    path("signup", signup, name="signup"), 
    path("profile", profile, name="profile"),
    path("<str:username>/activate", user_activate, name="user_activate"), 
]
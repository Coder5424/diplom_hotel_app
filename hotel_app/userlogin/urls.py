from django.urls import path
from .views import RegisterView, LoginView, UpdateView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('myprofile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]

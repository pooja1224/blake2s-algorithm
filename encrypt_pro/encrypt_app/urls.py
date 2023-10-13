from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Usersignup.as_view()),
    path('signin/',views.Login.as_view())
]
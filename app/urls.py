from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<str:room_name>/", chatroom, name='room'),

    path("auth/login/", login, name="login"),
    path("auth/signup/", signup, name="signup"), 
    path('auth/logout/', logout_view, name='logout'),
]

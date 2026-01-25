from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("profile/<str:username>/",views.profile_detail,name ="profile"),
    path("follow/<str:username>/", views.follow_user, name="follow"),
    path("following/",views.following_user, name = "following"),
]
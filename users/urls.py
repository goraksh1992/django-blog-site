from django.urls import path
from .views import user_registration, profile
from django.contrib.auth import views

urlpatterns = [

    path('', user_registration, name="user-registration"),
    path('login', views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout', views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),

    path('password-reset', views.PasswordResetView.as_view(
        template_name='users/password_reset.html'
    ), name="password_reset"),

    path('password-reset-done', views.PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"
    ), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path('password_reset_complete', views.PasswordResetCompleteView.as_view(
        template_name="users/password_reset_complete.html"
    ), name="password_reset_complete"),

    path('profile', profile, name="profile"),
]


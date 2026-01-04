from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('apply/', views.apply, name="apply"),
    path('scheme/', views.scheme, name="scheme"),
    path('help/', views.help_page, name="help"),
    path('contact/', views.contact, name="contact"),

    path("auth/", views.auth_page, name="auth_page"),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout"),




    path('reset_password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

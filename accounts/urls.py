from django.urls import path
from accounts.views import register, perfil, perfil_edit, salir
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', salir, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('profile/', perfil, name='perfil'),
    path('profile/edit/', perfil_edit, name='perfil_edit'),
    # path('logout/', salir, name='logout'),
]
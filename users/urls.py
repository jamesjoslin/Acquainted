from django.urls import path
from .views import UserEditView, UserRegisterView, PasswordsChangeView
from . import views
# urls are given for each view here
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password.html')),
    path('password_success', views.password_success, name='password-success')
]
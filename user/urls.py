from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.user_login_view.as_view(), name='login'),
    path('signup/', views.user_singup_view.as_view(), name='signup'),
]
# Em urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Definindo a URL do login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de logout
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create-post/', views.create_post, name='create_post'),
    path('signup/', views.signup, name='signup'),
]

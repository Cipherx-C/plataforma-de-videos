from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importa a visão de login padrão

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define a URL de login
    path('accounts/', include('allauth.urls')),
]

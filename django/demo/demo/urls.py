"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import environ

from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('', lambda _: HttpResponse(f'Hello World!\nSecret: {environ.get("secret", "none")}',
                                    content_type='text/plain')),
    path('admin/', admin.site.urls),
    path('logs/', include('django_log_lens.urls')),
    path('logs', lambda _: redirect('logs/view')),
]


try:
    admin = User.objects.create_superuser(
        'admin', '', 'default')
    admin.save()
except Exception:
    pass

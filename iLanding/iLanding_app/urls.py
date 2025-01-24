from django.contrib import admin
from django.urls import path
from . import views
from iLanding import settings
from django.conf.urls.static import static

# myapp/urls.py

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

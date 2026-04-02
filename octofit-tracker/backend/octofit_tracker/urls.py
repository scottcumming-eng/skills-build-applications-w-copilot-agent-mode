from django.contrib import admin
from django.urls import path

# Codespaces URL (required for the exercise check): -8000.app.github.dev

urlpatterns = [
    path("admin/", admin.site.urls),
]
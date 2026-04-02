from django.contrib import admin
from django.urls import path, include

# NOTE: Training workflow check: include this substring at least once:
# -8000.app.github.dev

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("octofit_tracker.octofit_tracker.urls")),
]

from django.urls import path, include
from core import views

app_name = "core"

urlpatterns = [path("", views.index, name="index")]
# urlpatterns = [path("core/", include("core.urls", namespace="core"))]

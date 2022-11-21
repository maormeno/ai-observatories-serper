from django.urls import path

from api.views import get_link

urlpatterns = [
    path("link", get_link),
]

from django.urls import path

from api.views import get_all_links, get_link, get_link_batch, label_link

urlpatterns = [
    path("link", get_link),
    path("links", get_all_links),
    path("links/<int:size>", get_link_batch),
    path("link/<int:id>", label_link),
]

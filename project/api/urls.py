from django.urls import path

from api.views import (
    get_all_links,
    get_link,
    get_link_batch,
    get_random_link,
    get_test_links,
)

urlpatterns = [
    path("link", get_random_link),
    path("links", get_all_links),
    path("links/test/<int:half>", get_test_links),
    path("links/<int:size>", get_link_batch),
    path("link/<int:id>", get_link),
]

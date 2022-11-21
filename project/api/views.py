from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models import Link
import random


@api_view(["GET"])
def get_link(request):
    items = list(Link.objects.filter(label=None))
    print(items)
    random_item = random.choice(items)
    return Response(
        {
            "id": random_item.pk,
            "source": random_item.link,
            "title": random_item.title,
            "country": random_item.country,
            "keyword1": random_item.keyword1,
            "keyword2": random_item.keyword2,
            "label": random_item.label,
        }
    )

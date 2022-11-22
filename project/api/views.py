import json
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models import Link
import random


@api_view(["GET"])
def get_link(request):
    items = list(Link.objects.filter(label__isnull=True))
    random_item = random.choice(items)
    return Response(
        {
            "id": random_item.pk,
            "source": random_item.url,
            "title": random_item.title,
            "country": random_item.country,
            "keyword1": random_item.keyword1,
            "keyword2": random_item.keyword2,
            "label": random_item.label,
            "created": random_item.created_at,
            "updated": random_item.updated_at,
        }
    )


@api_view(["GET"])
def get_link_batch(request, size):
    items = list(Link.objects.filter(label__isnull=True))
    random_items = random.sample(items, size)
    serialized_links = []
    for link in random_items:
        serialized_links.append(
            {
                "id": link.pk,
                "source": link.url,
                "title": link.title,
                "country": link.country,
                "keyword1": link.keyword1,
                "keyword2": link.keyword2,
                "label": link.label,
                "created": link.created_at,
                "updated": link.updated_at,
            }
        )
    return Response({"links": serialized_links})


@api_view(["GET"])
def get_all_links(request):
    links = Link.objects.filter(label__isnull=True)
    serialized_links = []
    for link in links:
        serialized_links.append(
            {
                "id": link.pk,
                "source": link.url,
                "title": link.title,
                "country": link.country,
                "keyword1": link.keyword1,
                "keyword2": link.keyword2,
                "label": link.label,
                "created": str(link.created_at),
                "updated": str(link.updated_at),
            }
        )
    return Response({"links": serialized_links})


@api_view(["PUT"])
def label_link(request, id):
    link = Link.objects.get(pk=id)
    body = request.data["label"]
    try:
        link.label = body
        link.save()
        return Response("Successfully labeled", status=200)
    except:
        return Response("Couldn't label", status=301)

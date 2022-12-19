import json
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.models import Link
import random


@api_view(["GET"])
def get_random_link(request):
    items = list(Link.objects.filter(label__isnull=True))
    random_item = random.choice(items)
    return Response(
        {
            "id": random_item.pk,
            "url": random_item.url,
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
                "url": link.url,
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
                "url": link.url,
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


@api_view(["GET"])
def get_test_links(request, half):
    # used_test_ids = [
    #     3319,
    #     3341,
    #     3436,
    #     2831,
    #     2933,
    #     2723,
    #     2778,
    #     3544,
    #     3526,
    #     3188,
    #     3332,
    #     3444,
    #     3460,
    #     3434,
    #     3429,
    #     2852,
    #     3190,
    #     3276,
    #     3348,
    #     3011,
    #     3347,
    #     3095,
    #     2699,
    #     3129,
    #     3231,
    #     3472,
    #     2882,
    #     2925,
    #     3382,
    #     2869,
    #     3325,
    #     3549,
    #     3428,
    #     2969,
    #     2691,
    #     2947,
    #     3531,
    #     2814,
    #     2828,
    #     2868,
    #     3263,
    #     3107,
    #     2712,
    #     3512,
    #     3392,
    #     3631,
    #     2886,
    #     3246,
    #     3191,
    #     2962,
    #     3200,
    #     3430,
    #     3661,
    #     3509,
    #     3260,
    #     2965,
    #     3170,
    #     2995,
    #     3662,
    #     3016,
    #     2892,
    #     2680,
    #     3193,
    #     2865,
    #     3349,
    #     3644,
    #     3643,
    #     2745,
    #     3057,
    #     3384,
    #     3304,
    #     3452,
    #     2733,
    #     2809,
    #     2755,
    #     2902,
    #     2859,
    #     3052,
    #     3262,
    #     3275,
    #     3589,
    #     3447,
    #     3366,
    #     3496,
    #     3449,
    #     3264,
    #     3352,
    #     2948,
    #     2867,
    #     3224,
    #     3521,
    #     2889,
    #     3010,
    #     3285,
    #     2720,
    #     2885,
    #     3246,
    #     2890,
    #     3551,
    #     3651,
    # ]
    test_ids = [2673, 3104, 3241, 2784, 3032, 3171, 3068, 3302, 3632, 3533, 2904, 2816, 3271, 3282, 2735, 3502, 3102, 2773, 3318, 3474, 3303, 3256, 2914, 3358, 3647, 3027, 3222, 2690, 2811, 2759, 3571, 3195, 3543, 3098, 2980, 2708, 2944, 3185, 3230, 2851, 2880, 2804, 3365, 3539, 3490, 2812, 3497, 2845, 2915, 3617, 3443, 3453, 3148, 2944, 3165, 3546, 2761, 3138, 3510, 3146, 2686, 3471, 3272, 3417, 2912, 3254, 3013, 2822, 3415, 3558, 3077, 2862, 3281, 3462, 2873, 3000, 3330, 3280, 3330, 2820, 3021, 3619, 3254, 3004, 3379, 3404, 2943, 2820, 3475, 3175, 3024, 2730, 2898, 3330, 3228, 3165, 3028, 3235, 3283, 2695]
    serialized_links = []
    if half == 1:
        test_ids = test_ids[:50]
    else:
        test_ids = test_ids[50:]
    for id in test_ids:
        link = Link.objects.get(pk=id)
        serialized_links.append(
            {
                "id": link.pk,
                "url": link.url,
                "title": link.title,
                "country": link.country,
                "keyword1": link.keyword1,
                "keyword2": link.keyword2,
                "label": link.label,
                "created": str(link.created_at),
                "updated": str(link.updated_at),
                "owner": link.owner,
            }
        )
    return Response({"links": serialized_links})


@api_view(["PUT", "GET"])
def get_link(request, id):
    if request.method == "GET":
        try:
            link = Link.objects.get(pk=id)
            return Response(
                {
                    "id": link.pk,
                    "url": link.url,
                    "title": link.title,
                    "country": link.country,
                    "keyword1": link.keyword1,
                    "keyword2": link.keyword2,
                    "label": link.label,
                    "created": link.created_at,
                    "updated": link.updated_at,
                }
            )
        except:
            print("ERROR")
            return Response(f"Link with id {id} not found", status=404)

    try:
        link = Link.objects.get(pk=id)
        label = request.data["label"]
        interesting = request.data["interesting"]
        if interesting == 1:
            link.interesting = interesting
        link.label = label
        link.save()
        return Response("Successfully labeled", status=200)
    except:
        return Response("Couldn't label", status=301)

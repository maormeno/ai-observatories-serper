import random

rng = []
used = [3319, 3341, 3436, 2831, 2933, 2723, 2778, 3544, 3526, 3188, 3332, 3444, 3460, 3434, 3429, 2852, 3190, 3276, 3348, 3011, 3347, 3095, 2699, 3129, 3231, 3472, 2882, 2925, 3382, 2869, 3325, 3549, 3428, 2969, 2691, 2947, 3531, 2814, 2828, 2868, 3263, 3107, 2712, 3512, 3392, 3631, 2886, 3246, 3191, 2962, 3200, 3430, 3661, 3509, 3260, 2965, 3170, 2995, 3662, 3016, 2892, 2680, 3193, 2865, 3349, 3644, 3643, 2745, 3057, 3384, 3304, 3452, 2733, 2809, 2755, 2902, 2859, 3052, 3262, 3275, 3589, 3447, 3366, 3496, 3449, 3264, 3352, 2948, 2867, 3224, 3521, 2889, 3010, 3285, 2720, 2885, 3246, 2890, 3551, 3651]

while len(rng) < 100:
    r = random.randint(2673, 3672)
    if r not in used:
        rng.append(r)

print(rng)
import json
import pandas as pd
from app.models import Link
import xlsxwriter


def xlsx_writer(file_info):
    used_ids = [
        # 1st batch
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
        # 2nd batch
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
        # 3rd batch
        # 2690,
        # 2773,
        # 2804,
        # 2811,
        # 2816,
        # 2851,
        # 3358,
        # 2880,
        # 2914,
        # 3032,
        # 3102,
        # 3222,
        # 3241,
        # 3282,
        # 3271,
        # 3474,
        # 3632,
        # 3533,
        # 3543,
        # 3647,
        # 2673,
        # 3104,
        # 3617,
        # 2915,
        # 2845,
        # 3497,
        # 2812,
        # 3490,
        # 3539,
        # 3365,
        # 3230,
        # 3185,
        # 2944,
        # 2708,
        # 2980,
        # 3098,
        # 3195,
        # 3571,
        # 2759,
        # 3027,
        # 3256,
        # 3303,
        # 3318,
        # 3502,
        # 2735,
        # 2904,
        # 3302,
        # 3068,
        # 3171,
        # 2784,
    ]
    test_ids = [
        3443,
        3453,
        3148,
        2944,
        3165,
        3546,
        2761,
        3138,
        3510,
        3146,
        2686,
        3471,
        3272,
        3417,
        2912,
        3254,
        3013,
        2822,
        3415,
        3558,
        3077,
        2862,
        3281,
        3462,
        2873,
        3000,
        3330,
        3280,
        3330,
        2820,
        3021,
        3619,
        3254,
        3004,
        3379,
        3404,
        2943,
        2820,
        3475,
        3175,
        3024,
        2730,
        2898,
        3330,
        3228,
        3165,
        3028,
        3235,
        3283,
        2695,
    ]
    links_df = pd.DataFrame(Link.objects.filter(pk__in=test_ids).values())

    links_df["created_at"] = links_df["created_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )
    links_df["updated_at"] = links_df["updated_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )

    writer = pd.ExcelWriter(
        f"resultados_busqueda_{file_info}.xlsx", engine="xlsxwriter"
    )
    links_df.style.apply(highlight_rows, axis=1).to_excel(writer, sheet_name="Sheet1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    border_fmt = workbook.add_format({"bottom": 1, "top": 1, "left": 1, "right": 1})
    worksheet.conditional_format(
        xlsxwriter.utility.xl_range(0, 0, len(links_df), len(links_df.columns)),
        {"type": "no_errors", "format": border_fmt},
    )
    writer.save()


def highlight_rows(row):

    val = row.loc["label"]
    if val == "yes":
        color = "#60D660"
    elif val == "no":
        color = "#D66460"
    elif val == "maybe":
        color = "#F0E666"
    elif val == "academic":
        color = "#ff781f"
    else:
        color = "#FFFFFF"
    return ["background-color: {}".format(color) for r in row]

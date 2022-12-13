import json
import pandas as pd
from app.models import Link
import xlsxwriter


def xlsx_writer():
    test_ids = [
        3319,
        3341,
        3436,
        2831,
        2933,
        2723,
        2778,
        3544,
        3526,
        3188,
        3332,
        3444,
        3460,
        3434,
        3429,
        2852,
        3190,
        3276,
        3348,
        3011,
        3347,
        3095,
        2699,
        3129,
        3231,
        3472,
        2882,
        2925,
        3382,
        2869,
        3325,
        3549,
        3428,
        2969,
        2691,
        2947,
        3531,
        2814,
        2828,
        2868,
        3263,
        3107,
        2712,
        3512,
        3392,
        3631,
        2886,
        3246,
        3191,
        2962,
        3200,
        3430,
        3661,
        3509,
        3260,
        2965,
        3170,
        2995,
        3662,
        3016,
        2892,
        2680,
        3193,
        2865,
        3349,
        3644,
        3643,
        2745,
        3057,
        3384,
        3304,
        3452,
        2733,
        2809,
        2755,
        2902,
        2859,
        3052,
        3262,
        3275,
        3589,
        3447,
        3366,
        3496,
        3449,
        3264,
        3352,
        2948,
        2867,
        3224,
        3521,
        2889,
        3010,
        3285,
        2720,
        2885,
        3246,
        2890,
        3551,
        3651,
    ]
    links_df = pd.DataFrame(Link.objects.filter(pk__in=test_ids).values())
    links_df["created_at"] = links_df["created_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )
    links_df["updated_at"] = links_df["updated_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )
    writer = pd.ExcelWriter("resultados_busqueda.xlsx", engine="xlsxwriter")
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

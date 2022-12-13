import json
import pandas as pd
from app.models import Link
import xlsxwriter


def xlsx_writer(file_info):
    test_ids = [2756, 3211, 2866, 3208, 2923, 3183, 3312, 2804, 2956, 3008, 3138, 2940, 3037, 2895, 2999, 3610, 3465, 3156, 3553, 2904, 3267, 3484, 2681, 3305, 2675, 3313, 3609, 3238, 3168, 3175, 3669, 2977, 3069, 2710, 2926, 2916, 3295, 3451, 3054, 3291, 3314, 2926, 3475, 3130, 3196, 3493, 3032, 3344, 2766, 3164, 3066, 3090, 3094, 2717, 3647, 3080, 3045, 2829, 2806, 3559, 2754, 2848, 3192, 3148, 2951, 2835, 3338, 2808, 3206, 2931, 2955, 2940, 3181, 3007, 2760, 3028, 2916, 3261, 2966, 2991, 2861, 3373, 2921, 3563, 3299, 2850, 2754, 3333, 3026, 3595, 3567, 3213, 2844, 3029, 2824, 3053, 3608, 3458, 3221, 3359]
    # links_df = pd.DataFrame(Link.objects.filter(pk__in=test_ids[:50]).values()) #1st half MATEO 2nd half JELVE
    # links_df = pd.DataFrame(Link.objects.filter(pk__in=test_ids[50:]).values()) #1st half JELVE 2nd half MATEO
    links_df = pd.DataFrame(Link.objects.filter(pk__in=test_ids).values()) #ALL 100
    links_df["created_at"] = links_df["created_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )
    links_df["updated_at"] = links_df["updated_at"].apply(
        lambda a: pd.to_datetime(a).date()
    )
    
    writer = pd.ExcelWriter(f"resultados_busqueda_{file_info}.xlsx", engine="xlsxwriter")
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

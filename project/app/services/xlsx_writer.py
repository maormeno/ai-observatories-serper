import json
import pandas as pd
from app.models import Link
import xlsxwriter


def xlsx_writer():
    links_df = pd.DataFrame(Link.objects.all().values())
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

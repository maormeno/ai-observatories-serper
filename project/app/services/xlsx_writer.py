import xlsxwriter
import json
from app.models import Link


def xlsx_writer():
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook("resultados_busqueda.xlsx")
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 18)
    worksheet.set_column("C:C", 23)
    # countries = ["Chile", "Argentina", "Uruguay"]
    countries = [
        "Chile",
        "Argentina",
        "Brasil",
        "Colombia",
        "Uruguay",
        "Mexico",
        "Bolivia",
        "Costa Rica",
        "Cuba",
        "Ecuador",
        "El Salvador",
        "Guatemala",
        "Haiti",
        "Honduras",
        "Nicaragua",
        "Panama",
        "Paraguay",
        "Peru",
        "Republica Dominicana",
        "Venezuela",
    ]
    worksheet.write(
        0,
        0,
        "Lo que hay que preguntarse: ¿es una coleccion de algoritmos para la toma de decisiones automatizadas?",
    )
    worksheet.write(
        0,
        3,
        "Tiempo demora",
    )
    worksheet.write(
        0,
        4,
        "Quien",
    )
    worksheet.write(
        0,
        5,
        "Fecha",
    )
    worksheet.write(
        0,
        6,
        "Link Resultado busqueda",
    )
    for i in range(7, 17):
        worksheet.write(0, i, f"Link{i - 6}")

    for country in countries:
        worksheet.write((countries.index(country)) * 6 + 1, 0, country)
        worksheet.write((countries.index(country)) * 6 + 1, 1, "Observatorio")
        worksheet.write(
            (countries.index(country)) * 6 + 1, 2, "Inteligencia Artificial"
        )
        worksheet.write((countries.index(country)) * 6 + 1 + 1, 2, "Algoritmos")
        worksheet.write(
            (countries.index(country)) * 6 + 2 + 1, 2, "Decisiones Automatizadas"
        )
        worksheet.write((countries.index(country)) * 6 + 3 + 1, 1, "Repositorio")
        worksheet.write(
            (countries.index(country)) * 6 + 3 + 1, 2, "Inteligencia Artificial"
        )
        worksheet.write((countries.index(country)) * 6 + 4 + 1, 2, "Algoritmos")
        worksheet.write(
            (countries.index(country)) * 6 + 5 + 1, 2, "Decisiones Automatizadas"
        )

    starting_row = 1
    for i in range(1, 121):
        with open(
            f"results/result{i}.json", "r", encoding="utf-8"
        ) as json_response_file:
            json_data = json.load(json_response_file)
            link_list = json_data["organic"]
            for link in link_list:
                worksheet.write(starting_row, link_list.index(link) + 7, link["link"])
            starting_row += 1

    workbook.close()

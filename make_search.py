from google_serp import *


def make_search():
    countries = {
        "Chile": "cl",
        "Argentina": "ar",
        "Brasil": "br",
        "Colombia": "co",
        "Uruguay": "uy",
        "Mexico": "mx",
        "Bolivia": "bo",
        "Costa Rica": "cr",
        "Cuba": "cu",
        "Ecuador": "ec",
        "El Salvador": "sv",
        "Guatemala": "gt",
        "Haiti": "ht",
        "Honduras": "hn",
        "Nicaragua": "ni",
        "Panama": "pa",
        "Paraguay": "py",
        "Peru": "pe",
        "Republica Dominicana": "do",
        "Venezuela": "ve",
    }
    keywords_1 = ["Observatorio", "Algoritmo"]
    keywords_2 = ["Inteligencia Artificial", "Algoritmos", "Decisiones Automatizadas"]

    i = 0
    for country, code in countries.items():
        for kw1 in keywords_1:
            for kw2 in keywords_2:
                i += 1
                query = f"{country} {kw1} {kw2}"
                result = google_serp_to_json(query, code)
                request_search_json_to_file(result, f"results/result{str(i)}.json")
                print(f"Query: {query} - Result: DONE")

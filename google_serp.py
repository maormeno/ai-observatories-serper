import http.client
import json


def google_serp_to_json(
    query, country_code, google_language="es-419", autocorrect=False
):
    conn = http.client.HTTPSConnection("google.serper.dev")

    payload = json.dumps(
        {
            "q": query,
            "gl": country_code,
            "hl": google_language,
            "autocorrect": autocorrect,
        }
    )
    headers = {
        "X-API-KEY": "49dedcce235972cc0c02f77b16d59e9bf2c5f678",
        "Content-Type": "application/json",
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def request_search_json_to_file(query_result, file_name="google_serp.json"):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(query_result, f, indent=2, ensure_ascii=False)

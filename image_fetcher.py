import os, requests

def get_image(query):
    key = os.environ["UNSPLASH_ACCESS_KEY"]
    url = "https://api.unsplash.com/search/photos"

    r = requests.get(url, params={
        "query": query,
        "per_page": 1
    }, headers={
        "Authorization": f"Client-ID {key}"
    })

    data = r.json()
    if data["results"]:
        return data["results"][0]["urls"]["regular"]
    return None

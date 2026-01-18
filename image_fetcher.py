import requests
import os
from dotenv import load_dotenv

load_dotenv()
UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_image(query, idx):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": 1
    }
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_KEY}"
    }

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    if data["results"]:
        img_url = data["results"][0]["urls"]["regular"]
        img_data = requests.get(img_url).content
        path = f"image_{idx}.jpg"
        with open(path, "wb") as f:
            f.write(img_data)
        return path

    return None
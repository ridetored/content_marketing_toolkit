import requests
import pandas as pd
import yaml

def fetch_keywords(topic):
    """Fetch keyword suggestions using Semrush API."""
    with open("config/settings.yaml", "r") as file:
        config = yaml.safe_load(file)

    api_key = config["semrush_api_key"]
    url = f"https://api.semrush.com/?type=phrase_related&key={api_key}&phrase={topic}&database=us"

    response = requests.get(url)
    if response.status_code == 200:
        keywords = response.json().get("data", [])
        df = pd.DataFrame(keywords)
        output_path = "data/keywords.csv"
        df.to_csv(output_path, index=False)
        print(f"Keyword research results saved to {output_path}")
    else:
        print("Failed to fetch keywords:", response.text)

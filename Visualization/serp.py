from serpapi import GoogleSearch
import os

def search(params):
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]
    for i in range(len(organic_results)):
        
        if "who" in organic_results[i]["link"]:
            # print(i)
            # print(organic_results[i]["displayed_link"])
            # print(organic_results[i]["snippet_highlighted_words"])
            ans=(organic_results[i]["link"],organic_results[i]["snippet_highlighted_words"])
            return ans
    return None

def stats_finder(disease):
    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    params = {
    "engine": "google",
    "q": f"no of people suffering from {disease} in the world",
    "api_key": COHERE_API_KEY
    }
    return search(params)


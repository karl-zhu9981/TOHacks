import json
from serpapi import GoogleSearch

params = {
  "api_key": "e61e09984c68bf6aa40bb477fb5bf5ebb5802ac55f9ce17ac7325575e7765257",
  "engine": "google",
  "q": "chocolate and rice crispy recipes",
  "location": "Austin, Texas, United States",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()

for key,value in results.items():
	final = results.get('recipes_results')


print (json.dumps(final, indent=1))
import requests

def get_random_wikipedia_fact():
    # Get a random article title
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        title = data["title"]
        summary = data["extract"]
        return f"{title}: {summary}"
    else:
        return "Couldn't fetch a random Wikipedia fact."

print(get_random_wikipedia_fact())

#evil guy was here!

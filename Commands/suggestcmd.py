import requests, keys

def function(comment):
    data = {
    "content" : comment,
    "username" : "Suggestion"
    }
    result = requests.post(keys.webhook, json = data)
import random, discord, requests, json

def function():
    n = random.choice([1, 2])
    if (n==1):
        subreddit = "memes"
    else:
        subreddit = "dankmemes"
    r = requests.get('https://meme-api.herokuapp.com/gimme/' + subreddit)
    data = json.loads(r.text)
    embedVar = discord.Embed(title=data['title'], url=data['postLink'] , color=0xFFFFFF)
    embedVar.set_image(url=data['url'])
    embedVar.set_footer(text="By u/"+data['author']+ " in r/" + data['subreddit'])
    return embedVar
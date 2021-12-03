import discord, json, requests

def function():
    r = requests.get('https://api.quotable.io/random')
    data = json.loads(r.text)
    quote = data['content']
    author = data['author']
    if(data['length']>255):
        embedVar = discord.Embed(description='\"'+quote+"\"\n\nAuthor: "+author, color=0xFFFFFF)
    else:
        embedVar = discord.Embed(title='"'+quote+'"', description="Author: "+author, color=0xFFFFFF)
    return embedVar
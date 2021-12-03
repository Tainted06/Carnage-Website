import requests, json, keys, discord

def function(word):
    r = requests.get('https://wordsapiv1.p.rapidapi.com/words/'+word+'/definitions', headers={
        'x-rapidapi-key': keys.defineapikey
    })
    data = json.loads(r.text)
    try:
        notfound = data["message"]
        embedVar = discord.Embed(title='No Definitions Found', description="Sorry, no definitions were found for " + word +'.', color=0xFFFFFF)
    except:
        embedVar = discord.Embed(title='Definition for ' + word, color=0xFFFFFF)
        n=0
        for i in data['definitions']:
            n = n+1
            embedVar.add_field(name='Definition #' + str(n) + ':',value=i['definition'], inline=False)
    return(embedVar)
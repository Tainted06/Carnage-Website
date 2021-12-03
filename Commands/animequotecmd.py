import json, random, discord

def function():
    s=open("animequotes.txt","r", encoding='utf-8')
    m=s.readlines()
    l=[]
    for i in range(0,len(m)-1):
        x=m[i]
        z=len(x)
        a=x[:z-1]
        l.append(a)
    l.append(m[i+1])
    a = json.loads(random.choice(l))
    return(discord.Embed(title='"'+a["quote"]+'"', description="Anime: "+a["anime"]+"\nCharacter: "+a["character"], color=0xFFFFFF))
import discord

def function(msg):
    if(msg == None):
        return(discord.Embed(title="Add a messsage for me to say!", color=0xFFFFFF))
    else:
        if(len(msg)>255):
            return(discord.Embed(description=msg, color=0xFFFFFF))
        else:
            return(discord.Embed(title=msg, color=0xFFFFFF))
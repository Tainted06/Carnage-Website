import discord

def function(ctx):
    dm = ctx.author.create_dm()
    embedVar = discord.Embed(title='Command List',description='List of all the commands for Carnage Bot', color=0xFFFFFF)
    embedVar.add_field(name='Fun',value='>animequote - **Sends a random quote from anime**\n>meme - **Gets a random meme from reddit**\n>eightball `question` - **Gives an 8ball response to a question**\n>quote - **Gives you a random quote**', inline=False)
    embedVar.add_field(name='Moderation',value='>ban `user` - **Bans the mentioned user**\n>kick `user` - **Kicks the mentioned user**', inline=False)
    embedVar.add_field(name='Utility',value='>echo `message` - **Echos a message**\n>commandlist - **Dms you all the commands**\n>define `word` - **Defines a word**\n>suggest `suggestion` - **Sends your suggestion to the devs**', inline=False)
    dm.send(embed = embedVar)
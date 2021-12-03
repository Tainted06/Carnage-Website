import random, discord

possibleoutputs = [
        "It is certain",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

def function(msg):
    random_index = random.randrange(len(possibleoutputs))
    if int(random_index)<10:
        embedcolor = 0x00ff00
    if int(random_index)<16 and int(random_index)>10:
        embedcolor = 0xffa500
    if int(random_index)>15:
        embedcolor = 0xff0000
    embedVar = discord.Embed(title='8-Ball Response',description=possibleoutputs[random_index], color=embedcolor)
    embedVar.add_field(name='Question:',value=msg, inline=False)
    return embedVar

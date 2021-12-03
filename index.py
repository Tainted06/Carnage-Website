import discord, time, random, json, requests, keys
from Commands import animequotecmd, commandlistcmd, definecmd, echocmd, eightballcmd, memecmd, quotecmd, suggestcmd
from discord.errors import ClientException
from discord.ext import commands

bot = commands.Bot(command_prefix='>', case_insensitive=True, help_command=None)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Your missing some parts of the command! Use the command >commandlist to see how to use a command!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Sorry, you are missing the permissions to do that!")

@bot.command()
async def animequote(ctx):
    await ctx.send(embed=animequotecmd.function())

@bot.command()
async def define(ctx, word):
    await ctx.send(embed=definecmd.function(word))    

@bot.command()
async def eightball(ctx, *, msg):
    await ctx.send(embed=eightballcmd.function(msg))

@bot.command()
async def quote(ctx):
    await ctx.send(embed=quotecmd.function())

@bot.command()
async def meme(ctx):
    await ctx.send(embed=memecmd.function())

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    try:
        await member.ban(reason = reason)
        await ctx.send(embed=discord.Embed(title=str(member) + " was banned!", description="Reason: " + str(reason), color=0xff0000))
    except:        
        await ctx.send(embed=discord.Embed(title="Unable to ban " + str(member) + ".", color=0xff0000))

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    try:
        await member.kick(reason = reason)
        await ctx.send(embed=discord.Embed(title=str(member) + " was kicked!", description="Reason: " + str(reason), color=0xff0000))
    except:        
        await ctx.send(embed=discord.Embed(title="Unable to kick " + str(member) + ".", color=0xff0000))

@bot.command()
async def echo(ctx, *, msg = None):
    await ctx.send(embed=echocmd.function(msg))

@bot.command()
async def commandlist(ctx):
    commandlistcmd.function(ctx)
    ctx.send(embed=discord.Embed(title="Sent the list of commands in dms!", color=0xFFFFFF))

@bot.command()
async def suggest(ctx, *, comment):
    suggestcmd.function(comment)
    await ctx.send(embed=discord.Embed(title='Suggestion Sent!', color=0xFFFFFF))

bot.run(keys.token)
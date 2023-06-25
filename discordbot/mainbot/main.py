import nextcord
from nextcord.ext import commands
import json
import os
import random
import time
import discord
from datetime import timedelta
import datetime

# Bot token
os.chdir("D:\\discordbot\\mainbot")
TOKEN = 'MTA0NTM2OTQzNDYyMzE5NzMxNA.GiDz3K.nuNjWJDcbfavVH3u_gPnEuI2wXfAzh316ZpJ5c'

# Prefix for commands
prefix = '.'

# Create bot instance with required intents
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def drown(ctx, member: nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} drowned to death.')
    await ctx.send("https://tenor.com/view/starryshuas-dog-drown-dog-funny-pool-scene-gif-24845467")

@bot.command()
@commands.has_permissions(ban_members=True)
async def burn(ctx, member: nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} has been burned to death.')
    await ctx.send("https://tenor.com/view/skeleto-skeleton-fire-hell-burn-gif-26129219")


    


@bot.command()
async def sui(ctx):
    await ctx.send("https://tenor.com/view/sui-siu-ronaldo-football-portugal-gif-25997537")

@bot.command()
async def laugh(ctx):
    await ctx.send("https://tenor.com/view/death-note-light-yagami-light-yagami-laugh-maniac-maniacal-laugh-gif-24380748")

@bot.command()
async def bal(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = nextcord.Embed(title=f"{ctx.author.name}'s balance", color=nextcord.Color.red())
    em.add_field(name = "Wallet Balance", value= wallet_amt)
    em.add_field(name = "Bank Balance", value= bank_amt)
    await ctx.send(embed = em)

@bot.command()
async def earn(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()

    earnings = random.randrange(101)
    await ctx.send(f"Someone gave you {earnings} coins !!!")

    users[str(user.id)]["wallet"] += earnings
    with open("bank.json", "w") as f:
        json.dump(users, f)
    

async def open_account(user):
    users = await get_data()


    if str(user.id) in users:
        return False
    
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        

    with open("bank.json", "w") as f:
        json.dump(users, f)
    return True
        
async def get_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users



bot.run(TOKEN)

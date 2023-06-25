import discord
from discord.ext import commands
import random
import time
from firebase import firebase
import kanto
firebase = firebase.FirebaseApplication("https://dcmondb-default-rtdb.firebaseio.com/", None)
TOKEN = 'MTA0NTM2OTQzNDYyMzE5NzMxNA.GiDz3K.nuNjWJDcbfavVH3u_gPnEuI2wXfAzh316ZpJ5c'
client = discord.Client(intents=discord.Intents.default())
client = commands.Bot(command_prefix="!*", intents=discord.Intents.all())




@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

print()
@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  channel = str(message.channel.name)
  user_message = str(message.content)
      


  print(f'Message {user_message} by {username} on {channel}, {user_message}')

  if message.author == client.user:
    return

 
  if user_message.lower() == ".start":
    embedVar = discord.Embed(
      title="Welcome",
      description=
      f"{username}, looks like you're new here! **Allow me to walk you through the basics**\n on the world of DCmon- the world of Pokémon!", color=0x6717FF)
    #isme username ko ping kar nhi rha h wo thik kardiyo
    await message.channel.send(embed=embedVar)
    time.sleep(1)
    embedVar = discord.Embed(title="Star your Journey", description= f"{username}, type  `.choose`  to choose your very first pokemon and begin your journey of conquering the world",color=0x6717FF)
    
    await message.channel.send(embed=embedVar)
  
  if user_message.lower() == ".choose":
    
    
    embedVar = discord.Embed(
      title="Well... well....well, you are about to enter the great world of Pokémon.\n**Choose one out of these three**",
      description="",color=0x6717FF)
    
    await message.channel.send(embed=embedVar)
    time.sleep(1)
    embedVar = discord.Embed(title="Star your Journey", description= f"**1. **<:kindpng_310251:1045678519470006412>Chimchar\n**2. **<:da3oic409b94747b7c344e7ac882cb79:1045675715955269753>Rowlet\n**3. **<:PngItem_3892128:1045674252625518642> Froakie\n**4. ** <:PngItem_159453:1045680073258303548> Pikachu",color=0x6717FF)
    
    await message.channel.send(embed=embedVar)
    choose = "true"

  
    
    if user_message.lower() == "1.":
            embedVar = discord.Embed(
            title="So u and chimchar(suppose the trainer chose this poke) is on a journey to be the very best and be ready for your upcoming challenges",
            description="",color=0x6717FF)
            data = {'Name':username,'Money':100,'Pokemon':'Chimchar'}
            await message.channel.send(embed=embedVar)
            result = firebase.post(f'https://dcmondb-default-rtdb.firebaseio.com/Profiles/{username}',data)
          



client.run(TOKEN)
import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
#examples https://github.com/Rapptz/discord.py/tree/master/examples

description = '''A discord bot to easily view statistics from the game Helldrivers 2 including planet info, 
Major Order updates, news, and more..'''

load_dotenv()
token = os.getenv('bot_token')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)
#client = MyClient(intents=intents)
@bot.event
async def on_ready():
    print('Logged on as', bot.user)

@bot.listen('on_message')
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if message.content == 'Democracy' or 'democracy':
        await message.channel.send('How about a cup of Liber-Tea!')

@bot.command()
async def war_status(ctx):
    #shows info on the galatic war in general
    pass
    #await ctx.send('Galactic War Stats:')

@bot.command()
async def major_orders(ctx):
    #shows info on the galatic war in general
    pass
    #await ctx.send('Current Major Order:')

@bot.command()
async def dispatches(ctx):
    #shows info on the galatic war in general
    pass
    #await ctx.send('Current Major Order:')

@bot.command()
async def planets(ctx,planet):
    #gathers liberation info on a specific planet
    await ctx.channel.send(planet)

@bot.command()
async def weapons(ctx,weapon):
    # show information on weapons
    pass

@bot.command()
async def strategems(ctx,strat):
    #pull/show info on stratgems
    pass


bot.run(token)
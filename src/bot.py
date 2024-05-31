import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient
#examples https://github.com/Rapptz/discord.py/tree/master/examples

description = '''A discord bot to easily view statistics from the game Helldrivers 2 including planet info, 
Major Order updates, news, and more..'''

load_dotenv()
token = os.getenv('bot_token')
db_uri = os.getenv('account_uri')
db_key = os.getenv('account_key')

#initialize db connection
client = CosmosClient(url=db_uri, credential=db_key)
database_name = 'democracy_bot'
database = client.get_database_client(database_name)
container_name = 'war_status'
container = database.get_container_client(container_name)

#ini
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

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
async def dispatch(ctx, arg):
    if arg == None:
        arg = 1
    #shows info on the galatic war in general
    await ctx.send('''**OPERATION \"\"ENDURING PEACE\"\"\u2014PHASE I**\n\nThe time has come to address the **Terminid Supercolony** on **Meridia**. Using an experimental substance weaponized by our top scientific minds, the Helldivers will conduct a targeted strike to permanently end the threat posed by the Supercolony.\n\nThe first phase of this operation is to secure a route to Meridia, and hold the staging ground until sufficient quantities of Dark Fluid can be weaponized and deployed. This is the priority: all other territorial losses are acceptable to ensure the success of this operation. Consult the Galactic Map on your ship for more details.''')
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

#starts bot and begins listening for events and commands
bot.run(token)
import discord

from services.dc_bot_actions import process_stock_watching
from settings import DC_BOT_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('running as', client.user)


@client.event
async def on_message(message):
    # Skip if the message was sent by bot.
    if message.author == client.user:
        return
    await process_stock_watching(message)


client.run(DC_BOT_TOKEN)

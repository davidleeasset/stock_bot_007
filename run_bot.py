import discord

from services.dc_bot_actions import DCBotActions
from settings import DC_BOT_TOKEN, DC_BOT_CONTROL_CHANNEL_IDS, DC_BOT_CONTROL_ROLE_IDS

client = discord.Client()


@client.event
async def on_ready():
    print('running as', client.user)


async def process_stock_watching(message):
    if message.channel.id in DC_BOT_CONTROL_CHANNEL_IDS and message.author.top_role.id in DC_BOT_CONTROL_ROLE_IDS:
        msg = message.content
        if msg.startswith('--'):
            bot_actions = DCBotActions(message)
            msgs = message.content.strip().replace("--", "").split(" ")
            action = msgs[0]

            if action == "wl":
                await bot_actions.show_watching_list()
            elif action == "add_w":
                if len(msgs) != 2:
                    await message.channel.send("--add_w takes 2 args.")
                await bot_actions.add_to_watching_list(msgs[1])
            elif action == "del_w":
                if len(msgs) != 2:
                    await message.channel.send("--del_w takes 2 args.")
                await bot_actions.delete_from_watching_list(msgs[1])
            elif action in ["help", "h"]:
                await message.channel.send(
                    "--wl :show watching list \n"
                    "--add_w $symbol : add $symbol to watching list\n"
                    "--del_w $symbol : remove $symbol from the watching list"
                )
            else:
                await message.channel.send("are you sending a command? use --help")


@client.event
async def on_message(message):
    # Skip if the message was sent by bot.
    if message.author == client.user:
        return
    await process_stock_watching(message)


client.run(DC_BOT_TOKEN)

import discord
client = discord.Client()


@client.event
async def on_ready():
    print('目前登入身份：', client.user)


@client.event
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('#'):
        msgs = message.content.replace("#", "").split(" ")
        action = msgs[0]

        if action == "hi":
            await message.channel.send("hello")

client.run('OTUwNTYxMzQ1OTA3MDY0ODky.YiatPQ.YHqmm_gEQJU7hFcQ6aanU1Rjdlo')

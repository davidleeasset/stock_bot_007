from services.mongo_access import MongoDBCollections
from settings import DC_BOT_CONTROL_CHANNEL_IDS, DC_BOT_CONTROL_ROLE_IDS


class DCBotActions:
    def __init__(self, message):
        self.message = message
        self.mongo = MongoDBCollections()

    async def show_watching_list(self):
        watching_list = self.mongo.get_watch_dict().keys()
        await self.message.channel.send(f"觀察清單: {', '.join(watching_list)}")

    async def add_to_watching_list(self, symbol):
        self.mongo.add_watch(symbol)
        watching_list = self.mongo.get_watch_dict().keys()
        await self.message.channel.send(f"已增加, 更新後的觀察清單: {', '.join(watching_list)}")

    async def delete_from_watching_list(self, symbol):
        self.mongo.del_watch(symbol)
        watching_list = self.mongo.get_watch_dict().keys()
        await self.message.channel.send(f"已刪除, 更新後的觀察清單: {', '.join(watching_list)}")


async def process_stock_watching(message):
    if message.channel.type.value == 1:  # is private message
        pass
    elif message.channel.id in DC_BOT_CONTROL_CHANNEL_IDS and message.author.top_role.id in DC_BOT_CONTROL_ROLE_IDS:
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
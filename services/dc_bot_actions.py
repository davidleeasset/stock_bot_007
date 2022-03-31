from services.mongo_access import MongoDBCollections


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

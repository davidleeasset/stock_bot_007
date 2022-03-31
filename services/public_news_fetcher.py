from services.mongo_access import MongoDBCollections
from venders.cnyes import CNYes
from venders.dc_webhook import DiscordWebhook, DiscordWebhookChannels
from venders.mops import MOPS


class PublicNewsFetcher:
    def __init__(self):
        self.mongo = MongoDBCollections()
        self.watch_dict = self.mongo.get_watch_dict()
        self.mops_client = MOPS()
        self.cnyes_client = CNYes()

    def fetch_news(self):
        for symbol in self.watch_dict.keys():
            for new_from_cnyes in self.cnyes_client.get_news(symbol):
                DiscordWebhook.send_message(
                    DiscordWebhookChannels.news_hook,
                    message=f"關鍵字: {symbol}",
                    embeds=[
                        {
                            "title": f"{new_from_cnyes['title']}",
                            "description": new_from_cnyes["summary"],
                            "url": new_from_cnyes["link"],
                            "color": 5814783
                        }
                    ]
                )
            # for news_to_feed in self.mops_client.get_public_news(symbol):
            #     DiscordWebhook.send_message(
            #         DiscordWebhookChannels.public_news_hook,
            #         message=f"公開資訊觀測站發布",
            #         embeds=[
            #             {
            #                 "title": f"**{symbol}**",
            #                 "description": news_to_feed,
            #                 "color": 5814783
            #             }
            #         ]
            #     )

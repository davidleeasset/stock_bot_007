from services.mongo_access import MongoDBCollections
from venders.dc_webhook import DiscordWebhook, DiscordWebhookChannels
from venders.mops import MOPS


class PublicNewsFetcher:
    def __init__(self):
        self.mongo = MongoDBCollections()
        self.watch_dict = self.mongo.get_watch_dict()
        self.mops_client = MOPS()

    def fetch_news(self):
        for symbol in self.watch_dict.keys():
            for news_to_feed in self.mops_client.get_public_news(symbol):
                DiscordWebhook.send_message(
                    DiscordWebhookChannels.public_news_hook,
                    message=f"公開資訊觀測站發布",
                    embeds=[
                        {
                            "title": f"**{symbol}**",
                            "description": news_to_feed,
                            "color": 5814783
                        }
                    ]
                )

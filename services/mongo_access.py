import pymongo

from settings import MONGODB_URL

client = pymongo.MongoClient(MONGODB_URL)


class MongoDBCollections:
    daily = client.stock_007.daily
    daily_money_flow = client.stock_007.daily_money_flow
    watch_list = client.stock_007.watch_list
    public_news = client.stock_007.public_news

    def update_daily(self, date, symbol, data):
        self.daily.update_one(
            {
                "date": date,
                "symbol": symbol
            },
            {"$set": data},
            True
        )
        print(f"{symbol} {date} updated!")

    def get_watch_dict(self):
        """
        :return:
        [{
            "symbol": "3037",
            "data": {
                "date": "date",
                "high": 251,
                "low": 249,
                "close": 250
            }  # optional key
        }]
        """
        return {watch["symbol"]: watch for watch in self.watch_list.find()}

    def update_watch(self, symbol, data):
        self.watch_list.update_one(
            {
                "symbol": symbol
            },
            {"$set": {
                "data": data
            }},
            True
        )
        print(f"{symbol} watch updated!")

    def get_public_news(self, symbol, key):
        return list(self.public_news.find({"symbol": symbol, "key": key}))

    def create_public_news(self, symbol, key, content):
        return self.public_news.update_one(
            {"symbol": symbol, "key": key},
            {"$set": {
                "content": content
            }},
            True
        )

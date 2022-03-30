import pymongo

from settings import MONGODB_URL

client = pymongo.MongoClient(MONGODB_URL)


class MongoDBCollections:
    daily = client.stock_007.daily
    daily_money_flow = client.stock_007.daily_money_flow
    watch_list = client.stock_007.watch_list

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

import pymongo

from settings import MONGODB_URL

client = pymongo.MongoClient(MONGODB_URL)


class MongoDBCollections:
    daily = client.stock_007.daily
    daily_money_flow = client.stock_007.daily_money_flow
    watch_list = client.stock_007.watch_list
    public_news = client.stock_007.public_news
    money_flow_group = client.stock_007.money_flow_group
    income = client.stock_007.income

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

    def add_watch(self, symbol):
        self.watch_list.update_one(
            {
                "symbol": symbol
            },
            {"$set": {"symbol": symbol}},
            True
        )
        print(f"{symbol} watch added!")

    def del_watch(self, symbol):
        self.watch_list.remove({"symbol": symbol})
        print(f"{symbol} watch removed!")

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

    def insert_income(self, symbol, date_key, data):
        self.income.update_one(
            {"symbol": symbol, "date_key": date_key},
            {"$set": data},
            True
        )

    def get_group_list(self):
        return [group["name"] for group in self.money_flow_group.find()]

    def add_or_enable_group(self, name: str, stock_symbol_list: list = None):
        money_flow_group = self.money_flow_group.find_one({"name": name})
        exists_stocks = money_flow_group["stcoks"] if money_flow_group else []
        self.money_flow_group.update_one(
            {
                "name": name
            },
            {"$set": {
                "enabled": True,
                "stocks": list(set(stock_symbol_list or [] + exists_stocks))
            }},
            True
        )
        print(f"{name} group disabled!")

    def disable_group(self, name):
        self.money_flow_group.update_one(
            {
                "name": name
            },
            {"$set": {"enabled": False}},
            False
        )
        print(f"{name} group disabled!")

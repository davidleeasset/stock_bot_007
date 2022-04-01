from services.mongo_access import MongoDBCollections
from venders.mopsfin import Mopsfin


class IncomeProcessor:
    def __init__(self):
        self.mongo = MongoDBCollections()
        self.data = Mopsfin().get_income()

    def process(self):
        for index, item in self.data.iterrows():
            item_dict = item.to_dict()
            symbol = item_dict.pop("symbol")
            date_key = item_dict.pop("date_key")
            print(f"processing {symbol} {date_key}")
            self.mongo.insert_income(symbol=symbol, date_key=date_key, data=item_dict)

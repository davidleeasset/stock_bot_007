import requests

from services.mongo_access import MongoDBCollections


class CNYes:
    def __init__(self):
        self.mongo = MongoDBCollections()

    def get_news(self, symbol):
        response = requests.get(url=f"https://ess.api.cnyes.com/ess/api/v1/news/keyword?q={symbol}&limit=20&page=1")
        """
        {
        'objectType': 'NEWS', 'newsId': 4844692, 'title': '欣興:本公司董事會決議通過與旭德科技股份有限公司股份轉換事宜', 
        'summary': '欣興:本公司董事會決議通過與旭德科技股份有限公司股份轉換事宜', 
        'category': [{'categoryId': '868', 'name': '台股公告'}], 
        'publishAt': 1648645796, 'coverSrc': {'xs': None, 's': None, 'm': None, 'l': None, 'xl': None, 'xxl': None},
         'payment': 0
         }
         link https://news.cnyes.com/news/id/4844692
        """
        news = []
        for item in response.json()["data"]["items"]:
            key = f"news_{symbol}_{item['newsId']}"
            if self.mongo.get_public_news(symbol, key):
                return None
            item["link"] = f"https://news.cnyes.com/news/id/{item['newsId']}"
            news.append(item)
            self.mongo.create_public_news(symbol, key=key, content=item)
        return news

import requests
from bs4 import BeautifulSoup

from services.mongo_access import MongoDBCollections


class MOPS:
    def __init__(self):
        self.mongo = MongoDBCollections()

    def get_public_news_detail(self, symbol, detail_dict):
        key = f"{detail_dict['keyword']}_{detail_dict['spoke_date']}_{detail_dict['seq_no']}"
        if self.mongo.get_public_news(symbol, key):
            return None
        response = requests.post(
            url="https://mops.twse.com.tw/mops/web/ajax_t05st01", data=detail_dict
        )
        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')
        content_table = soup.find('table', {'class': 'hasBorder'})
        contents = []
        for tr in content_table.find_all('tr'):
            contents.append(tr.get_text())
        content_msg = "\n".join(contents)
        self.mongo.create_public_news(symbol, key=key, content=content_msg)
        return content_msg

    def get_public_news(self, symbol):
        data = {
            "firstin": "Y",
            "TYPEK": "all",
            "step": "1",
            "co_id": symbol,
            "funcName": "t146sb05",
            "searchtype": None,
            "inpuType": "keyword",
            "auto-more": None,
            "keycon": None,
            "keyword": symbol
        }
        response = requests.post(
            url="https://mops.twse.com.tw/mops/web/t146sb05", data=data
        )
        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')
        public_news_table = soup.find('div', {"id": "company"}).find_all('table')[1]
        news = []
        for tr in public_news_table.find_all('tr'):
            button = tr.find_all('td')[1].find("button")
            if not button:
                continue
            detail_text = button.attrs["onclick"]
            for x in detail_text.split(";"):
                if str.startswith(x, "document.fm1") and not str.startswith(x, "document.fm1.action"):
                    field, value = x.replace("document.fm1.", "").replace("'", "").replace(".value", "").split("=")
                    data[field] = value
            new_news = self.get_public_news_detail(symbol, data)
            if new_news:
                news.append(new_news)
        return news

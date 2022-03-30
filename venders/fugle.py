import requests


class Fugle:
    @classmethod
    def get_heatmap(cls, market):  # IX0043
        if market not in ("IX0001", "IX0043"):
            raise Exception(f"wrong market {market}!")

        r = requests.get(f'https://heatmap.fugle.tw/api/heatmaps/{market}')
        """
            {
                "date": "2022-03-29",
                "type": "EQUITY",
                "exchange": "TPEx",
                "symbol": "3491",
                "name": "昇達科",
                "openPrice": 194.5,
                "highPrice": 197.5,
                "lowPrice": 187.5,
                "closePrice": 190,
                "change": -6,
                "changePercent": -3.06,
                "previousClose": 196,
                "tradeVolume": 6302,
                "tradeValue": 1210687,
                "tradeValueWeight": 1.9918488110902715,
                "marketValueWeight": 0.2316,
                "industry": "27",
                "lastUpdated": 1648530720193344
            }
        """
        return [stock for stock in r.json() if stock["type"] == "EQUITY" and "openPrice" in stock]

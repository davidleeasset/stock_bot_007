import requests


class TPEX:
    def get_daily_hedge_result(self):
        response = requests.get("https://www.tpex.org.tw/web/stock/3insti/daily_trade/"
                                "3itrade_hedge_result.php?l=zh-tw&se=EW&t=D")
        data = response.json()
        return data['reportDate'], data["aaData"]

from datetime import datetime

import requests

from services.local_time_helper import LocalDateTime


class TWSE:
    def __init__(self):
        self.local_time_helper = LocalDateTime()

    def get_daily_hedge_result(self, date=None):
        if date is None:
            date = self.local_time_helper.local_today_date
        uri = f"https://www.twse.com.tw/fund/T86?response=json&date={date.strftime('%Y%m%d')}&selectType=ALLBUT0999&_=1615364742259"
        print(uri)
        data = requests.get(uri).json()

        if "data" not in data:
            return None, None

        data_date = datetime.strptime(f'{data["date"]} 09:00', "%Y%m%d %H:%M")
        return data_date, data["data"]

from venders.tpex import TPEX
from venders.twse import TWSE


class BuyAndSellService:
    def fetch_data(self):
        otc_result = TPEX().get_daily_hedge_result()
        list_result = TWSE().get_daily_hedge_result()
        print(otc_result)


BuyAndSellService().fetch_data()
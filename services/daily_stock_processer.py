from datetime import datetime

from services.mongo_access import MongoDBCollections
from venders.dc_webhook import DiscordWebhook, DiscordWebhookChannels
from venders.fugle import Fugle


class DailyStockProcessor:
    def __init__(self):
        self.mongo = MongoDBCollections()
        self.watch_dict = self.mongo.get_watch_dict()

    def run(self):
        self.process_list(Fugle.get_heatmap("IX0001"))
        self.process_list(Fugle.get_heatmap("IX0043"))

    def single_stock_check(self, stock_data):
        if stock_data["symbol"] in self.watch_dict:
            watch_data = self.watch_dict[stock_data["symbol"]]
            daily_watch_data = watch_data.get("data")
            current_watch_data = {
                "date": stock_data["date"],
                "high": stock_data["highPrice"],
                "low": stock_data["lowPrice"],
                "close": stock_data["closePrice"]
            }
            trade_vol = stock_data["tradeValue"]/100000
            plus_str = "+" if stock_data['changePercent'] > 0 else ""
            base_msg = f"{stock_data['name']} {stock_data['symbol']} " \
                       f"價格 ${stock_data['closePrice']} 趴數 {plus_str}{stock_data['changePercent']}% " \
                       f"成交量 {trade_vol:.2f} 億"
            if daily_watch_data and daily_watch_data["date"] == stock_data["date"]:
                last_close = daily_watch_data["close"]
                if stock_data["closePrice"] > daily_watch_data["high"]:
                    DiscordWebhook.send_message(
                        DiscordWebhookChannels.watch_hook,
                        message=f"新高! {base_msg}"
                    )
                    self.mongo.update_watch(stock_data["symbol"], data=current_watch_data)
                elif stock_data["closePrice"] < daily_watch_data["low"]:
                    DiscordWebhook.send_message(
                        DiscordWebhookChannels.watch_hook,
                        message=f"新低! {base_msg}"
                    )
                    self.mongo.update_watch(stock_data["symbol"], data=current_watch_data)
                elif 100 * abs(last_close - stock_data["closePrice"]) / last_close > 1:
                    DiscordWebhook.send_message(
                        DiscordWebhookChannels.watch_hook,
                        message=f"價格變動! {base_msg}"
                    )
                    self.mongo.update_watch(stock_data["symbol"], data=current_watch_data)
            else:
                DiscordWebhook.send_message(
                    DiscordWebhookChannels.watch_hook,
                    message=f"開始觀察({stock_data['date']}): {base_msg}"
                )
                self.mongo.update_watch(stock_data["symbol"], data=current_watch_data)

    def process_list(self, data_list):
        for stock in data_list:
            self.single_stock_check(stock_data=stock)
            self.mongo.update_daily(
                date=datetime.strptime(stock["date"], "%Y-%m-%d"),
                symbol=stock["symbol"],
                data={
                    "name": stock["name"],
                    "open_price": stock["openPrice"],
                    "high_price": stock["highPrice"],
                    "low_price": stock["lowPrice"],
                    "close_price": stock["closePrice"],
                    "change": stock["change"],
                    "change_percent": stock["changePercent"],
                    "previous_close": stock["previousClose"],
                    "trade_volume": stock["tradeVolume"],
                    "trade_value": stock["tradeValue"],
                    "trade_value_weight": stock["tradeValueWeight"],
                    "market_value_weight": stock["marketValueWeight"],
                    "industry": stock["industry"],
                    "last_updated": stock["lastUpdated"]
                }
            )

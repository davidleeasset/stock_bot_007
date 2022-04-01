import pandas


class Mopsfin:
    def get_income(self):
        data_list = pandas.read_csv("https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv")
        data_otc = pandas.read_csv("https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv")
        data = pandas.concat([data_list, data_otc])
        data.columns = [
            "datetime", "date_key", "symbol", "name", "industry", "income", "last_income", "mom", "yoy",
             "yoy_diff", "income_this_year", "income_last_year", "to_date_yoy", "note"
        ]
        return data

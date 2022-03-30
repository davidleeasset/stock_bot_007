from datetime import datetime

from pytz import timezone


class LocalDateTime:
    def __init__(self):
        self.localtz = timezone('Asia/Taipei')
        self.today = self.localtz.localize(datetime.utcnow())
        self.today_str = self.today.strftime('%Y-%m-%d')
        self.today_date = datetime.strptime(f'{self.today_str} 09:00', "%Y-%m-%d %H:%M")
        self.local_today_date = self.localtz.localize(self.today_date)

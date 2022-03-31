from apscheduler.schedulers.blocking import BlockingScheduler

from services.daily_stock_processer import DailyStockProcessor
from services.public_news_fetcher import PublicNewsFetcher

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='1', minute="1,2,3,*/5")
def open_scanner():
    DailyStockProcessor().run()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='2-4', minute="*/5")
def daily_scanner():
    DailyStockProcessor().run()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='5', minute="0-35/5")
def close_scanner():
    DailyStockProcessor().run()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='1-12/4', minute="27")
def fetch_public_news():
    PublicNewsFetcher().fetch_news()


sched.start()

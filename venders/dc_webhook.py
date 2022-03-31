import requests
import settings


class DiscordWebhookChannels:
    watch_hook = settings.WATCH_HOOK
    public_news_hook = settings.PUBLIC_NEWS_HOOK
    news_hook = settings.NEWS_HOOK


class DiscordWebhook:
    @classmethod
    def send_message(cls, hook, message, embeds=None):
        print(message)
        result = requests.post(
            url=hook,
            json={
                "content": message,
                "embeds": embeds
            }
        )
        print(result)

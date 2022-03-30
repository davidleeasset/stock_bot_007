import requests


class DiscordWebhookChannels:
    watch_hook = "https://discordapp.com/api/webhooks/958607409805398086/" \
                 "vmtCscpLfCl_n1kYRr3x8Q9DRUQ4hz5ULz4c5MB93lu1_5xr1m9U_kRaMtQhzPRpXMFj"


class DiscordWebhook:
    @classmethod
    def send_message(cls, hook, message):
        requests.post(
            url=hook,
            json={
                "content": message,
                "embeds": None
            }
        )

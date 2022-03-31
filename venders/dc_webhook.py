import requests


class DiscordWebhookChannels:
    watch_hook = "https://discordapp.com/api/webhooks/958607409805398086/" \
                 "vmtCscpLfCl_n1kYRr3x8Q9DRUQ4hz5ULz4c5MB93lu1_5xr1m9U_kRaMtQhzPRpXMFj"
    public_news_hook = "https://discordapp.com/api/webhooks/958915830610010202/" \
                       "uGTC03E_5AYhmm3f_4TrmJlcocmSopPDFZm326TfvXaYPph2BAdoggmP1aJILCAB2R2A"
    news_hook = "https://discordapp.com/api/webhooks/958961716690042950/" \
                "4wXzdbAUAgnYnwZFVfZP0lPr2ABc_PLxtxMmrlqxP4heWp9_Nb6P60W8CsxCNqKYB3uc"


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

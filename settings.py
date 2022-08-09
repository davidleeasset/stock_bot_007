MONGODB_URL = "--"

DC_BOT_TOKEN = '--'
DC_BOT_CONTROL_CHANNEL_IDS = []
DC_BOT_CONTROL_ROLE_IDS = []

WATCH_HOOK = "--"
PUBLIC_NEWS_HOOK = "--"
NEWS_HOOK = "--"

import sentry_sdk
sentry_sdk.init(
    "--",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

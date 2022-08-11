import os

import sentry_sdk

MONGODB_URL = os.environ.get("MONGODB_URL", "--")

DC_BOT_TOKEN = os.environ.get("DC_BOT_TOKEN", "--")
DC_BOT_CONTROL_CHANNEL_IDS = []
DC_BOT_CONTROL_ROLE_IDS = []

WATCH_HOOK = os.environ.get("WATCH_HOOK", "--")
PUBLIC_NEWS_HOOK = os.environ.get("PUBLIC_NEWS_HOOK", "--")
NEWS_HOOK = os.environ.get("NEWS_HOOK", "--")

sentry_sdk.init(
    os.environ.get("SENTRY_URL", "--"),
    traces_sample_rate=1.0
)

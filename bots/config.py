from datetime import datetime
from os import environ
from pathlib import Path


class Settings:
    id = environ.get("NOMICS_COIN_ID")

    reload_delay = environ.get("DELAY", 5)
    debug = environ.get("DEBUG", "").lower() == "true"


class Tokens:
    nomics = environ.get("NOMICS_TOKEN")
    ethgasstation = environ.get("ETHGASSTATION_TOKEN")

    bots = {
        "price": environ.get("PRICE_BOT_TOKEN"),
        "volume": environ.get("VOLUME_BOT_TOKEN"),
        "gas": environ.get("GAS_BOT_TOKEN")
    }


class Logs:
    path = Path("bots/logs")
    name = f"{datetime.today().strftime('%d-%m-%Y')}.log"

    fmt = "%(asctime)s - %(name)s %(levelname)s: %(message)s"
    datefmt = "%D %H:%M:%S"


class Symbols:
    arrow_up = "↗"
    arrow_down = "↘"


class Nicknames:
    price = "${price:,.2f} ({arrow})"
    volume = "${volume} ({arrow})"
    gas = "⚡{gas} gwei"


class Status:
    price = "price 24h: {pct:+.2%}"
    volume = "volume 24h: {pct:+.2%}"
    gas = "🚶{fast}, 🐢{regular}"

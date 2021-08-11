from datetime import datetime
from os import environ
from pathlib import Path


class Settings:
    name = "Million"
    debug = environ.get("DEBUG", "").lower() == "true"


class Tokens:
    bots = {
        "price": environ.get("PRICE_BOT_TOKEN"),
        "volume": environ.get("VOLUME_BOT_TOKEN"),
        "cap": environ.get("CAP_BOT_TOKEN"),
        "holders": environ.get("HOLDERS_BOT_TOKEN"),
        "gas": environ.get("GAS_BOT_TOKEN")
    }


class Logs:
    path = Path("bots/logs")
    name = f"{datetime.today().strftime('%d-%m-%Y')}.log"

    fmt = "%(asctime)s - %(name)s %(levelname)s: %(message)s"
    datefmt = "%D %H:%M:%S"

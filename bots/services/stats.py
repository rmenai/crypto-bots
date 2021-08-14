import asyncio
import logging
import sys
from typing import List

from bots.config import Settings, Tokens
from bots.utils.api import etherescan, nomics

log = logging.getLogger(__name__)

# Handle missing keys or tokens
for action in Tokens.bots.keys():
    if action in ["price", "volume", "cap"]:
        if not Settings.id:
            log.info("You need to provide NOMICS_COIN_ID")
            sys.exit()
        elif not Tokens.nomics:
            log.info("You need to provide NOMICS_API_KEY")
            sys.exit()


class Coin:
    """A class representing a coin data."""

    def __init__(self, coin_id: str, actions: List[str]):
        self.id = coin_id

        self.price = 0
        self.market_cap = 0
        self.volume = 0

        self.price_change_pct = 0
        self.market_cap_change_pct = 0
        self.volume_change_pct = 0

        self.gas = {'slow': 0, 'regular': 0, 'fast': 0, 'fastest': 0}

        # Add tasks according to the actions
        self.tasks = set()
        for task in actions:
            if task in ["price", "volume", "cap"]:
                self.tasks.add(self.fetch_data)
            elif action == "gas":
                self.tasks.add(self.fetch_gas)

        self.loop = asyncio.get_event_loop()

    def _update(self, **kwargs) -> None:
        """Update the values of the coin and format the data."""
        for key, value in kwargs.items():
            if key == "1d":
                self.price_change_pct = float(value.get("price_change_pct", 0))
                self.market_cap_change_pct = float(value.get("market_cap_change_pct", 0))
                self.volume_change_pct = float(value.get("volume_change_pct", 0))
                self.volume = float(value.get("volume", 0))
            elif key in self.__dict__:
                try:
                    self.__dict__.update({key: float(value)})
                except ValueError:
                    self.__dict__.update({key: value})

    def fetch_data(self) -> None:
        """Fetch new coin data."""
        r = nomics.Currencies.get_currencies(ids=self.id)
        if not r:
            # If the response is empty it means that the coin id is invalid.
            log.error("NOMICS_COIN_ID is invalid.")

            self.loop.stop()
            return
        elif isinstance(r, str):
            # If the response is a string it means the API key is invalid.
            log.error("NOMICS_API_KEY is invalid.")

            self.loop.stop()
            return

        self._update(**r[0])

    def fetch_gas(self) -> None:
        """Fetch eth gas prices."""
        r = etherescan.get_gasprices()
        for key, value in r.items():
            if value is None:
                continue
            else:
                self.gas[key] = value

    def reload(self) -> None:
        """Run all coin tasks."""
        for task in self.tasks:
            task()


coin = Coin(Settings.id, actions=Tokens.bots.keys())

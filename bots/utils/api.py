import logging
import sys

from bots.config import Settings, Tokens
from ethereum_gasprice import GaspriceController
from ethereum_gasprice.consts import EthereumUnit
from ethereum_gasprice.providers import EthGasStationProvider
from nomics import Nomics

log = logging.getLogger(__name__)

if not Tokens.nomics:
    log.info("You need to provide NOMICS_TOKEN")
    sys.exit()

if Tokens.bots["gas"] and not Tokens.ethgasstation:
    log.info("You need to provide ETHGASSTATION_TOKEN")
    sys.exit()

nomics = Nomics(Tokens.nomics)
etherescan = GaspriceController(
    settings={EthGasStationProvider.title: Tokens.ethgasstation},
    return_unit=EthereumUnit.GWEI
)


class Coin:
    """A class representing a coin data."""

    def __init__(self):
        self.id = ""
        self.currency = ""
        self.symbol = ""
        self.name = ""
        self.logo_url = ""
        self.status = ""
        self.price = 0
        self.price_date = ""
        self.price_timestamp = ""
        self.circulating_supply = 0
        self.max_supply = 0
        self.market_cap = 0
        self.market_cap_dominance = 0
        self.num_exchanges = 0
        self.num_pairs = ""
        self.num_pairs_unmapped = ""
        self.first_candle = ""
        self.first_trade = ""
        self.first_order_book = ""
        self.rank = 9999
        self.rank_delta = ""
        self.high = ""
        self.high_timestamp = ""

        self.price_change_pct = 0
        self.market_cap_change_pct = 0
        self.volume = 0
        self.volume_change_pct = 0

        self.gas = {'slow': 0, 'regular': 0, 'fast': 0, 'fastest': 0}

    def _update(self, **kwargs) -> None:
        """Update the values of the coin and format the data."""
        for key, value in kwargs.items():
            if value:
                if key == "name" or key == "symbol":
                    self.__dict__.update({key: value})
                    continue
                elif key == "1d":
                    self.price_change_pct = float(value.get("price_change_pct", 0))
                    self.market_cap_change_pct = float(value.get("market_cap_change_pct", 0))
                    self.volume_change_pct = float(value.get("volume_change_pct", 0))
                    self.volume = float(value.get("volume", 0))
                    continue

                try:
                    self.__dict__.update({key: float(value)})
                except ValueError:
                    self.__dict__.update({key: value})
                except TypeError:
                    self.__dict__.update({key: value})

    def reload(self) -> None:
        """Fetch new coin data."""
        r = nomics.Currencies.get_currencies(ids=Settings.id)
        if not r:
            log.error("NOMICS_COIN_ID is invalid.")
            sys.exit()

        self._update(**r[0])

        if Tokens.bots["gas"]:
            r = etherescan.get_gasprices()
            for key, value in r.items():
                if value is None:
                    continue
                else:
                    self.gas[key] = value


coin = Coin()

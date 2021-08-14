import ethereum_gasprice
from bots.config import Tokens
from nomics import Nomics

nomics = Nomics(Tokens.nomics)

# Uses free etherscan API key.
etherescan = ethereum_gasprice.GaspriceController(
    return_unit=ethereum_gasprice.EthereumUnit.GWEI
)

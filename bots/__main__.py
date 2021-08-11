from bots.bots import client
from bots.config import Tokens
from bots.utils.extensions import walk_extensions

for ext in walk_extensions():
    client.load_extension(ext)

client.run(Tokens.bots)

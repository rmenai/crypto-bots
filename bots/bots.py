import asyncio
import logging
import re
import sys
from typing import Any, Dict

from bots.config import Settings
from bots.utils.api import coin
from bots.utils.coin import repeat
from discord.errors import LoginFailure
from discord.ext import commands

log = logging.getLogger(__name__)

if not Settings.id:
    log.info("You need to provide NOMICS_COIN_ID")
    sys.exit()


def exception_handler(loop: Any, context: Dict[str, Any]) -> None:
    """Handle asyncio tasks exceptions."""
    if isinstance(context["exception"], LoginFailure):
        log.error("There is an invalid token")
        loop = asyncio.get_event_loop()
        loop.stop()


class Bot(commands.Bot):
    """Base bot class."""

    def __init__(self):
        # Initiate a bot without a command prefix
        super(Bot, self).__init__(None)

    async def edit_nick(self, nick: str) -> None:
        """Edit the nickname of the bot in all servers."""
        for guild in self.guilds:
            await guild.get_member(self.user.id).edit(nick=nick)


class Bots:
    """Base client class."""

    def __init__(self, bots: Dict[str, Bot]) -> None:
        self.bots = bots
        self.running = []

    def load_extension(self, path: str) -> None:
        """Load bot cogs extensions."""
        folder, name = re.findall(r"bots\.exts\.(\w+)\.(\w+)", path)[0]
        if folder == "status":
            # The file must be the same name as the bot
            bot = self.bots.get(name)
            if bot:
                try:
                    bot.load_extension(path)
                except commands.errors.NoEntryPointError:
                    pass

    def run(self, tokens: Dict[str, str]) -> None:
        """Run the bots forever."""
        loop = asyncio.get_event_loop()

        # Reload the coin data forever with a delay
        loop.create_task(repeat(coin.reload, delay=Settings.reload_delay))

        for name, token in tokens.items():
            if token:
                loop.create_task(self.bots[name].start(token))
                self.running.append(name)

        # Handle exceptions
        if self.running:
            log.info(f"Client starting for {Settings.id} with {', '.join(self.running)}")
            log.info(f"Updating bots status every {Settings.reload_delay} seconds.")
            loop.set_exception_handler(exception_handler)
            loop.run_forever()
        else:
            log.info("Bots are not running, please provide valid tokens")


client = Bots(
    {
        "price": Bot(),
        "volume": Bot(),
        "gas": Bot()
    }
)

import asyncio
import logging
import re
from typing import Dict

from bots.config import Settings
from bots.services.stats import coin
from bots.utils.loops import repeat
from discord.errors import LoginFailure
from discord.ext import commands

log = logging.getLogger(__name__)


class Bot(commands.Bot):
    """Base bot class."""

    def __init__(self):
        # Initiate a bot without a command prefix
        self.name = ""
        super(Bot, self).__init__(None)

    async def start(self, *args, **kwargs) -> None:
        """Start the bot."""
        try:
            await super(Bot, self).start(*args, *kwargs)
        except LoginFailure:
            log.error(f"{self.name.upper()}_BOT_TOKEN is an invalid discord token.")
            self.loop.stop()

    async def edit_nick(self, nick: str) -> None:
        """Edit the nickname of the bot in all servers."""
        for guild in self.guilds:
            await guild.get_member(self.user.id).edit(nick=nick)


class Bots:
    """Base client class."""

    def __init__(self, bots: Dict[str, Bot]) -> None:
        self.bots = bots
        self.coin = coin

        self.actions = []

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
        self.actions = [key for key in tokens.keys() if key]

        if not self.actions:
            log.info("Bots are not running, please provide at least one token")
            return

        loop = asyncio.get_event_loop()
        loop.create_task(repeat(coin.reload, delay=Settings.reload_delay))

        # Reload the coin data forever with a delay
        for action in self.actions:
            bot = self.bots[action]
            bot.name = action

            loop.create_task(bot.start(tokens[action]))

        log.info(f"Client starting for {Settings.id} with {', '.join(self.actions)}")
        log.info(f"Updating bots status every {Settings.reload_delay} seconds.")

        loop.run_forever()


client = Bots({
    "price": Bot(),
    "volume": Bot(),
    "cap": Bot(),
    "gas": Bot()
})

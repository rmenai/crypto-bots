import logging

import discord
from bots.bots import Bot
from bots.config import Nicknames, Settings, Status
from bots.services.stats import coin
from bots.utils.coin import get_arrow
from discord.ext import commands, tasks

log = logging.getLogger(__name__)


class Price(commands.Cog):
    """A cog for updating the price of a bot."""

    def __init__(self, client: Bot):
        self.client = client

        self.coin = coin

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """When the bot is ready."""
        log.debug(f"{self.client.user} has connected!")
        self.update_status.start()

    @tasks.loop(seconds=Settings.reload_delay)
    async def update_status(self) -> None:
        """Update the bot nickname and status."""
        if not self.coin.price:
            return

        arrow = get_arrow(self.coin.price_change_pct)
        nick = Nicknames.price.format(price=self.coin.price, arrow=arrow)
        status = Status.price.format(pct=self.coin.price_change_pct)

        await self.client.edit_nick(nick)
        await self.client.change_presence(activity=discord.Game(status))


def setup(bot: Bot) -> None:
    """Load the Price Cog."""
    bot.add_cog(Price(bot))

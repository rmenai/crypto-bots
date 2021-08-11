import asyncio
import logging
from typing import Any, Dict

from discord import Client
from discord.errors import LoginFailure

log = logging.getLogger(__name__)


def exception_handler(loop: Any, context: Dict[str, Any]) -> None:
    """Handle asyncio tasks exceptions."""
    if isinstance(context["exception"], LoginFailure):
        log.error("There is an invalid token")
        loop = asyncio.get_event_loop()
        loop.stop()


class Bots:
    """Base class."""

    def __init__(self, bots: Dict[str, Client]) -> None:
        self.bots = bots
        self.running = []

    def run(self, tokens: Dict[str, str]) -> None:
        """Run the bots forever."""
        loop = asyncio.get_event_loop()
        for name, token in tokens.items():
            if token:
                loop.create_task(self.bots[name].start(token))
                self.running.append(name)

        # Handle exceptions
        if self.running:
            log.info(f"Client started with {', '.join(self.running)}")
            loop.set_exception_handler(exception_handler)
            loop.run_forever()
        else:
            log.info("Bots are not running, please provide valid tokens")


client = Bots(
    {
        "price": Client(),
        "volume": Client(),
        "cap": Client(),
        "holders": Client(),
        "gas": Client()
    }
)

import argparse
import importlib
from typing import List

from shortify import __version__
from shortify.constants import SUPPORTED_SERVICES


class Application:
    """Shortify :class:`Application` class for all possible needs."""

    def __init__(self):
        """:class:`Application` dunder init method."""
        self.parser = argparse.ArgumentParser(
            prog="shortify",
            usage="%(prog)s <service> <url to shorten>",
            description="Shortify Command-Line Interface.",
        )

    def initialize(self) -> None:
        """`shortify.initialize` function, the place where all set args get passed.

        Later on we use this feature in `self.run` method.
        """
        self.parser.add_argument(
            "-v", "--version", action="version", version=f"%(prog)s {__version__}"
        )
        self.parser.add_argument(
            "service",
            choices=SUPPORTED_SERVICES,
            help="Provide a service you'd like to use.",
        )
        self.parser.add_argument("url", help="Pass an URL to shorten.")

    def run(self, argv: List[str]) -> None:
        """Here we handle all positional arguments the user provides.

        Then shortenize the URL according to the known arguments.

        Parameters
        ----------
        argv : List[str]
            List of args passed in the terminal.
        """
        self.initialize()
        args = self.parser.parse_args()
        module = importlib.import_module("shortify.services." + args.service)
        service = module.Shortener()

        # TODO: probably need to do something other than print()
        print(service.shorten(args.url))

"""The command-line interface of shortify."""

import sys
from typing import List, Optional

from shortify.main.app import Application


def main(argv: Optional[List[str]] = sys.argv[1:]) -> None:
    """Execute the main bit of the app.

    Parameters
    ----------
    argv : Optional[List[str]], optional
        The list of arguments to be passed in the command-line, by default sys.argv[1:]
    """
    app = Application()
    app.run(argv)

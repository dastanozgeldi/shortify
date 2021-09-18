from enum import Enum
from importlib import import_module
from typing import Optional

import typer

app = typer.Typer(
    epilog="Type shortify [command] --help to get help for a specific command."
)


class Service(str, Enum):
    tinyurl = "tinyurl"
    git = "git"
    shrtcode = "shrtcode"
    isgd = "isgd"
    clck = "clck"
    tinyuid = "tinyuid"
    cleanuri = "cleanuri"


@app.command(help="Shorten any URL with this command.")
def shorten(service: Service, url: str) -> None:
    mod = import_module("shortify.services." + service)
    typer.secho(mod.Shortener().shorten(url), color=typer.colors.CYAN)


@app.command(help="Get an example on how to use Shortify's features.")
def example(service: Optional[Service] = Service.tinyurl) -> None:
    import requests
    # Fetching a random URL for an example.
    resp = requests.get(
        "https://random-data-api.com/api/internet_stuff/random_internet_stuff"
    )
    if resp.ok:
        typer.echo(f"shortify shorten {service} {resp.json()['url']}")


if __name__ == "__main__":
    app()

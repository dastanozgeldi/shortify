import argparse
import importlib


def parse_arguments() -> argparse.Namespace:
    """`shortify.parse_arguments` function, the place where all set args get passed.

    Later on we use this feature in `main` function, the core of the CLI.
    """
    choices = (
        'tinyurl',
        'git',
        'shrtcode',
        'isgd',
        'clck',
    )
    parser = argparse.ArgumentParser(
        'shortify',
        usage='shortify <service> <url to shorten>',
        description='Shortify CLI!',
    )
    parser.add_argument(
        'service', choices=choices, help='Provide a service you\'d like to use.'
    )
    parser.add_argument('url', help='Pass an URL to shorten.')

    return parser.parse_args()


def main() -> None:
    """The core of Shortify CLI.

    Here we handle all positional arguments the user provides.

    Then we shorenize the URL according to the parsed arguments.
    """
    args = parse_arguments()
    module = importlib.import_module('shortify.services.' + args.service)
    service = module.Shortener()
    print(service.shorten(args.url))


if __name__ == '__main__':
    main()

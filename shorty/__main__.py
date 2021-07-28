import argparse
import importlib


def get_arguments() -> argparse.Namespace:
    """`shorty.get_arguments` function, the place where all set args get passed.

    Later on we use this feature in `main` function, the core of the CLI.
    """
    choices = ('tinyurl', 'git', 'shrtcode', 'isgd', 'clck',)
    parser = argparse.ArgumentParser('shorty', description='Shorty CLI!')
    parser.add_argument(
        'service',
        default='tinyurl',
        choices=choices,
        help='Provide a service you\'d like to use.'
    )
    parser.add_argument(
        'url',
        help='Pass an URL to shorten.'
    )

    return parser.parse_args()


def main() -> None:
    """The core of Shorty CLI.

    Here we handle all positional arguments the user provides.

    Then we shorenize the URL according to the parsed arguments.
    """
    args = get_arguments()
    module = importlib.import_module('shorty.services.' + args.service)
    service = module.Shortener()
    print(service.shorten(args.url))


if __name__ == '__main__':
    main()

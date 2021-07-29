from shortify.services.git import Shortener


def main():
    """Imagine this is a CLI you are using Shortify in.

    This is the core method that does the user-terminal stuff.
    """
    sh = Shortener()
    url = sh.shorten('https://www.github.com/Dositan/passman', custom_code='passman')
    print(url)


if __name__ == '__main__':
    main()

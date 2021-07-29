from shortify.services.tinyurl import Shortener


def main():
    """Imagine this is a CLI you are using Shortify in.

    This is the core method that does the user-terminal stuff.
    """
    sh = Shortener()
    url = sh.shorten('http://www.github.com/Dositan/Boribay')
    print(url)


if __name__ == '__main__':
    main()

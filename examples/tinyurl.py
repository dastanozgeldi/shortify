from shorty.services import TinyURL


def main():
    """Imagine this is a CLI you are using Shorty in.

    This is the core method that does the user-terminal stuff.
    """
    t = TinyURL()
    url = t.shorten('http://www.github.com/Dositan/Boribay')
    print(url)


if __name__ == '__main__':
    main()

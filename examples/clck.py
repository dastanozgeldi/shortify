from shorty.services.clck import Shortener


def main():
    """Imagine this is a CLI you are using Shorty in.

    This is the core method that does the user-terminal stuff.
    """
    sh = Shortener()
    url = sh.shorten('http://www.github.com/Dositan/passman')
    print(url)


if __name__ == '__main__':
    main()

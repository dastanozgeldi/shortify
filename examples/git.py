from shorty.services import Git


def main():
    """Imagine this is a CLI you are using Shorty in.

    This is the core method that does the user-terminal stuff.
    """
    g = Git()
    url = g.shorten('https://www.github.com/Dositan/passman', custom_code='passman')
    print(url)


if __name__ == '__main__':
    main()

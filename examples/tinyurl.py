from shorty.services import TinyURL


def main():
    t = TinyURL()
    url = t.short('http://www.github.com/Dositan/Boribay')
    print(url)


if __name__ == '__main__':
    main()

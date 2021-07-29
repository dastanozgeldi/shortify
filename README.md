<h1 align="center">
    Shortify - shorten your URL
</h1>

A simple URL shortening API wrapper library written in Python by Dositan.

## Supported services
1. [TinyURL](https://tinyurl.com)
2. [Git.io](https://git.io)
3. [Shrtco.de](https://shrtco.de)
4. [Is.gd](is.gd)
5. [Clck.ru](clck.ru)

-----

## Installing
```console
$ pip install shortify

---> 100%
```

After pressing enter, pip will install all the required packages for the project.

</div>

-----

## CLI usage
Like all CLIs, `shortify` supports `--help` flag.
```console
$ shortify --help

usage: shortify [-h] {tinyurl,git} url

Shortify CLI!

.....
```

Generating a shortened URL using git.io:
```console
$ shortify git https://www.github.com/Dositan/Boribay/

https://git.io/JBsPu
```

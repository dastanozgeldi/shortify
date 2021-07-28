<h1 align="center">
    Shorty - shorten your URL
</h1>

A simple URL shortening API wrapper library written in Python by Dositan.

## Supported services
1. [TinyURL](https://tinyurl.com)
2. [Git.io](https://git.io)

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
Like all CLIs, `shorty` supports `--help` flag.
```console
$ shorty --help

usage: shorty [-h] {tinyurl,git} url

Shorty CLI!

.....
```

Generating a shortened URL using git.io:
```console
$ shorty git https://www.github.com/Dositan/Boribay/

https://git.io/JBsPu
```

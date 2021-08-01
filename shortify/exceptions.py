
__all__ = ('InvalidURL', 'ShorteningError', 'ExpandingError',)


class ShortifyError(Exception):
    """The base class for all Shortify exceptions.

    Any other exceptions should likely inherit from this class.
    """


class InvalidURL(ShortifyError):
    """Raised when the given URL fails regular-expression check."""

    def __init__(self, url: str) -> None:
        super().__init__(f'The URL "{url}" is invalid.')


class ShorteningError(ShortifyError):
    """Raised when the shortening from one service (e.g TinyURL) fails."""

    def __init__(self, url: str) -> None:
        super().__init__(f'Unexpected problem occurred on trying to shorten this URL: {url}')


class ExpandingError(ShortifyError):
    """Raised when the expanding from one service (e.g TinyURL) fails."""

    def __init__(self, url: str) -> None:
        super().__init__(f'Unexpected problem occurred on trying to expand this URL: {url}')


class ShortyError(Exception):
    """The base class for all Shorty exceptions.

    Any other exceptions should likely inherit from this class.
    """


class InvalidURL(ShortyError):
    """Raised when the given URL fails regular-expression check."""

    def __init__(self, url: str) -> None:
        super().__init__(f'The URL "{url}" is invalid.')


class ShorteningError(ShortyError):
    """Raised when the shortening from one service (e.g TinyURL) fails."""

    def __init__(self, url: str) -> None:
        super().__init__(f'Unexpected problem occurred on trying to shorten this URL: {url}')


class ExpandingError(ShortyError):
    """Raised when the expanding from one service (e.g TinyURL) fails."""

    def __init__(self, url: str) -> None:
        super().__init__(f'Unexpected problem occurred on trying to expand this URL: {url}')

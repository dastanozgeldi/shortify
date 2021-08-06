from shortify.abc import ShortifyBase
from shortify.exceptions import ShorteningError


class Shortener(ShortifyBase):
    """TinyUID.com shortener.

    This class inherits from `shortify.base.ShortifyBase`.
    """

    def shorten(self, url: str) -> str:
        response = self.post(
            "https://tinyuid.com/api/v1/shorten", data={"url": self.sanitize_url(url)}
        )
        if response.ok:
            return response.json()['result_url']

        raise ShorteningError(response.content)

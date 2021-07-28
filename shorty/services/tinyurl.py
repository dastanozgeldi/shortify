from ..base import ShortyBase
from ..errors import ShorteningError


class Shortener(ShortyBase):
    """TinyURL shortener.

    This class inherits from `shorty.base.ShortyBase`.
    """

    def shorten(self, url: str) -> str:
        """Shorten function.

        Parameters
        ----------
        url : str
            The URL you need to shorten.

        Returns
        -------
        str
            The shortened URL.

        Raises
        ------
        ShorteningError
            If the response status was not around 200 (not ok).
        """
        response = self.get(
            'https://tinyurl.com/api-create.php',
            params={'url': self.sanitize_url(url)}
        )
        if response.ok:
            return response.text.strip()

        raise ShorteningError(response.content)

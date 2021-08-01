from ..abc import ShortifyBase
from ..exceptions import ShorteningError


class Shortener(ShortifyBase):
    """Is.gd shortener.

    This class inherits from `shortify.base.ShortifyBase`.
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
            'https://is.gd/create.php',
            params={'url': self.sanitize_url(url), 'format': 'simple'}
        )
        if response.ok:
            return response.text.strip()

        raise ShorteningError(response.content)

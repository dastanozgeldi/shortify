from typing import Optional

from ..base import ShortyBase
from ..errors import ShorteningError


class Shortener(ShortyBase):
    """Git.io URL shortener.

    Notice that this works only for `GitHub` URLs.

    This class inherits from `shorty.base.ShortyBase`.
    """

    def shorten(self, url: str, *, custom_code: Optional[str] = None) -> str:
        """Works only with GitHub URLs.

        Parameters
        ----------
        url : str
            The URL you need to shorten.
        custom_code : Optional[str], optional
            Custom permalink code (e.g shorty), by default None

        Returns
        -------
        str
            The shortened URL.

        Raises
        ------
        ShorteningError
            If the response status was not around 200 (not ok).
        """
        response = self.post(
            'https://git.io',
            data={'url': self.sanitize_url(url), 'code': custom_code}
        )
        if not response.ok or not response.headers.get('Location'):
            raise ShorteningError(response.content)

        return response.headers['Location']

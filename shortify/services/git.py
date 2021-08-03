from typing import Optional

from ..abc import ShortifyBase
from ..exceptions import ShorteningError


class Shortener(ShortifyBase):
    """Git.io URL shortener.

    Notice that this works only for `GitHub` URLs.

    This class inherits from `shortify.base.ShortifyBase`.
    """

    def shorten(self, url: str, *, custom_code: Optional[str] = None) -> str:
        """Works only with GitHub URLs.

        Parameters
        ----------
        url : str
            The URL you need to shorten.
        custom_code : Optional[str], optional
            Custom permalink code (e.g shortify), by default None

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
            "https://git.io", data={"url": self.sanitize_url(url), "code": custom_code}
        )
        if not response.ok or not response.headers.get("Location"):
            raise ShorteningError(response.content)

        return response.headers["Location"]

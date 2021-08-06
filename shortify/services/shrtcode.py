from shortify.abc import ShortifyBase
from shortify.exceptions import ShorteningError


class Shortener(ShortifyBase):
    """Shrtco.de shortener.

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
        print("This API may work slow, please consider waiting!\n")

        response = self.get("https://api.shrtco.de/v2/shorten", params={"url": url})
        if response.ok:
            result = response.json()["result"]
            return "\n".join(
                result[res] for res in result if res.startswith("full_short_link")
            )

        raise ShorteningError(response.content)

import re
from typing import Any, Dict

import requests

from .exceptions import ExpandingError, InvalidURL

__all__ = ('ShortifyBase',)

URL_REGEX = re.compile(
    r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.]'
    r'[a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)'
    r'))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()'
    r'\[\]{};:\'".,<>?«»“”‘’]))'
)


class ShortifyBase:
    """ShortifyBase - the base class for all subclass-shorteners.

    There is an idea of making a class per one popular URL-shortening service.

    Parameters
    ----------
    timeout : float, optional
        The timeout amount for the library to wait.
    verify : bool, optional
        Whether to make an SSL verification.
    proxies : dict, optional
        Web-proxy configuration for making requests.
    cert : optional
        The custom client-side certificate.

    Example
    -------
    >>> class MyShortener(ShortifyBase):
    ...     def short(self, url: str) -> str:
    ...         # shortener code may differ from the example below,
    ...         # this is API-specific.
    ...         response = self.get(
    ...            'http://api.formyshortener.xyz/v69',
    ...            params={'url': self.sanitize_url(url)}
    ...        )
    ...        if response.ok:
    ...            return response.text.strip()
    ...        # Response status is not ok (does not equal 200).
    ...        raise ShorteningError(response.content)
    """

    def __init__(self, **kwargs: Any) -> None:
        self.timeout = kwargs.pop('timeout', 60.0)
        self.verify = kwargs.pop('verify', True)
        self.proxies = kwargs.pop('proxies', {})
        self.cert = kwargs.pop('cert', None)

    @staticmethod
    def sanitize_url(url: str) -> str:
        """The method that discovers a URL beforehand through regular expression.

        Parameters
        ----------
        url : str
            A URL to clear up.

        Returns
        -------
        str
            The sanitized URL.

        Raises
        ------
        InvalidURL
            If the URL fails the regular expression check.
        """
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        if not URL_REGEX.match(url):
            raise InvalidURL(url)

        return url

    def get(
        self,
        url: str,
        params: Dict[str, Any] = None,
        headers: Dict[str, Any] = None
    ) -> requests.Response:
        """The get method which is just `requests.get` with extra kwargs passed in.

        Parameters
        ----------
        url : str
            A URL that should be shortened.
        params : Dict[str, Any], optional
            A dictionary of parameters to pass in, by default None
        headers : Dict[str, Any], optional
            A dictionary of headers to pass in, by default None

        Returns
        -------
        requests.Response
            A response object we use in the shortening process.
        """
        return requests.get(
            url=self.sanitize_url(url),
            params=params,
            verify=self.verify,
            timeout=self.timeout,
            headers=headers,
            proxies=self.proxies,
            cert=self.cert,
        )

    def post(
        self,
        url: str,
        data: Dict[str, str] = None,
        json: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        headers: Dict[str, Any] = None
    ) -> requests.Response:
        """The post method which is just `requests.post` with extra kwargs passed in.

        Parameters
        ----------
        url : str
            A URL that should be shortened.
        data : Dict[str, str], optional
            The data to pass in manually, by default None
        json : Dict[str, Any], optional
            JSON data to send in the body of the request, by default None
        params : Dict[str, Any], optional
            A dictionary of parameters to pass in, by default None
        headers : Dict[str, Any], optional
            A dictionary of headers to pass in, by default None

        Returns
        -------
        requests.Response
            A response object we use in the shortening process.
        """
        return requests.post(
            url=self.sanitize_url(url),
            data=data,
            json=json,
            params=params,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify,
            proxies=self.proxies,
            cert=self.cert,
        )

    def shorten(self, url: str) -> str:
        """The key-method that must be overridden by child classes."""
        raise NotImplementedError

    def expand(self, url: str) -> str:
        """Expand a URL using specific services.

        Parameters
        ----------
        url : str
            A URL to shorten.

        Returns
        -------
        str
            The expanded URL.

        Raises
        ------
        ExpandingError
            If the URL fails on expanding.
        """
        resp = self.get(self.sanitize_url(url))
        if resp.ok:
            return resp.url

        raise ExpandingError(url)

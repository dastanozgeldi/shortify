import re
from typing import Any, Dict

import requests

from .errors import ExpandingError, InvalidURL

URL_REGEX = re.compile(
    r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.]"
    r"[a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)"
    r"))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()"
    r'\[\]{};:\'".,<>?«»“”‘’]))'
)


class ShortyBase:
    def __init__(self, **kwargs: Any) -> None:
        self.timeout = kwargs.pop('timeout', 5.0)
        self.verify = kwargs.pop('verify', True)
        self.proxies = kwargs.pop('proxies', {})
        self.cert = kwargs.pop('cert', None)

    @staticmethod
    def sanitize_url(url: str) -> str:
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

    def short(self, url: str) -> str:
        raise NotImplementedError

    def expand(self, url: str) -> str:
        response = self.get(self.sanitize_url(url))
        if response.ok:
            return response.url

        raise ExpandingError(url)

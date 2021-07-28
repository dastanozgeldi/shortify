from typing import Optional

from ..base import ShortyBase
from ..errors import ShorteningError


class Git(ShortyBase):
    def shorten(self, url: str, *, custom_code: Optional[str] = None) -> str:
        response = self.post(
            'https://git.io',
            data={'url': self.sanitize_url(url), 'code': custom_code}
        )
        if not response.ok or not response.headers.get('Location'):
            raise ShorteningError(response.content)

        return response.headers['Location']

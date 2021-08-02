"""
Shortify
========
A library created for users who quickly want to shorten their really-long-urls up.

There are several services supported, so if you find one not suiting your purposes,
you can always use another API.
"""
import logging
from typing import Literal, NamedTuple

__title__ = 'shortify'
__author__ = 'Dositan'
__license__ = 'MIT'
__copyright__ = f'Copyright 2021 {__author__}'
__version__ = '0.4.5'


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final']
    serial: int


version_info = VersionInfo(major=0, minor=4, micro=5, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

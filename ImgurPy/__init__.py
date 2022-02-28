from .Account import Account
from .Album import Album
from .Authenticate import Authenticate
from .Image import Image
from .imgurPy import ImgurPy
from .core import Core

__all__ = ['Account', 'Album', 'Authenticate', 'Image', 'ImgurPy', 'Core']

Authenticate.__module__ = 'ImgurPy'
Core.__module__ = 'ImgurPy'
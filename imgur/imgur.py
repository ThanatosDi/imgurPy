from .Account import Account
from .Album import Album


class ImgurAPI(Account, Album):
    API = 'https://api.imgur.com'
    __version__ = '0.0.1'

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str = None
    ):
        Account.__init__(self, client_id, client_secret,
                         refresh_token, self.API)
        Album.__init__(self, client_id, client_secret,
                       refresh_token, self.API)
        self.__access_token = None

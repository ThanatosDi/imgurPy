from .Authenticate import Authenticate


class Album(Authenticate):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        API: str,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.API = API
        self.__access_token = None
        Authenticate.__init__(
            self, client_id, client_secret, refresh_token, API)

    def Auth(func):
        def warp(self, *args, **kwargs):
            self.__access_token = self.access_token
            return func(self, *args, **kwargs)
        return warp

    def Album(self, albumHash: str) -> dict:
        endpoint = f'{self.API}/3/album/{albumHash}'
        headers = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        response = self.make_request(
            'get',
            endpoint,
            headers=headers
        ).json()
        return response

    def AlbumImages(self, albumHash: str) -> dict:
        endpoint = f'{self.API}/3/album/{albumHash}/images'
        headers = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        response = self.make_request(
            'get',
            endpoint,
            headers=headers
        ).json()
        return response

    def AlbumImage(self, albumHash: str, imageHash:str) -> dict:
        endpoint = f'{self.API}/3/album/{albumHash}/images/{imageHash}'
        headers = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        response = self.make_request(
            'get',
            endpoint,
            headers=headers
        ).json()
        return response

    
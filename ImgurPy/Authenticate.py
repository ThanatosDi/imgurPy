from .core import Core


class Authenticate(Core):
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

    def Auth(func):
        def warp(self, *args, **kwargs):
            self.__access_token = self.access_token
            return func(self, *args, **kwargs)
        return warp

    @property
    def OAuth2(self):
        return f'{self.API}/oauth2/authorize?client_id={self.client_id}&response_type=token'

    @property
    def access_token(self):
        response = self.GenerateAccessToken()
        self.__access_token = response['access_token']
        return self.__access_token

    def GenerateAccessToken(self) -> dict:
        """Given a user's refresh token, this endpoint generates an access token.

        Returns:
            dict
        """
        endpoint = f'{self.API}/oauth2/token'
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token',
        }
        response = self.make_request(
            "post",
            endpoint,
            data=payload
        ).json()
        return response

    def Auth(func):
        def warp(self):
            self.access_token
            func()
        return warp
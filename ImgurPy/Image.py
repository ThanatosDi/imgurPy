from .Authenticate import Authenticate
from typing import Union


class Image(Authenticate):
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

    def ImageUpload(
            self,
            file: Union[str, bytes] = None,
            type: str = 'file', **kwargs
    ) -> dict:
        """Upload a new image or video.

        Args:
            file (Union[str, bytes], optional): file path, file bytes or file url. Defaults to None.
            type (str, optional): file, base64 or url. Defaults to 'file'.  
            album (str, optional): upload image to the album. Defaults to None.
            name (str, optional): image file name.
            title (str, optional): image title.
            description (str, optional): image description.
            auth (bool, optional): if upload to hidden album, need to set True of auth. Default to False.
        """
        endpoint = f'{self.API}/3/upload'
        headers = {'Authorization': f'Client-ID {self.client_id}'}
        payload = {
            'type': type
        }

        (headers.update({'Authorization': f'Bearer {self.access_token}'})
            if kwargs.get('auth', False) == True else ...)

        params = ['album', 'name', 'title', 'description']
        for param in params:
            (payload.update({param: kwargs.get(param, '')})
                if kwargs.get(param, '') != '' else ...)

        (payload.update({'image': file})
            if type == 'url' or isinstance(file, str) else ...)

        response = self.make_request(
            'post',
            endpoint,
            headers=headers,
            data=payload
        ).json()
        return response

    def ImageDelete(
        self,
        imageHash: str,
        auth: bool = False
    ):
        """Deletes an image.

        Args:
            imageHash (str): _description_
            auth (bool, optional): _description_. Defaults to False.
        """
        endpoint = f'{self.API}/3/image/{imageHash}'
        headers = {'Authorization': f'Client-ID {self.client_id}'}
        (headers.update({'Authorization': f'Bearer {self.access_token}'})
            if auth == True else ...)

        response = self.make_request(
            'delete',
            endpoint,
            headers=headers,
        ).json()
        return response

    def ImageUpdate(
        self,
        imageHash: str,
        auth: bool = False,
        **kwargs
    ):
        """Updates the title or description of an image.

        Args:
            imageHash (str): _description_
            auth (bool, optional): _description_. Defaults to False.
        """
        endpoint = f'{self.API}/3/image/{imageHash}'
        headers = {'Authorization': f'Client-ID {self.client_id}'}
        params = ['title', 'description']
        payload = {}
        (headers.update({'Authorization': f'Bearer {self.access_token}'})
            if auth == True else ...)
        for param in params:
            (payload.update({param: kwargs.get(param, '')})
                if kwargs.get(param, '') != '' else ...)
        response = self.make_request(
            'post',
            endpoint,
            headers=headers,
            data=payload,
        ).json()
        return response

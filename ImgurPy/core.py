import requests


class Core(object):
    def make_request(
        self,
        method: str,
        url: str,
        *args,
        **kwargs
    ):

        response = requests.request(
            method.upper(),
            url,
            *args,
            **kwargs
        )
        return response

    
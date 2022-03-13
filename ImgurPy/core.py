import requests
import aiohttp


class Core(object):

    def wrapping_response_instance(
        self, 
        aiohttp_response:aiohttp.ClientResponse, 
        content:bytes
    ) -> requests.Response:
        """wrap response from aiohttp to requests

        Args:
            aiohttp_response (aiohttp.ClientResponse): _description_
            content (bytes): _description_

        Returns:
            requests.Response: Response of requests
        """        
        # https://stackoverflow.com/questions/57565577/how-to-return-aiohttp-like-python-requests
        response = requests.Response()
        response._content = content
        response.url = str(aiohttp_response.url)
        response.status_code = aiohttp_response.status
        headers = {row[0]: row[1] for row in aiohttp_response.headers.items()}
        response.headers = headers
        return response

    async def make_request(
        self,
        method: str,
        url: str,
        *args,
        **kwargs
    ) -> requests.Response:
        """Make a request

        Args:
            method (str): request method.
            url (str): request url.

        Returns:
            requests.Response: response of request.
        """
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, *args, **kwargs) as response:
                content, _ = await response.content.readchunk()
                return self.wrapping_response_instance(response, content)

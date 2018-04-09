import requests


class HTTPClient:
    """The HTTP client, define the basics http methods"""

    def __init__(self, username=None, password=None, base_url=None):
        self._username = username
        self._password = password
        self._base_url = base_url

    def get(self, path):
        url = f"{self._base_url}{path}"
        result = requests.get(url=url, auth=(self._username, self._password))
        return result.json()

    def post(self, path, data):
        url = f"{self._base_url}{path}"
        result = requests.post(
            url=url,
            json=data,
            auth=(self._username, self._password)
        )
        return result.json()

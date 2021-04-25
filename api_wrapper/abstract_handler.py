import requests


class AbstractHandler:

    api_key: str

    url_link: str

    def __init__(self, new_api_key):
        self.api_key = new_api_key
        self.url_link += f'apikey={self.api_key}'

    def getByUrl(self, url: str) -> requests.Response:
        return requests.get(
            url,
            headers={"Content-Type": "text/html", "charset": "utf-8"}
        )

    def buildUrl(self, params: dict = None) -> str:
        if params:
            return self.url_link + '&' + '&'.join(self.buildParams(params))
        else:
            return self.url_link

    def buildParams(self, params: dict) -> list:
        query_params = []
        for param in params:
            query_params.append(param + '=' + params[param])
        return query_params

import requests

from configs.yandex import *


class HandlerFactory:

    @staticmethod
    def getSVOHandler():
        return StationHandler(
            api_key,
            station,
            system
        )


class StationHandler:

    api_key: str
    station: str
    system: str
    TRANSPORT_PLANE: str = 'plane'

    url_link = f'https://api.rasp.yandex.net/v3.0/schedule/?'

    def __init__(self, new_api_key, new_station, new_system):
        self.api_key = new_api_key
        self.station = new_station
        self.system = new_system
        self.url_link += f'apikey={self.api_key}' \
                         f'&station={self.station}' \
                         f'&system={self.system}'

    def getPlanes(self) -> requests.Response:
        params = {'transport_types': self.TRANSPORT_PLANE}
        return self.getByUrl(
            self.buildUrl(params)
        )

    def getPlanesSchedule(self) -> dict:
        data = self.getPlanes().json()
        return data['schedule']

    def getByUrl(self, url: str) -> requests.Response:
        return requests.get(
            url,
            headers={"Content-Type": "text/html", "charset": "utf-8"}
        )

    def buildUrl(self, params: dict) -> str:
        url = self.url_link + '&' + '&'.join(self.buildParams(params))
        return url

    def buildParams(self, params: dict) -> list:
        query_params = []
        for param in params:
            query_params.append(param + '=' + params[param])
        return query_params

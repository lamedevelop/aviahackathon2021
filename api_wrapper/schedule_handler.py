import requests

from api_wrapper.abstract_handler import AbstractHandler


class BasicPlaneScheduleHandler(AbstractHandler):

    station: str
    TRANSPORT_PLANE: str = 'plane'

    url_link = f'https://api.rasp.yandex.net/v3.0/schedule/?'

    def __init__(self, new_api_key, new_station):
        super().__init__(new_api_key)
        self.station = new_station
        self.url_link += f'&station={self.station}'

    def getPlanes(self) -> requests.Response:
        params = {'transport_types': self.TRANSPORT_PLANE}
        return self.getByUrl(
            self.buildUrl(params)
        )

    def getPlanesSchedule(self) -> dict:
        data = self.getPlanes().json()
        return data['schedule']


class PlaneScheduleHandler(BasicPlaneScheduleHandler):

    system: str

    def __init__(self, new_api_key, new_station, new_system):
        super().__init__(new_api_key, new_station)
        self.system = new_system
        self.url_link += f'&system={self.system}'

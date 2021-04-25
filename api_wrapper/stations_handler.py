from api_wrapper.abstract_handler import AbstractHandler


class StationsHandler(AbstractHandler):

    url_link = f'https://api.rasp.yandex.net/v3.0/stations_list/?'

    def getAllStations(self) -> dict:
        return self.getByUrl(self.buildUrl()).json()

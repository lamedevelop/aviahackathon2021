from api_wrapper.abstract_handler import AbstractHandler


class RouteHandler(AbstractHandler):

    from_code: str
    to_code: str
    system: str

    url_link = f'https://api.rasp.yandex.net/v3.0/search/?'

    def __init__(self, new_api_key, from_code, to_code, system):
        super().__init__(new_api_key)
        self.from_code = from_code
        self.to_code = to_code
        self.system = system
        self.url_link += f'&from={self.from_code}' \
                         f'&to={self.to_code}' \
                         f'&system={self.system}'

    def getAllTrips(self) -> dict:
        return self.getByUrl(self.buildUrl()).json()

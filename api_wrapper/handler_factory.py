from configs.yandex import *

from api_wrapper.dummy_handler import DummyHandler
from api_wrapper.route_handler import RouteHandler
from api_wrapper.stations_handler import StationsHandler
from api_wrapper.schedule_handler import PlaneScheduleHandler, BasicPlaneScheduleHandler


class HandlerFactory:

    @staticmethod
    def getDummyHandler():
        return DummyHandler()

    @staticmethod
    def getBasicSVOHandler():
        return BasicPlaneScheduleHandler(
            api_key,
            station
        )

    @staticmethod
    def getSVOHandler():
        return PlaneScheduleHandler(
            api_key,
            station,
            system
        )

    @staticmethod
    def getStationsHandler():
        return StationsHandler(
            api_key
        )

    @staticmethod
    def getRouteHandler():
        return RouteHandler(
            api_key,
            station,
            'AER',
            system
        )

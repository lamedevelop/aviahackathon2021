import pytest

from yandex_api_handler.api_handler import HandlerFactory


@pytest.fixture
def handler():
    return HandlerFactory.getSVOHandler()


def test_svo_handler_station(handler):
    assert handler.station == 'SVO'


def test_svo_handler_system(handler):
    assert handler.system == 'iata'

import pytest

from api_wrapper.handler_factory import HandlerFactory


@pytest.fixture
def handler():
    return HandlerFactory.getSVOHandler()


def test_svo_handler_station(handler):
    assert handler.station == 'SVO'


def test_svo_handler_system(handler):
    assert handler.system == 'iata'

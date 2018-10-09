import pytest
from sanic.websocket import WebSocketProtocol
from erasto_blaster import app as erasto_app
from erasto_sieve import erasto_sieve, some_example_primes
import time


@pytest.yield_fixture
def app():
    yield erasto_app


@pytest.fixture
def socket_fixture(app, loop, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))


async def test_erasto_socket(socket_fixture):
    websocket = await socket_fixture.ws_connect("/primes")
    for expected_prime in some_example_primes:
        prime_string = await websocket.receive_str()

        print(f"test_erasto_socket recieved prime: {prime_string}")

        assert int(prime_string) == expected_prime

        await websocket.send_str("okay!")

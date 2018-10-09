import pytest
from sanic.websocket import WebSocketProtocol
from erasto_blaster import app as erasto_app
from erasto_sieve import some_example_primes


@pytest.yield_fixture
def app():
    yield erasto_app


@pytest.fixture
def socket_fixture(app, loop, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))


async def test_erasto_socket(socket_fixture):
    """ erasto_blaster yields the first six prime numbers via websocket """
    websocket = await socket_fixture.ws_connect("/primes")
    text_response = "okay!"
    for expected_prime in some_example_primes:
        prime_string = await websocket.receive_str()

        print(f"test_erasto_socket recieved prime: {prime_string}")
        assert int(prime_string) == expected_prime

        print(f"test_erasto_socket sending response: {text_response}")
        await websocket.send_str(text_response)

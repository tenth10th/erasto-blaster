from sanic import Sanic
from sanic.response import json
from erasto_sieve import erasto_sieve

app = Sanic(__name__)


@app.websocket("/primes")
async def erasto_blaster(request, ws):
    prime_generator = erasto_sieve()

    for next_prime in prime_generator:

        print(f"erasto_blaster sending Prime: {next_prime}")

        await ws.send(str(next_prime))

        incoming_data = await ws.recv()

        print(f"erasto_blaster recieved response: {incoming_data}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

from sanic import Sanic
from erasto_sieve import erasto_sieve

app = Sanic(__name__)


@app.websocket("/primes")
async def erasto_blaster(request, websocket):
    prime_generator = erasto_sieve()

    for next_prime in prime_generator:

        print(f"erasto_blaster sending Prime: {next_prime}")

        await websocket.send(str(next_prime))

        incoming_data = await websocket.recv()

        print(f"erasto_blaster recieved response: {incoming_data}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

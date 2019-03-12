# Erasto-Blaster

A simple [Sanic](https://github.com/huge-success/sanic) demo app that serves Prime Numbers over a websocket, with (py)tests.

I get the impression that Sanic is not Windows-friendly because of [uvloop](https://uvloop.readthedocs.io/), but this app should be useable under MacOS or Linux (where Python 3.6+ is available).

To install via [pipenv](https://pipenv.readthedocs.io/en/latest/), clone this repo, cd into the folder, and run:
```
pipenv install --dev
```

Or more generally via [pip](https://pypi.org/project/pip/) (ideally in a virtualenv):
```
pip install -r dev-requirements.txt
```
(Dev includes some requirements you may not want or need, like [flake8](https://pypi.org/project/flake8/) and [black](https://pypi.org/project/black/), but is necessary to run the tests below.)

You can then run the erasto_blaster server directly:
```
python erasto_blaster.py
```

Though a better proof of concept is to run the tests, in verbose mode, not swallowing output (so that you can see the async websocket test in action):
```
pytest -vs
```

This is a very simple proof of concept (and my first Sanic app) - A real prime number service would have more performance considerations, yield a unique stream of primes per user, and maybe not exist at all (because the entire premise is silly).

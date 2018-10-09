# Erasto-Blaster

A simple Sanic demo app that serves Prime Numbers over a websocket, with (py)tests.

Sanic is not Windows-friendly because of UVLoop, but this app should be useable under MacOS or Linux (where Python 3.6 is available).

To install via Pipenv, clone this repo, cd into the folder, and run:
```
pipenv install --dev
```

Or more generally via Pip (ideally in a virtualenv):
```
pip install -r dev-requirements.txt
```
(Dev includes some requirements you may not want or need, like flake8 and black, but is necessary to run the tests below.)

You can then run the erasto_blaster server directly:
```
python erasto_blaster.py
```

Though a better proof of concept is to run the tests, in verbose mode, not swallowing output (so that you can see the asyc websocket test in action):
```
pytest -vs
```

This is a very simple proof of concept (and my first Sanic app) - A real prime number service would have more performance considerations, yield a unique stream of primes per user, and maybe not exist at all (because the entire premise is silly).

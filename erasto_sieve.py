some_example_primes = (2, 3, 5, 7, 11, 13)


def erasto_sieve():
    """
    Prime number generator (using the Sieve of Erastothenes)

    Adapted from my favorite StackOverflow implementations; This isn't really
    the interesting part of the app, just something to serve over a websocket.
    """
    divisors = dict()
    current_integer = 2

    while True:
        if current_integer not in divisors:
            yield current_integer
            divisors[current_integer * current_integer] = [current_integer]
        else:
            for d in divisors[current_integer]:
                divisors.setdefault(d + current_integer, []).append(d)

            del divisors[current_integer]

        current_integer += 1

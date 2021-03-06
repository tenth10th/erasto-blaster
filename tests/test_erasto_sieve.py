from erasto_sieve import erasto_sieve, some_example_primes


def test_erasto_sieve():
    """ erasto_sieve returns the first six prime numbers """
    prime_generator = erasto_sieve()
    for expected_prime in some_example_primes:
        assert next(prime_generator) == expected_prime

import math


def f(a: int, n: int) -> None:
    """Attempt to find a non-trivial factor of ``n`` using Pollard's p-1 method.

    Prints the exponent ``i`` and a factor of ``n`` if found.
    This is a minimal illustrative implementation.
    """
    for i in range(1, 20):
        a = pow(a, i, n)
        if a == 1:
            print("Pick new a")
            continue
        d = math.gcd(a - 1, n)
        if 1 < d < n:
            print(i, d)


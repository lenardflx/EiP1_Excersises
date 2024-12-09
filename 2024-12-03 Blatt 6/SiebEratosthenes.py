def iter_get_primes(n: int) -> list:
    primes, state = [], [True]*n
    for i in range(2,n):
        if state[i]:
            primes.append(i)
            for j in range(i*2,n,i):
                state[j] = False
    return primes

def semi_rec_get_primes(n: int) -> list:
    def rec(primes, state, current):
        if current >= n:
            return primes
        if state[current]:
            primes.append(current)
            for j in range(current*2, n, current):
                state[j] = False
        return rec(primes, state, current + 1)
    return rec([], [True]*n, 2)

def rec_get_primes(n: int) -> list:
    def rm_multiples(state, nbr, current):
        if current >= n:
            return
        state[current] = False
        rm_multiples(state, nbr, current + nbr)
    def rec(primes, state, current):
        if current >= n:
            return primes
        if state[current]:
            primes.append(current)
            rm_multiples(state, current, current*2)
        return rec(primes, state, current + 1)
    return rec([], [True]*n, 2)


# Ist n keine Primzahl, so hat n einen Teiler a mit a <= sqrt(n)
def simple_get_primes(n: int) -> list:
    return [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

# Tests
n = 100
res = [f(n) for f in [iter_get_primes, semi_rec_get_primes, rec_get_primes, simple_get_primes]]
print("\n".join(f"Primzahlen {i}) bis {n}: {p}" for i, p in enumerate(res, 1)))
print(f"Alle Identisch?: {all(p == res[0] for p in res)}")

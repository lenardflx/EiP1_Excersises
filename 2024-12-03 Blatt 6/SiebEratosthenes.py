def iter_get_primes(n: int) -> list:
    primes, state = [], [True]*n
    for i in range(2,n):
        if state[i]:
            primes.append(i)
            for j in range(i**2, n, i):
                state[j] = False
    return primes

def semi_rec_get_primes(n: int) -> list:
    def rec(primes, current=0):
        if current >= len(primes) or primes[current] ** 2 > primes[-1]:
            return primes
        primes = [x for x in primes if x == primes[current] or x % primes[current] != 0]
        return rec(primes, current + 1)
    return rec(list(range(2, n+1)))

def rec_get_primes(n: int) -> list:
    def rec(primes, current=0):
        if current >= len(primes) or primes[current] ** 2 > primes[-1]:
            return primes
        def rm_multiples(curr_primes: list, nbr: int) -> list:
            if not curr_primes:
                return []
            nxt = rm_multiples(curr_primes[1:], nbr)
            return [curr_primes[0]] + nxt if curr_primes[0] == nbr or curr_primes[0] % nbr != 0 else nxt
        return rec(rm_multiples(primes, primes[current]), current + 1)
    return rec(list(range(2, n+1)))

# Nach dem Prinzip: Ist n keine Primzahl, so hat n einen Teiler a mit a <= sqrt(n) (credits an Prof. de Jong)
def simple_get_primes(n: int) -> list:
    return [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

n = 100
res = [f(n) for f in [iter_get_primes, semi_rec_get_primes, rec_get_primes, simple_get_primes]]
print("\n".join(f"Primzahlen {i}) bis {n}: {p}" for i, p in enumerate(res, 1)))
print(f"Alle Identisch?: {all(p == res[0] for p in res)}")

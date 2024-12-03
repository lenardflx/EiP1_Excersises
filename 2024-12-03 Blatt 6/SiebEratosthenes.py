def iter_get_primes(n: int) -> list:
    primes = []
    state = [True] * n
    for i in range(2, n):
        if state[i]:
            primes.append(i)
            for j in range(i**2, n, i):
                state[j] = False
    return primes

def semi_rec_get_primes(primes: list, current: int = 0) -> list:
    if current >= len(primes) or primes[current] ** 2 > primes[-1]:
        return primes
    primes = [x for x in primes if x == primes[current] or x % primes[current] != 0]
    return semi_rec_get_primes(primes, current + 1)

def rec_get_primes(primes: list, current: int = 0) -> list:
    if current >= len(primes) or primes[current] ** 2 > primes[-1]:
        return primes
    def rm_multiples(curr_primes: list, nbr: int) -> list:
        if not curr_primes:
            return []
        nxt = rm_multiples(curr_primes[1:], nbr)
        return [curr_primes[0]] + nxt if curr_primes[0] == nbr or curr_primes[0] % nbr != 0 else nxt
    return rec_get_primes(rm_multiples(primes, primes[current]), current + 1)

# Nach dem Prinzip: Ist n keine Primzahl, so hat n einen Teiler a mit a <= sqrt(n) (credits an Prof. de Jong)
def simple_get_primes(n: int) -> list:
    return [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

n = 100
prime_res = [iter_get_primes(n), semi_rec_get_primes(list(range(2, n + 1))),
             rec_get_primes(list(range(2, n + 1))), simple_get_primes(n)]
print("\n".join(f"Primzahlen {i}) bis {n}: {p}" for i, p in enumerate(prime_res, 1)))
print(f"Alle Identisch?: {all(p == prime_res[0] for p in prime_res)}")

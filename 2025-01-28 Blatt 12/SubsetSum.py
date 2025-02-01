from time import time

def try_all(weights, max_weight):
    combinations = [[]]
    for wgt in weights:
        combinations += [c + [wgt] for c in combinations]
    return max([sum(c) for c in combinations if sum(c) <= max_weight])

def backtrack(weights, max_weight, curr=[]):
    if sum(curr) > max_weight: return 0
    res = [sum(curr)] + [backtrack(weights[i+1:], max_weight, curr + [weights[i]]) for i in range(len(weights))]
    return max(res)

def dyn_opt(weights, max_weight):
    memo = {}
    def OPT(j, v):
        if (j, v) in memo: return memo[(j, v)]
        if j < 0: return 0
        curr = weights[j]
        memo[(j, v)] = max(OPT(j-1,v), (curr+OPT(j-1,v-curr)) if v >= curr else 0)
        return memo[(j, v)]
    return OPT(len(weights) - 1, max_weight)

for func in [try_all, backtrack, dyn_opt]:
    start = time()
    weights, max_weight = [8, 15, 1, 14, 77, 13, 15, 21, 13], 96
    result = func(weights, max_weight)
    print(f"{func.__name__.ljust(9)} took {time() - start:.6f}s (Result: {result})")
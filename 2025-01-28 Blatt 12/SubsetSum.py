import time

def run_with_timing(func):
    start = time.time()
    weights = [8, 15, 1, 14, 77, 13, 15, 21, 13]
    max_weight = 93 # bei 1000 brauchen alle Funktionen ungefähr gleich lang, da jedes Element verwendet wird
    result = func(weights, max_weight)
    end = time.time()
    print(f"Function {func.__name__} took {end-start:2f} seconds")
    print(f"Result: {result}")

def try_all(weights, max_weight):
    combinations = [[]]
    for wgt in weights:
        combinations += [c + [wgt] for c in combinations]
    biggest = 0
    for combination in combinations:
        if max_weight >= sum(combination) > biggest:
            biggest = sum(combination)
    return biggest

def backtracking(weights, max_weight, index=0, current_sum=0):
    if index == len(weights):
        return current_sum
    include = 0
    if current_sum + weights[index] <= max_weight:
        include = backtracking(weights, max_weight, index + 1, current_sum + weights[index])
    exclude = backtracking(weights, max_weight, index + 1, current_sum)

    if include > exclude:
        return include
    return exclude

def dynamic_programming(weights, max_weight): # dasselbe wie backtracking?!?
    def OPT(j, v):
        if j < 0:
            return 0
        curr = weights[j]
        left = OPT(j - 1, v)
        right = 0 if v < curr else curr + OPT(j - 1, v - curr)
        return max(left, right)
    return OPT(len(weights) - 1, max_weight)

for func in [try_all, backtracking, dynamic_programming]:
    run_with_timing(func)
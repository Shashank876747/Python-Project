from itertools import product


def maximize_it(K, M, all_lists):
    all_combinations = product(*all_lists)
    max_value = 0
    for combo in all_combinations:
        value = sum(x**2 for x in combo) % M
        max_value = max(max_value, value)
    return max_value


if __name__ == "__main__":
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        elements = list(map(int, input().split()))
        # skip the first element which is the count Ni
        lists.append(elements[1:])
    print(maximize_it(K, M, lists))

def find_combinations(price, N, M, current_combination, current_category, current_cost, target_price, min_diff, memo):
    if current_category == N:
        diff = abs(current_cost - target_price)
        min_diff[0] = min(min_diff[0], diff)
        return

    if (current_category, current_cost) in memo:
        return

    for i in range(M):
        current_combination[current_category] = i
        new_cost = current_cost + price[current_category][i]
        find_combinations(price, N, M, current_combination, current_category + 1, new_cost, target_price, min_diff, memo)

    memo[(current_category, current_cost)] = True


def solution(N, M, K, price):
    current_combination = [0] * N
    min_diff = [float('inf')]
    memo = {}

    find_combinations(price, N, M, current_combination, 0, 0, K, min_diff, memo)

    return min_diff[0]


# Example usage:
N = 3
M = 2
K = 15
price = [
    [5, 8],
    [7, 12],
    [11, 2]
]

result = solution(N, M, K, price)
print("Minimum difference:", result)
# Задача о рюкзаке - необходимо подобрать комбинацию товаров,
# чтобы вес был не более W, и сумма их цен была максимальной.


def knapsack_bottom_up(capacity, weights, values):

    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем матрицу значениями
    # если вес i-го товара больше w, то вес i-го товара не включаем в рюкзак,
    # иначе берем максимум из стоимости включая i-й товар и не включая i-й товар.

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [2, 1, 3]
values = [20, 15, 30]
capacity = 3
max_value = knapsack_bottom_up(capacity, weights, values)
print(f"Максимальная стоимость: {max_value}")
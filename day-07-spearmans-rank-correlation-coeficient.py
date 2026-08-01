n = int(input())

x = list(map(float, input().split()))
y = list(map(float, input().split()))


def get_ranks(arr):
    sorted_arr = sorted(arr)
    ranks = {}

    for index, value in enumerate(sorted_arr):
        ranks[value] = index + 1

    return ranks


rank_x = get_ranks(x)
rank_y = get_ranks(y)

d_squared_sum = 0

for i in range(n):
    d = rank_x[x[i]] - rank_y[y[i]]
    d_squared_sum += d ** 2

spearman = 1 - (6 * d_squared_sum) / (n * (n ** 2 - 1))

print(f"{spearman:.3f}")
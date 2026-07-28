import math

n = int(input())

x = list(map(float, input().split()))
y = list(map(float, input().split()))

mean_x = sum(x) / n
mean_y = sum(y) / n

std_x = math.sqrt(sum((value - mean_x) ** 2 for value in x) / n)
std_y = math.sqrt(sum((value - mean_y) ** 2 for value in y) / n)

numerator = 0

for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)

pearson = numerator / (n * std_x * std_y)

print(f"{pearson:.3f}")

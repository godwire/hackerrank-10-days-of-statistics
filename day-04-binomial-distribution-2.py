import math

def binomial_probability(x, n, p):
    combinations = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return combinations * (p ** x) * ((1 - p) ** (n - x))


percentage, n = map(int, input().split())

p = percentage / 100

answer1 = 0

for i in range(0, 3):
    answer1 += binomial_probability(i, n, p)

answer2 = 0

for i in range(2, n + 1):
    answer2 += binomial_probability(i, n, p)

print(f"{answer1:.3f}")
print(f"{answer2:.3f}")
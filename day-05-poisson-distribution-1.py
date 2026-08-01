import math

mean = float(input())
k = int(input())

result = ((mean ** k) * (math.e ** -mean)) / math.factorial(k)

print(f"{result:.3f}")
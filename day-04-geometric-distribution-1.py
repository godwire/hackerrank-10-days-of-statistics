numerator, denominator = map(int, input().split())
n = int(input())

p = numerator / denominator

result = ((1 - p) ** (n - 1)) * p

print(f"{result:.3f}")
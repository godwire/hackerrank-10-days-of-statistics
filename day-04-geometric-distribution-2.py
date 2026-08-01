numerator, denominator = map(int, input().split())
n = int(input())

p = numerator / denominator

result = 1 - ((1 - p) ** n)

print(f"{result:.3f}")
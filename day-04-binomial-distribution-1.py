import math

boys, girls = map(float, input().split())

p_boy = boys / (boys + girls)

result = 0

for k in range(3, 7):
    combinations = math.factorial(6) / (math.factorial(k) * math.factorial(6 - k))
    probability = combinations * (p_boy ** k) * ((1 - p_boy) ** (6 - k))
    result += probability

print(f"{result:.3f}")
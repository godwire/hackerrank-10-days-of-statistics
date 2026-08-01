import math

mean, std = map(float, input().split())
x = float(input())
lower, upper = map(float, input().split())

def normal_cdf(value, mean, std):
    return 0.5 * (1 + math.erf((value - mean) / (std * math.sqrt(2))))

answer1 = normal_cdf(x, mean, std)
answer2 = normal_cdf(upper, mean, std) - normal_cdf(lower, mean, std)

print(f"{answer1:.3f}")
print(f"{answer2:.3f}")
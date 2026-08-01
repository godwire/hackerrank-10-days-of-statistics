import math

mean, std = map(float, input().split())
higher_than = float(input())
pass_mark = float(input())


def normal_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))


# P(X > 80)
answer1 = (1 - normal_cdf(higher_than, mean, std)) * 100

# P(X >= 60)
answer2 = (1 - normal_cdf(pass_mark, mean, std)) * 100

# P(X < 60)
answer3 = normal_cdf(pass_mark, mean, std) * 100

print(f"{answer1:.2f}")
print(f"{answer2:.2f}")
print(f"{answer3:.2f}")
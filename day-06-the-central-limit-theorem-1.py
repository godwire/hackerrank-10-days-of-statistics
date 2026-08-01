import math

max_weight = int(input())
n = int(input())
mean = int(input())
std = int(input())


def normal_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))


total_mean = n * mean
total_std = math.sqrt(n) * std

result = normal_cdf(max_weight, total_mean, total_std)

print(f"{result:.4f}")
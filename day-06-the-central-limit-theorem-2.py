import math

tickets_left = int(input())
students = int(input())
mean = float(input())
std = float(input())


def normal_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))


total_mean = students * mean
total_std = math.sqrt(students) * std

result = normal_cdf(tickets_left, total_mean, total_std)

print(f"{result:.4f}")
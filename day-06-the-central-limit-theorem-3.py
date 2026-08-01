import math

sample_size = int(input())
mean = float(input())
std = float(input())
percentage = float(input())
z = float(input())

margin_of_error = z * std / math.sqrt(sample_size)

lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print(f"{lower_bound:.2f}")
print(f"{upper_bound:.2f}")
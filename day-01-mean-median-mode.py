n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

# Mean
mean = sum(numbers) / n

# Median
if n % 2 == 0:
    middle1 = numbers[n // 2 - 1]
    middle2 = numbers[n // 2]
    median = (middle1 + middle2) / 2
else:
    median = numbers[n // 2]

# Mode
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

max_frequency = max(frequency.values())

for number in numbers:
    if frequency[number] == max_frequency:
        mode = number
        break

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(mode)
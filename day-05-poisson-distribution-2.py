mean_a, mean_b = map(float, input().split())

cost_a = 160 + 40 * (mean_a + mean_a ** 2)
cost_b = 128 + 40 * (mean_b + mean_b ** 2)

print(f"{cost_a:.3f}")
print(f"{cost_b:.3f}")
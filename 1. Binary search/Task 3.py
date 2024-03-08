def total_time(x, a, v0, vs):
    time_outside = ((x**2 + (1 - a)**2) ** 0.5) / v0
    time_inside = ((1 - x)**2 + a**2) ** 0.5 / vs

    return time_outside + time_inside


v0, vs = map(int, input().split())
s = int(input())
a = 1 - s / 100

left_border, right_border = 0, 1
epsilon = 1e-7  # Точность поиска

while right_border - left_border > epsilon:
    x1 = left_border + (right_border - left_border) / 3
    x2 = right_border - (right_border - left_border) / 3
    if total_time(x1, a, v0, vs) < total_time(x2, a, v0, vs):
        right_border = x2
    else:
        left_border = x1

print(f"{(left_border + right_border) / 2:.6f}")

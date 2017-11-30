import math

# ========== HW02 SOLUTION [Python3] ========== #


# ========== 1 ========== #

# You are given the first three numbers of the Fibonacci sequence as F = [0, 1, 1].
# Create a for loop to determine the next 20 numbers of the Fibonacci sequence.
# Print F with the final 23 numbers.

F = [0, 1, 1]
for n in range(3, 23):
    f_n = F[n - 1] + F[n - 2]
    F.append(f_n)
print(F)

# ========== 2 ========== #

# Given the list x = [2.0,3.0,5.0,7.0,9.0],
# create a list Y(x) for each float in x.
# Print the list Y .

x = [2.0, 3.0, 5.0, 7.0, 9.0]
Y = []
for v in x:
    new_val = (3.0 * v) ** 2 / (99 * v - v ** 3) - 1 / v
    Y.append(new_val)

# one-liner with list-comprehension:
Y = [(3.0 * v) ** 2 / (99 * v - v ** 3) - 1 / v
     for v in x]

print(Y)

# ========== 3 ========== #

def quadratic(a, b, c):
    x0 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x0, x1

print(quadratic(3.3, 1.7, -9.4))

# ========== 4 ========== #

ans = 0
while ans ** 2 < 2000:
    ans += 1
ans -= 1
print(ans)

# ========== 5 ========== #

def volume(r):
    return 4 / 3 * math.pi * r ** 3

def surface_area(r):
    return 4 * math.pi * r ** 2

def density(r, m=0.35):
    return m / volume(r)

print(volume(0.69))
print(surface_area(0.4))
print(density(0.3))
print(density(0.25, m=2.0))

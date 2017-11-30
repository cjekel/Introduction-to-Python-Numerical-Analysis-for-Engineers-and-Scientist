import numpy as np

# ========== HW04 SOLUTION [Python3] ========== #


# ========== 1 ========== #

np.random.seed(99)
sample = np.random.normal(27.0, 10.0, 100000)

print(sample.mean())
print(sample.std())
print(sample.max())
print(sample.min())

# ========== 2 ========== #

E = 80e10
L = 0.25

K = np.array([[0.00576, -0.00576, 0, 0],
              [-0.00576, 0.0095, -0.002687, 0],
              [0, -0.002687, 0.0075, -0.000733],
              [0, 0, -0.000733, 0.000733]])
# either works:
f = np.array([10000. / 6, 10000. / 3, 10000. / 3, 10000. / 6])
f = np.array([[10000. / 6],
              [10000. / 3],
              [10000. / 3],
              [10000. / 6]])
u = np.linalg.solve(E / L * K, f)
print(u)

# ========== 3 ========== #

a = np.array([[9, 5, 0],
              [9, 5, 0],
              [5, 4, 9]])
b = np.array([[5, 10, 5],
              [4, 4, 3],
              [6, 10, 4]])
# either works:
c = np.array([10, 6, 9])
c = np.matrix([[10],
               [6],
               [9]])

v = np.dot(np.dot(a, b), c)

# or use the @ operator (Python >= 3.5 ONLY)
v = a @ b @ c

# or use np.matrix:

a = np.matrix([[9, 5, 0],
               [9, 5, 0],
               [5, 4, 9]])
b = np.matrix([[5, 10, 5],
               [4, 4, 3],
               [6, 10, 4]])
c = np.matrix([[10], [6], [9]])

v = a * b * c

print(v)

# ========== 4 ========== #

np.random.seed(67)
ints = np.random.randint(3, 14, 100)

idx_max = np.argmax(ints)
print(ints[idx_max])
idx_min = np.argmin(ints)
print(ints[idx_min])

print(np.min(ints) == ints[idx_min])
print(np.max(ints) == ints[idx_max])

# ========== 5 ========== #

x = np.array([0.0, 0.7, 1.7, 2.1])
y = np.array([1.1, 2.99, 5.69, 6.77])
A = np.vstack([x, np.ones(len(x))]).T
# or
A = np.array([x, np.ones(len(x))]).T
c, residuals, rank, sing = np.linalg.lstsq(A, y)
print(c)
print(residuals)
print(rank)

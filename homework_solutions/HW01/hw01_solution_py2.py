# ========== HW01 SOLUTION [Python2] ========== #


# ========== 1 ========== #
# Name one difference between Python2 and Python3. Print your answer as a string in Python.


# accept any of the following:
# * printing in Python3 is done by a function rather than a command
# * integer/integer division always returns an integer in Python2
# * comparison across different data types does not raise an error in Python2
# * any other difference that was mentioned in lecture or is documented

# ========== 2 ========== #
# You are given a list x = [0,1,2,3,4,5,6]. Print the third item in list x.

x = [0,1,2,3,4,5,6]
print x[2]

# ========== 3 ========== #
# Assign y as the reversed order of list x. Print y.

# any of the following works:
y = x[::-1]  # fastest

y = list(reversed(x))

x.reverse()
y = x

print y

# ========== 4 ========== #
# Use list slicing to assign z [1,3,5] from x. Print z.
x = [0,1,2,3,4,5,6]

# any of the following works:
z = x[1:6:2]
z = x[1:7:2]
z = x[1:100:2]  # second slice value does not have an upper limit
z = x[1:-1:2]
z = x[1::2]
print z

# ========== 5 ========== #
""" Correct this code:
x = 99
if (x > 0) is True
print('x is positive')
"""
x = 99
if (x > 0) is True:
    print 'x is positive'

# alternatively, a simpler if condition:
if x > 0:
    print 'x is positive'

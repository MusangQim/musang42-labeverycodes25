###########################################
#  ___                  _       ___ ____  #
# / _ \ _   _  ___  ___| |_    / _ \___ \ #
#| | | | | | |/ _ \/ __| __|  | | | |__) |#
#| |_| | |_| |  __/\__ \ |_   | |_| / __/ #
# \__\_\\__,_|\___||___/\__|___\___/_____|#
#                         |_____|         #
###########################################

# ---------------------PART II-------------------------------------------------------------------

import itertools

# A = [35300, -64910] = using for example, answer 4076
A = [-3324, 68783]

# declare f(x) add, multiply , divide same like part I

def add(x, y):
    return [c1 + c2 for c1, c2 in zip(x, y)]

def multiply(x, y):
    a1, b1 = x
    a2, b2 = y
    return [a1 * a2 - b1 * b2, a1 * b2 + b1 * a2]

def divide(x, y):
    return [c1 // c2 if c1>= 0 else -((-c1) // c2) for c1, c2 in zip(x, y)]

count = 0
xs = [] # part for draw
ys = [] # part for draw

grid = [['.' for _ in range(101)] for _ in range(101)]

for x_axis, y_axis in itertools.product(range(101), range(101)):
    P = [A[0] + 10 * x_axis, A[1] + 10 * y_axis]
    R = [0, 0]
    valid = True

    for _ in range(100):
        R = multiply(R, R)
        R = divide(R, [100000, 100000])
        R = add(R, P)
        if any(abs(xy) > 1000000 for xy in R):
            valid = False
            break

    if valid:
        count += 1
        grid[y_axis][x_axis] = 'x' # yang 'x' is ungraved success
        xs.append(P[0])
        ys.append(P[1])

print("Total engraved:",  count)

for row in grid:
    print("".join(row))


# This part for drawing (yeah first time do this so use Chat okay)

with open("engraved_points.txt", "w")as f:
    for x, y in zip(xs, ys):
        f.write(F"{x},{y}\n")

# ----------------------------------------------------------------------------------------------

# My try and error too, omg tired

'''
# Create f(x) add, multiply, divide
# ..instead of return[a[0] + b[0].....], I just declare x and y with the value, return to x and y

A = [-3, 6]
R = [1, 1]

def add(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    return [x, y]

def multiply(a, b):
    x = a[0]*b[0] - a[1]*b[1]
    y = a[0]*b[1] + a[1]*b[0]
    return [x, y]

def divide(a, b):
    x = int(a[0] / b[0])
    y = int(a[1] / b[1])
    return [x, y]
'''
# This part fo looping 3 pusingan(cycle)
# Still using rules of cycle tadi, cuma declare as 'survive'
# If it too big --> point tak engraved, tapi kalau survive semua cycle --> point di engraved kan
'''
def survive(R, A):
    print(f"\nStart point R = {R}")
    for cycle in range(3):
        R = multiply(R, R)
        print(f" Lepas  multiply: {R}")

        R = divide(R, [10, 10])
        print(f" Lepas  divide: {R}")

        R = add(R, A)
        print(f" Lepas  add: {R}")

        if abs(R[0]) > 50000 or abs(R[1]) > 50000:
            print(f" Broke limit cycle  {cycle+1}! R = {R}")
            return False
    print(f" Survived semua cycle! Final R = {R}")
    return True

survive([1, 1], A)

engraved = 0
for y in range(10):
    for x in range(10):
        R = [x, y]
        if survive(R, A):
            engraved += 1

print("Total engraved points:", engraved)
'''

# ----------------------------------------------------------------------------------------------
# These all just try and error things -_-, penad ah ceni
'''
        if R[0] > threshold or R[0] < -threshold or R[1] > threshold or R[1] < -threshold:
            return False, R, i+1
    return True, R, cycles
'''
'''
A = [3, -6]  #[35300, -64910] # starting point
N = 21 #101 # using 101 x 101 grid based dari quest 
step = 1 #10 # distance point ke point, based on [1000 / (101 - 1)]
total = 0

for row in range(N):
    y_axis = A[1] + row*step
    line = ""
    for col in range(N):
        x_axis = A[0] + col*step
        ok, final, _ = survive([x_axis, y_axis], cycles=20, threshold=1000)
        if ok:
            line += "x"
            total += 1
        else:
            line += "."
    print(line)
print("Total engraved points:", total) #based on "ok"

grid_size = 10

for y in range(grid_size):
    row = ""
    for x in range(grid_size):
        R = [x, y]
        if survive(R, A):
            row += "x"
        else:
            row += "."
    print(row)
'''

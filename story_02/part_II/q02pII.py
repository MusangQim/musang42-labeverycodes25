###########################################
#  ___                  _       ___ ____  #
# / _ \ _   _  ___  ___| |_    / _ \___ \ #
#| | | | | | |/ _ \/ __| __|  | | | |__) |#
#| |_| | |_| |  __/\__ \ |_   | |_| / __/ #
# \__\_\\__,_|\___||___/\__|___\___/_____|#
#                         |_____|         #
###########################################

# ---------------------PART II-------------------------------------------------------------------

# Create f(x) add, multiply, divide
# ..instead of return[a[0] + b[0].....], I just declare x and y with the value, return to x and y

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

# This part fo looping 3 pusingan(cycle)
# Still using rules of cycle tadi, cuma declare as 'survive'
# If it too big --> point tak engraved, tapi kalau robot survive semua cycle --> point di engraved kan

def survive(point, cycles=3, threshold=1000):
    R= [0, 0]
    for i in range(cycles):
        R = multiply(R, R)
        R = divide(R, [10, 10])
        R = add(R, point)
        if R[0] > threshold or R[0] < -threshold or R[1] > threshold or R[1] < -threshold:
            return False, R, i+1
    return True, R, cycles

A = [1, 1]
N = 5
step = 2

for row in range(N):
    y_axis = A[1] + row*step
    line = ""
    for col in range(N):
        x_axis = A[0] + col*step
        ok, final, _ = survive([x_axis, y_axis], cycles=3, threshold=20)
        if ok:
            line += "x"
        else:
            line += "."
    print(line)

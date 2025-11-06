###########################################
#  ___                  _       ___ ____  #
# / _ \ _   _  ___  ___| |_    / _ \___ \ #
#| | | | | | |/ _ \/ __| __|  | | | |__) |#
#| |_| | |_| |  __/\__ \ |_   | |_| / __/ #
# \__\_\\__,_|\___||___/\__|___\___/_____|#
#                         |_____|         #
###########################################
# ---------------------PART I--------------------------------------------------------------------

# Declare A and R
# A = [25, 9] : Example
A = [154,53]
R = [0, 0]

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
'''
(1)Multiply the result by itself.
(2)Divide the result by  [10,10] .
(3)Add  A  to the result. 
'''

for i in range(3):
    R = multiply(R, R) 
    R = divide(R, [10, 10])
    R = add(R, A)

print("Final Result:", R) #answer from R

########################################
#  ___                  _       ___  _ #
# / _ \ _   _  ___  ___| |_    / _ \/ |#
#| | | | | | |/ _ \/ __| __|  | | | | |#
#| |_| | |_| |  __/\__ \ |_   | |_| | |#
# \__\_\\__,_|\___||___/\__|___\___/|_|#
#                         |_____|      #
########################################

# Part I

# list names according quest
names = ["Jorathgoril", "Aureardith", "Khardax", "Braeeth", "Ylarbel", "Mornzorin", "Harnix", "Aelithral", "Fyndagrath", "Aeorvynar"]
# list moves R = Right, L = Left
moves = ["L3", "R6", "L7", "R5", "L1", "R8", "L2", "R5", "L2", "R8", "L4"] # ["R3", "L2", "R3", "L1"]

print(names)

position = 0

for move in moves:
    direction = move[0]
    steps = int(move[1:])
        # move[0] = bagi first letter contoh: R
        # move[1:] = bagi ape ape je lepas first letter contoh : 3
        # int() = convert "3" as string kepada number

    print(direction, steps)
    
    print("Before", names[position])

    if direction == "R":
        position += steps
        # kalau R, it will go increase
    else:
        position -= steps
        # kalau L, it will go decrease

    if position < 0:
        position = 0
    if position >= len(names):
        position = len(names) - 1

    print("After", names[position])
    print("---")

print("Final name:", names[position]) # final answer written

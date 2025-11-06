########################################
#  ___                  _       ___  _ #
# / _ \ _   _  ___  ___| |_    / _ \/ |#
#| | | | | | |/ _ \/ __| __|  | | | | |#
#| |_| | |_| |  __/\__ \ |_   | |_| | |#
# \__\_\\__,_|\___||___/\__|___\___/|_|#
#                         |_____|      #
########################################

# Part II

# this is dummy names = ["Vyrdax", "Dra", "Fyrr", "Elarz"]
names = ["Xyrnarel", "Cynderxal", "Sarnvynar", "Ilddar", "Sarnadir", "Vyrgalor", "Aeljorath", "Joratheldrin" , "Kynkris", "Malfeth", "Jorathsarix", "Nyardith", "Glaurthyris", "Tarldaros", "Phyrrax", "Urithcarth", "Cynderzrak", "Larnar", "Krytheldrith", "Voraxardith"]
# this is dummy moves = ["R3", "L2", "R3", "L1"]
moves = ["L19", "R7", "L7", "R18", "L7", "R11", "L9", "R19", "L15", "R18", "L5", "R8", "L5", "R13", "L5", "R18","L5", "R18", "L5", "R8", "L15", "R12", "L6", "R18", "L15", "R13", "L9", "R17", "L10"]

print(names)

position = 0;

n = len(names) # n mewakili number of names dlm array contoh : ade 4 org

print(n)

for move in moves:
    direction = move[0] # take R as right and L as Left
    steps = int(move[1:]) # based on how many moves after R and L

    print(direction, steps)
    print("Before:", names[position])

    if direction == "R":
        position = (position + steps) % n # like increment by modulus
    else:
        position = (position - steps) % n # decrement for Left (L) and modulus

    print("After:", names[position])
    print("---")

print("First parent:", names[position])

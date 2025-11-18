#####################################
#  ___                  _       _ _ #
# / _ \ _   _  ___  ___| |_    / / |#
#| | | | | | |/ _ \/ __| __|   | | |#
#| |_| | |_| |  __/\__ \ |_    | | |#
# \__\_\\__,_|\___||___/\__|___|_|_|#
#        |_____|   #
#####################################
# ---------------PART II-------------------------------------
# cols = [9, 1, 1, 4, 9, 6]
# duck = [2, 1, 17, 12, 19, 9]
notes_given = """
805
706
179
48
158
150
232
885
598
524
423
"""

duck = list(map(int, notes_given.strip().split("\n")))

phase = 1
lap = 10

while True:
    change = False
    for i in range(len(duck) - 1):
        if phase == 1:
            if duck[i] > duck[i + 1]:
                duck[i] -= 1
                duck[i + 1] += 1
                change = True
        else:
            if duck[i] < duck[i + 1]:
                duck[i] += 1
                duck[i + 1] -= 1
                change = True
    if change:
        # lap -= 1
        lap += 1
    else:
        if phase == 1:
            phase = 2
        else:
            break

print("The answer is:", lap)

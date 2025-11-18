#####################################
#  ___                  _       _ _ #
# / _ \ _   _  ___  ___| |_    / / |#
#| | | | | | |/ _ \/ __| __|   | | |#
#| |_| | |_| |  __/\__ \ |_    | | |#
# \__\_\\__,_|\___||___/\__|___|_|_|#
#                         |_____|   #
#####################################
# ---------------PART I-------------------------------------

def checksum(cols):
    total = 0
    for i, c in enumerate(cols):
        total += (i + 1) * c
    return total

def phase1(cols):
    moved = False
    for i in range(len(cols) - 1):
        if cols[i] > cols[i + 1]:
            cols[i] -= 1
            cols[i + 1] += 1
            moved = True
    return moved

def phase2(cols):
    moved = False
    for i in range(len(cols) - 1):
        if cols[i] < cols[i + 1]:
            cols[i] += 1
            cols[i + 1] -= 1
            moved = True
    return moved

def simulate(cols, rounds):
    cols = cols.copy()
    checksums = []
    phase = 1
    for r in range(1, rounds + 1):
        if phase == 1:
            change  = phase1(cols)
            if not change:
                phase = 2
        else:
            phase2(cols)
        checksums.append(checksum(cols))
    return checksums

cols = [9, 1, 1, 4, 9, 6]
# cols = [2, 1, 17, 12, 19, 9]
checksums = simulate(cols, 10)

for i, c in enumerate(checksums, start=1):
    print(f"Round {i}: {c}")

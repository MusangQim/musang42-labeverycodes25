#########################################
#  ___                  _       _ ____  #
# / _ \ _   _  ___  ___| |_    / |___ \ #
#| | | | | | |/ _ \/ __| __|   | | __) |#
#| |_| | |_| |  __/\__ \ |_    | |/ __/ #
# \__\_\\__,_|\___||___/\__|___|_|_____|#
#                         |_____|       #
#########################################
# ----------------------PART II----------------------
from collections import deque
"""
notes = """
989601
857782
746543
766789
"""
"""

notes = """
9589233445
9679121695
8469121876
8352919876
7342914327
7234193437
6789193538
6781219648
5691219769
5443329859
"""

clean_notes = notes.strip()
list_notes = clean_notes.splitlines()


arrange_barrel = []

for rows in list_notes:
    row_barrel = []
    for num in rows:
        row_barrel.append(int(num))
    arrange_barrel.append(row_barrel)

row_last = len(arrange_barrel) - 1
col_last = len(arrange_barrel[0]) - 1

burn_barrel = set()
burn_barrel.add((0, 0))
burn_barrel.add((row_last, col_last))

turn_ignite = deque()
turn_ignite.append((0, 0))
turn_ignite.append((row_last, col_last))

while turn_ignite:
    r, c = turn_ignite.popleft()

    another_barrel = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
    ]

    for rr, cc in another_barrel:
        if rr < 0 or rr >= len(arrange_barrel):
            continue
        if cc < 0 or cc >= len(arrange_barrel[rr]):
            continue
        if arrange_barrel[rr][cc] > arrange_barrel[r][c]:
            continue
        if (rr, cc) in burn_barrel:
            continue
        burn_barrel.add((rr, cc))
        turn_ignite.append((rr, cc))

print(len(burn_barrel))

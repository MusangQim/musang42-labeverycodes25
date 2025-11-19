#########################################
#  ___                  _       _ ____  #
# / _ \ _   _  ___  ___| |_    / |___ \ #
#| | | | | | |/ _ \/ __| __|   | | __) |#
#| |_| | |_| |  __/\__ \ |_    | |/ __/ #
# \__\_\\__,_|\___||___/\__|___|_|_____|#
#                         |_____|       #
#########################################
# ----------------------PART I----------------------
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
91373452051102203839
99573717042213282599
89970322318840562992
58998253514566229905
13699710612685799330
00679938857265997830
07530991762849930463
40487399077699510534
24164849970998243223
44076676999914838153
45363147099750525566
82723858999945143676
53661629987993333510
04522499370099083852
82404998708379927534
31519986362331995048
64499588555353899141
42996206408576049985
49955541042706041994
99441265008735846399
"""
clean_notes = notes.strip()
list_notes = clean_notes.splitlines()


arrange_barrel = []

for rows in list_notes:
    row_barrel = []
    for num in rows:
        row_barrel.append(int(num))
    arrange_barrel.append(row_barrel)

burn_barrel = set()
burn_barrel.add((0, 0))

turn_ignite = deque()
turn_ignite.append((0, 0))

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

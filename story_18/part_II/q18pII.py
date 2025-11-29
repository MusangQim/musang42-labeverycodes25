#######################################
#  ___                  _     _  ___  #
# / _ \ _   _  ___  ___| |_  / |( _ ) #
#| | | | | | |/ _ \/ __| __| | |/ _ \ #
#| |_| | |_| |  __/\__ \ |_  | | (_) |#
# \__\_\\__,_|\___||___/\__| |_|\___/ #
#                                     #
#######################################
# ---------------------PART II------------------------------
import re

raw_input_text = """
Plant 1 with thickness 1:
- free branch with thickness 1

Plant 2 with thickness 1:
- free branch with thickness 1

Plant 3 with thickness 1:
- free branch with thickness 1

Plant 4 with thickness 1:
- free branch with thickness 1

Plant 5 with thickness 1:
- free branch with thickness 1

Plant 6 with thickness 1:
- free branch with thickness 1

Plant 7 with thickness 1:
- free branch with thickness 1

Plant 8 with thickness 1:
- free branch with thickness 1

Plant 9 with thickness 1:
- free branch with thickness 1

Plant 10 with thickness 1:
- free branch with thickness 1

Plant 11 with thickness 1:
- free branch with thickness 1

Plant 12 with thickness 1:
- free branch with thickness 1

Plant 13 with thickness 1:
- free branch with thickness 1

Plant 14 with thickness 1:
- free branch with thickness 1

Plant 15 with thickness 1:
- free branch with thickness 1

Plant 16 with thickness 1:
- free branch with thickness 1

Plant 17 with thickness 17:
- branch to Plant 1 with thickness 21
- branch to Plant 2 with thickness 1
- branch to Plant 3 with thickness 15
- branch to Plant 4 with thickness 22
- branch to Plant 5 with thickness 10
- branch to Plant 6 with thickness 9
- branch to Plant 7 with thickness 3
- branch to Plant 8 with thickness 27
- branch to Plant 9 with thickness 27
- branch to Plant 10 with thickness 24
- branch to Plant 11 with thickness 10
- branch to Plant 12 with thickness 16
- branch to Plant 13 with thickness 16
- branch to Plant 14 with thickness 6
- branch to Plant 15 with thickness -1
- branch to Plant 16 with thickness -5

Plant 18 with thickness 19:
- branch to Plant 1 with thickness -5
- branch to Plant 2 with thickness -2
- branch to Plant 3 with thickness 12
- branch to Plant 4 with thickness 14
- branch to Plant 5 with thickness 22
- branch to Plant 6 with thickness 10
- branch to Plant 7 with thickness 24
- branch to Plant 8 with thickness 23
- branch to Plant 9 with thickness 25
- branch to Plant 10 with thickness 1
- branch to Plant 11 with thickness 11
- branch to Plant 12 with thickness 20
- branch to Plant 13 with thickness 13
- branch to Plant 14 with thickness 0
- branch to Plant 15 with thickness 4
- branch to Plant 16 with thickness 13

Plant 19 with thickness 13:
- branch to Plant 1 with thickness 18
- branch to Plant 2 with thickness -7
- branch to Plant 3 with thickness -6
- branch to Plant 4 with thickness 17
- branch to Plant 5 with thickness 10
- branch to Plant 6 with thickness 26
- branch to Plant 7 with thickness -8
- branch to Plant 8 with thickness -3
- branch to Plant 9 with thickness 5
- branch to Plant 10 with thickness 0
- branch to Plant 11 with thickness 9
- branch to Plant 12 with thickness 29
- branch to Plant 13 with thickness -3
- branch to Plant 14 with thickness 26
- branch to Plant 15 with thickness 19
- branch to Plant 16 with thickness -2

Plant 20 with thickness 18:
- branch to Plant 1 with thickness 28
- branch to Plant 2 with thickness 21
- branch to Plant 3 with thickness -8
- branch to Plant 4 with thickness 16
- branch to Plant 5 with thickness -8
- branch to Plant 6 with thickness 6
- branch to Plant 7 with thickness 8
- branch to Plant 8 with thickness 2
- branch to Plant 9 with thickness 25
- branch to Plant 10 with thickness 23
- branch to Plant 11 with thickness 7
- branch to Plant 12 with thickness -5
- branch to Plant 13 with thickness 9
- branch to Plant 14 with thickness 7
- branch to Plant 15 with thickness 24
- branch to Plant 16 with thickness 9

Plant 21 with thickness 12:
- branch to Plant 1 with thickness 18
- branch to Plant 2 with thickness 26
- branch to Plant 3 with thickness 1
- branch to Plant 4 with thickness 16
- branch to Plant 5 with thickness -2
- branch to Plant 6 with thickness 17
- branch to Plant 7 with thickness -3
- branch to Plant 8 with thickness -2
- branch to Plant 9 with thickness 13
- branch to Plant 10 with thickness 2
- branch to Plant 11 with thickness -5
- branch to Plant 12 with thickness 9
- branch to Plant 13 with thickness -6
- branch to Plant 14 with thickness 3
- branch to Plant 15 with thickness -6
- branch to Plant 16 with thickness -2

Plant 22 with thickness 4:
- branch to Plant 1 with thickness 28
- branch to Plant 2 with thickness 17
- branch to Plant 3 with thickness 11
- branch to Plant 4 with thickness 9
- branch to Plant 5 with thickness 15
- branch to Plant 6 with thickness 3
- branch to Plant 7 with thickness 23
- branch to Plant 8 with thickness 19
- branch to Plant 9 with thickness 7
- branch to Plant 10 with thickness 16
- branch to Plant 11 with thickness 14
- branch to Plant 12 with thickness -8
- branch to Plant 13 with thickness 18
- branch to Plant 14 with thickness 28
- branch to Plant 15 with thickness 8
- branch to Plant 16 with thickness 22

Plant 23 with thickness 12:
- branch to Plant 1 with thickness -9
- branch to Plant 2 with thickness 9
- branch to Plant 3 with thickness 20
- branch to Plant 4 with thickness -4
- branch to Plant 5 with thickness -1
- branch to Plant 6 with thickness 1
- branch to Plant 7 with thickness 25
- branch to Plant 8 with thickness -7
- branch to Plant 9 with thickness -5
- branch to Plant 10 with thickness 8
- branch to Plant 11 with thickness 28
- branch to Plant 12 with thickness 26
- branch to Plant 13 with thickness 0
- branch to Plant 14 with thickness 3
- branch to Plant 15 with thickness -8
- branch to Plant 16 with thickness 29

Plant 24 with thickness 18:
- branch to Plant 1 with thickness 20
- branch to Plant 2 with thickness 7
- branch to Plant 3 with thickness 14
- branch to Plant 4 with thickness 16
- branch to Plant 5 with thickness 20
- branch to Plant 6 with thickness 5
- branch to Plant 7 with thickness -5
- branch to Plant 8 with thickness 13
- branch to Plant 9 with thickness 9
- branch to Plant 10 with thickness -10
- branch to Plant 11 with thickness -5
- branch to Plant 12 with thickness 23
- branch to Plant 13 with thickness -5
- branch to Plant 14 with thickness 27
- branch to Plant 15 with thickness 27
- branch to Plant 16 with thickness 24

Plant 25 with thickness 18:
- branch to Plant 1 with thickness 16
- branch to Plant 2 with thickness 28
- branch to Plant 3 with thickness 27
- branch to Plant 4 with thickness 6
- branch to Plant 5 with thickness -7
- branch to Plant 6 with thickness -1
- branch to Plant 7 with thickness 4
- branch to Plant 8 with thickness 12
- branch to Plant 9 with thickness 5
- branch to Plant 10 with thickness 29
- branch to Plant 11 with thickness 27
- branch to Plant 12 with thickness -8
- branch to Plant 13 with thickness 0
- branch to Plant 14 with thickness 7
- branch to Plant 15 with thickness 11
- branch to Plant 16 with thickness 21

Plant 26 with thickness 14:
- branch to Plant 1 with thickness 2
- branch to Plant 2 with thickness 8
- branch to Plant 3 with thickness 11
- branch to Plant 4 with thickness 2
- branch to Plant 5 with thickness 2
- branch to Plant 6 with thickness 25
- branch to Plant 7 with thickness 18
- branch to Plant 8 with thickness 26
- branch to Plant 9 with thickness 9
- branch to Plant 10 with thickness 16
- branch to Plant 11 with thickness 28
- branch to Plant 12 with thickness 6
- branch to Plant 13 with thickness 28
- branch to Plant 14 with thickness 6
- branch to Plant 15 with thickness 14
- branch to Plant 16 with thickness -8

Plant 27 with thickness 74:
- branch to Plant 17 with thickness 49
- branch to Plant 18 with thickness -15
- branch to Plant 19 with thickness 22
- branch to Plant 20 with thickness 45
- branch to Plant 21 with thickness 30
- branch to Plant 22 with thickness 59
- branch to Plant 23 with thickness -15
- branch to Plant 24 with thickness 51
- branch to Plant 25 with thickness 3
- branch to Plant 26 with thickness 9

Plant 28 with thickness 32:
- branch to Plant 17 with thickness 20
- branch to Plant 18 with thickness 49
- branch to Plant 19 with thickness 37
- branch to Plant 20 with thickness 20
- branch to Plant 21 with thickness 68
- branch to Plant 22 with thickness 16
- branch to Plant 23 with thickness -16
- branch to Plant 24 with thickness 41
- branch to Plant 25 with thickness -11
- branch to Plant 26 with thickness -15

Plant 29 with thickness 68:
- branch to Plant 17 with thickness 9
- branch to Plant 18 with thickness -8
- branch to Plant 19 with thickness 67
- branch to Plant 20 with thickness 29
- branch to Plant 21 with thickness 29
- branch to Plant 22 with thickness 22
- branch to Plant 23 with thickness 18
- branch to Plant 24 with thickness 39
- branch to Plant 25 with thickness -9
- branch to Plant 26 with thickness 42

Plant 30 with thickness 77:
- branch to Plant 17 with thickness 39
- branch to Plant 18 with thickness 38
- branch to Plant 19 with thickness 26
- branch to Plant 20 with thickness 8
- branch to Plant 21 with thickness -1
- branch to Plant 22 with thickness 20
- branch to Plant 23 with thickness 13
- branch to Plant 24 with thickness 67
- branch to Plant 25 with thickness 54
- branch to Plant 26 with thickness -15

Plant 31 with thickness 76:
- branch to Plant 17 with thickness -14
- branch to Plant 18 with thickness -4
- branch to Plant 19 with thickness 35
- branch to Plant 20 with thickness 19
- branch to Plant 21 with thickness 42
- branch to Plant 22 with thickness -11
- branch to Plant 23 with thickness 49
- branch to Plant 24 with thickness 22
- branch to Plant 25 with thickness 65
- branch to Plant 26 with thickness 56

Plant 32 with thickness 76:
- branch to Plant 17 with thickness -5
- branch to Plant 18 with thickness -5
- branch to Plant 19 with thickness -8
- branch to Plant 20 with thickness 43
- branch to Plant 21 with thickness 59
- branch to Plant 22 with thickness 2
- branch to Plant 23 with thickness 43
- branch to Plant 24 with thickness -10
- branch to Plant 25 with thickness 27
- branch to Plant 26 with thickness -14

Plant 33 with thickness 34:
- branch to Plant 27 with thickness 48
- branch to Plant 28 with thickness 70
- branch to Plant 29 with thickness 4
- branch to Plant 30 with thickness 64
- branch to Plant 31 with thickness 41
- branch to Plant 32 with thickness 15

Plant 34 with thickness 85:
- branch to Plant 27 with thickness 2
- branch to Plant 28 with thickness -20
- branch to Plant 29 with thickness 8
- branch to Plant 30 with thickness 25
- branch to Plant 31 with thickness -20
- branch to Plant 32 with thickness -5

Plant 35 with thickness 53:
- branch to Plant 27 with thickness -19
- branch to Plant 28 with thickness 15
- branch to Plant 29 with thickness 30
- branch to Plant 30 with thickness 51
- branch to Plant 31 with thickness 28
- branch to Plant 32 with thickness 41

Plant 36 with thickness 68976325:
- branch to Plant 33 with thickness 29
- branch to Plant 34 with thickness 28
- branch to Plant 35 with thickness 11


1 1 1 1 1 0 0 1 0 0 0 0 1 0 1 1
1 1 1 0 1 1 0 1 1 0 1 0 0 0 0 0
0 1 0 1 1 1 0 1 1 0 0 1 1 1 0 0
0 0 1 0 0 1 0 0 1 0 0 0 0 0 1 1
1 1 1 1 0 0 0 1 1 0 0 0 1 1 1 1
1 1 1 0 0 0 0 1 0 0 1 1 1 1 1 1
1 1 0 0 0 0 0 1 1 1 0 0 1 1 1 1
1 0 0 0 0 1 1 0 0 1 1 0 1 0 1 1
0 1 1 1 1 1 0 1 1 0 0 0 0 1 0 0
0 1 1 0 1 1 1 0 1 0 0 1 1 0 0 1
1 1 0 0 0 0 1 0 0 1 0 0 1 1 0 0
0 1 0 0 0 1 1 1 0 1 0 0 0 1 0 1
1 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0
1 0 1 0 1 1 1 1 1 0 0 1 0 0 0 1
1 0 0 0 0 0 1 0 1 0 1 1 0 0 1 1
1 1 1 0 0 1 0 1 1 0 1 0 1 0 1 0
0 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0
1 0 1 1 0 1 1 0 0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1 0 0 1 1 1 1 1 1
1 1 0 1 1 0 0 1 0 1 1 0 1 1 0 0
1 0 1 1 0 1 1 0 0 1 1 1 0 1 0 0
1 1 0 1 1 0 1 1 0 1 1 0 0 1 1 1
0 1 1 0 1 1 0 0 1 1 1 1 0 1 0 1
1 1 1 0 1 0 1 0 1 1 1 1 1 0 0 0
0 1 1 1 0 1 1 0 1 0 1 1 1 0 0 0
1 0 0 1 0 0 0 1 0 0 0 1 0 0 1 1
0 0 1 0 0 0 1 0 0 1 1 0 1 1 0 1
1 0 0 1 0 0 1 0 1 1 0 0 1 1 0 0
0 1 0 1 0 0 1 0 1 1 1 1 0 1 1 0
1 0 0 1 1 0 0 1 1 1 0 1 1 0 0 1
0 0 0 0 0 1 1 0 0 1 1 1 0 0 1 0
0 0 1 1 0 1 1 1 1 1 0 1 1 0 1 0
1 0 0 1 0 0 0 0 1 1 1 0 0 1 0 0
0 0 1 0 1 0 1 1 1 1 0 1 0 1 0 1
1 0 0 0 1 1 0 0 1 0 0 1 1 0 1 1
0 1 1 1 0 0 0 0 1 0 0 1 1 1 0 0
1 1 1 1 0 1 1 0 1 1 0 0 0 0 0 1
0 1 1 1 1 1 1 0 1 1 0 1 1 0 1 1
1 0 0 1 0 0 1 0 1 1 1 1 1 0 1 1
0 0 0 1 1 0 0 0 0 1 0 1 1 1 1 1
1 0 1 0 1 0 1 0 0 1 0 0 0 1 0 1
0 0 1 0 1 0 0 1 1 1 1 0 0 0 0 1
0 1 1 1 0 0 0 0 0 1 0 1 0 1 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1
1 0 1 0 0 0 1 0 1 0 1 1 1 0 1 1
0 0 1 0 1 0 0 1 1 0 0 0 1 0 1 1
1 0 0 0 1 1 0 1 0 0 0 0 0 1 1 1
1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 0
0 1 0 1 1 1 0 0 1 0 1 0 0 1 1 0
1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 0
0 1 0 1 0 0 1 0 1 0 0 1 1 1 0 0
1 0 1 0 1 0 0 1 1 1 0 0 1 1 1 1
0 1 1 1 1 1 1 1 0 1 0 0 0 1 0 1
1 0 0 1 1 1 0 1 1 1 1 1 0 0 0 1
1 0 1 0 0 0 0 1 1 1 1 0 0 1 1 1
0 1 1 0 1 0 1 1 1 1 0 0 1 1 1 0
1 0 0 0 0 0 1 1 0 0 1 0 1 1 1 1
1 0 0 1 1 0 1 1 1 1 0 1 0 1 1 0
0 0 1 0 1 1 1 1 0 0 0 0 0 1 1 1
1 1 0 1 0 0 0 0 1 0 0 0 1 1 0 1
1 0 1 0 1 1 0 0 1 0 0 1 0 1 0 1
0 1 0 0 1 0 0 1 0 0 0 0 1 1 0 1
0 0 1 0 1 1 1 1 0 1 0 0 1 1 1 0
1 0 1 1 1 1 1 0 0 1 1 0 0 0 1 1
0 1 0 1 1 0 0 1 1 0 1 0 0 0 1 0
1 1 1 0 1 1 1 1 1 1 1 0 1 0 1 0
0 1 0 0 0 0 0 1 0 1 0 1 1 0 0 1
0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 1
0 1 0 0 0 1 0 0 0 1 1 1 1 0 0 0
1 0 1 0 0 1 0 0 1 1 0 0 1 1 0 1
1 0 1 0 1 0 1 1 0 1 0 1 1 1 0 0
0 0 1 0 1 0 0 0 1 1 1 0 1 0 0 1
1 1 1 0 1 0 0 1 0 1 1 1 0 1 1 0
1 1 1 1 0 0 0 0 1 1 1 0 1 1 1 0
1 0 1 0 1 0 1 0 0 1 1 1 0 1 0 1
1 0 0 0 0 1 0 1 0 1 0 1 0 1 1 0
0 1 0 1 1 1 0 1 0 1 0 0 1 1 0 0
0 0 1 1 1 1 0 1 1 1 0 0 1 0 0 0
0 1 1 1 1 0 0 1 1 1 0 0 0 1 1 0
1 1 1 0 0 1 1 1 0 0 1 0 0 1 1 1
0 0 0 1 1 1 0 1 0 1 1 0 0 0 1 1
1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1
1 1 0 0 0 1 0 1 0 1 1 0 1 1 1 0
0 1 0 1 1 1 0 0 1 0 1 1 0 1 1 1
1 0 0 0 0 0 1 0 0 0 1 1 1 1 0 0
0 1 1 0 0 1 1 1 1 0 0 0 1 0 0 1
1 1 0 1 1 1 0 0 0 1 1 0 1 0 1 1
1 1 1 1 0 0 1 1 0 1 1 0 0 0 0 0
0 0 0 0 1 1 0 1 1 1 0 0 1 1 1 1
0 0 1 0 0 1 1 1 1 0 0 1 1 0 0 1
0 1 0 0 1 1 0 1 1 0 1 1 1 1 1 1
1 0 1 0 1 0 1 0 0 0 0 0 0 1 1 0
0 1 1 0 0 1 0 0 0 0 0 1 0 0 0 1
1 1 1 0 1 1 1 0 1 1 0 1 0 0 0 0
1 0 0 0 1 0 1 1 1 1 1 0 0 0 1 0
0 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1
1 0 0 0 0 0 1 1 1 0 1 0 1 1 0 0
0 0 0 0 0 1 0 0 0 0 1 1 1 1 1 1
0 0 1 1 1 1 0 0 1 1 1 1 1 0 1 0
1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 0
""".strip()

blocks, tests = raw_input_text.split("\n\n\n")

thicknesses = {}
link_branches = {}

for block in blocks.split("\n\n"):
    plant_line, *branch_lines = block.splitlines()

    match = re.match(r"^Plant (\d+) with thickness (\d+):$", plant_line)
    plant_id = int(match[1])
    thicknesses[plant_id] = int(match[2])

    for line in branch_lines:
        if line.startswith("- free"):
            break

        match = re.match(r"^- branch to Plant (\d+) with thickness (-?\d+)$", line)
        source = int(match[1])
        branch_thick = int(match[2])

        if plant_id not in link_branches:
            link_branches[plant_id] = []

        link_branches[plant_id].append((source, branch_thick))


plant_count = len(thicknesses)

def calculate(activations):
    energy = {i + 1: value for i, value in enumerate(activations)}

    for plant in range(len(activations) + 1, plant_count + 1):
        total_energy = 0
        for source, thick in link_branches.get(plant, []):
            total_energy += energy[source] * thick

        energy[plant] = total_energy

        if energy[plant] < thicknesses[plant]:
            energy[plant] = 0

    return energy[plant_count]


total = 0

for test in tests.splitlines():
    total += calculate(list(map(int, test.split())))

print(total)


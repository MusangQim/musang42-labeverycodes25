#######################################
#  ___                  _     _  ___  #
# / _ \ _   _  ___  ___| |_  / |( _ ) #
#| | | | | | |/ _ \/ __| __| | |/ _ \ #
#| |_| | |_| |  __/\__ \ |_  | | (_) |#
# \__\_\\__,_|\___||___/\__| |_|\___/ #
#                                     #
#######################################
# ---------------------PART I------------------------------

import re

raw_input_text_ex = """
Plant 1 with thickness 1:
- free branch with thickness 1

Plant 2 with thickness 1:
- free branch with thickness 1

Plant 3 with thickness 1:
- free branch with thickness 1

Plant 4 with thickness 17:
- branch to Plant 1 with thickness 15
- branch to Plant 2 with thickness 3

Plant 5 with thickness 24:
- branch to Plant 2 with thickness 11
- branch to Plant 3 with thickness 13

Plant 6 with thickness 15:
- branch to Plant 3 with thickness 14

Plant 7 with thickness 10:
- branch to Plant 4 with thickness 15
- branch to Plant 5 with thickness 21
- branch to Plant 6 with thickness 34
""".strip()

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

Plant 10 with thickness 27:
- branch to Plant 8 with thickness 42
- branch to Plant 1 with thickness 26
- branch to Plant 2 with thickness 30
- branch to Plant 9 with thickness 49

Plant 11 with thickness 34:
- branch to Plant 5 with thickness 45
- branch to Plant 1 with thickness 27
- branch to Plant 4 with thickness 25
- branch to Plant 3 with thickness 46
- branch to Plant 9 with thickness 19
- branch to Plant 8 with thickness 23
- branch to Plant 7 with thickness 49

Plant 12 with thickness 41:
- branch to Plant 2 with thickness 10
- branch to Plant 5 with thickness 29

Plant 13 with thickness 19:
- branch to Plant 9 with thickness 32
- branch to Plant 6 with thickness 30

Plant 14 with thickness 46:
- branch to Plant 4 with thickness 23
- branch to Plant 8 with thickness 13

Plant 15 with thickness 10:
- branch to Plant 11 with thickness 14
- branch to Plant 13 with thickness 53
- branch to Plant 12 with thickness 57
- branch to Plant 14 with thickness 49

Plant 16 with thickness 72:
- branch to Plant 11 with thickness 15
- branch to Plant 13 with thickness 32

Plant 17 with thickness 87:
- branch to Plant 12 with thickness 29
- branch to Plant 13 with thickness 38
- branch to Plant 14 with thickness 54
- branch to Plant 11 with thickness 28

Plant 18 with thickness 9:
- branch to Plant 14 with thickness 70
- branch to Plant 13 with thickness 31
- branch to Plant 10 with thickness 27
- branch to Plant 11 with thickness 16

Plant 19 with thickness 1:
- branch to Plant 15 with thickness 12
- branch to Plant 16 with thickness 21
- branch to Plant 17 with thickness 68
- branch to Plant 18 with thickness 19
""".strip()

thickness_map = {}
free_energy_plants = set()
branch_map = {}

for block in raw_input_text.split("\n\n"):
    header_line, *branch_lines = block.splitlines()

    # Plant X with thickness Y:
    match = re.match(r"^Plant (\d+) with thickness (\d+):$", header_line)
    plant_id = int(match[1])
    plant_thick = int(match[2])
    thickness_map[plant_id] = plant_thick

    for line in branch_lines:
        if line.startswith("- free"):
            free_energy_plants.add(plant_id)
            break

        match = re.match(r"^- branch to Plant (\d+) with thickness (\d+)$", line)
        target_plant = int(match[1])
        branch_thick = int(match[2])

        if plant_id not in branch_map:
            branch_map[plant_id] = []

        branch_map[plant_id].append((target_plant, branch_thick))

total_plants = len(thickness_map)
energy_map = {}

for plant in range(1, total_plants + 1):

    if plant in free_energy_plants:
        energy_map[plant] = 1
    else:
        total_energy = 0
        for source_plant, branch_thick in branch_map.get(plant, []):
            total_energy += energy_map[source_plant] * branch_thick

        energy_map[plant] = total_energy

    # energy 0 → mati
    if energy_map[plant] < thickness_map[plant]:
        energy_map[plant] = 0


print(energy_map[total_plants])


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

raw_input_text = """
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


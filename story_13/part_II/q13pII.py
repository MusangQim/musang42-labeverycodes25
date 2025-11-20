#########################################
#  ___                  _       _ _____ #
# / _ \ _   _  ___  ___| |_    / |___ / #
#| | | | | | |/ _ \/ __| __|   | | |_ \ #
#| |_| | |_| |  __/\__ \ |_    | |___) |#
# \__\_\\__,_|\___||___/\__|___|_|____/ #
#                         |_____|       #
#########################################
# --------------------------PART II-------------------------------

list_notes = """
72
58
47
61
67
"""

clean_notes = list_notes.strip()
notes = clean_notes.splitlines()

roda = [1]
put_right = True

for start_num, end_num in notes:

    if start_num <= end_num:
        expand_num = list(range(start_num, end_num + 1))
    else:
        expand_num = list(range(start_num, end_num - 1, -1))

    if put_right:
        roda += expand_num
    else:
        roda = expand_num + roda

    put_right = not put_right

no_of_steps = 20252025

start_position = roda.index(1)
final_position = (start_position + no_of_steps) %len(roda)

print(roda[final_position])


# ----------------PART I punya------------------------------
"""
put_right = True
for value in notes:
    if put_right:
        roda.append(value)
    else:
        roda.insert(0, value)

    put_right = not put_right

no_of_turn = 2025
start_index = roda.index(1)
landing_index = (start_index + no_of_turn) % len(roda)
print(roda[landing_index])
"""

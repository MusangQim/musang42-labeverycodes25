#######################################
#  ___                  _     _ ____  #
# / _ \ _   _  ___  ___| |_  / | ___| #
#| | | | | | |/ _ \/ __| __| | |___ \ #
#| |_| | |_| |  __/\__ \ |_  | |___) |#
# \__\_\\__,_|\___||___/\__| |_|____/ #
#                                     #
#######################################
# ------------------------PART II------------------------------------

from collections import deque

# raw_notes = "L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"
# raw_notes = "L6,L3,L3,R3,L3,L3,R6,L6,L6,R3,L6,L3,R3,L3,R6,L3,L6,R6,L3,R3,L3,R6,L3,L6,R3,L6,R6,L6,R3,L6,L3,R3,L6,R3,L3,R6,L3,L3,R3,L3,R6,L3,R6,L3,R6,L6,L6,R6,L6,R3,R6,L6,L6,L3,R3,R6,L3,R3,L3,R6"
raw_notes = "L44,L44,L22,L11,R66,L55,L88,R77,L99,L22,L77,R55,R99,L11,L88,R55,R77,L22,L33,R66,L99,L77,R33,R22,L44,L11,R44,L77,L44,R77,L77,L11,R11,R55,L77,R44,L11,R88,L55,L88,R88,L77,L88,L66,R11,R99,R33,L22,L55,R11,R99,L88,L22,L55,R55,R55,R22,L77,R88,L33,L33,R66,L44,L22,R88,R77,L55,L88,R77,L77,R88,L77,R66,L11,R77,L44,L99,L22,R33,R33,L11,R55,R99,L99,L88,R99,L77,L99,R99,R77,L55,R88,L77,L22,R55,L44,L44,R11,R55,L66,R66,L88,R66,L55,L88,R44,L44,R11,R66,L44,R99,L22,L33,R99,L22,R77,L55,R11,L33,R77,L99,L77,R44,R77,L44,R99,L44,L44,R99,L99,L55,R22,R44,L99,R33,L22,R55,L88,R55,R33,L99,L88,L11,R88,R77,L55,L44,R55,L88,L11,R44,R66,L22,R88,L33,L55,R22,R44,L22,L11,R66,L11,R66,R66,L55,R44,L44,R99,L88,L11,R99,L99,L99,L44,R55,R33,R33,L88,R44,L66,R11,L55,R77,L55,R44,L66,R99,L99,L11,L22"
notes = [(item[0], int(item[1:])) for item in raw_notes.split(",")]


peta_laluan = {0: "S"}

direction = 1j
current_position = 0;

for turn, length in notes:
    if turn == "R":
        direction *= -1j
    else:
        direction *= 1j

    for _ in range(length):
        current_position += direction
        peta_laluan[current_position] = "#"

peta_laluan[current_position] = "E"

top = max(pos.imag for pos in peta_laluan) + 1
bottom = min(pos.imag for pos in peta_laluan) - 1
left = min(pos.real for pos in peta_laluan) - 1
right = max(pos.real for pos in peta_laluan) + 1

find_position = {0}
queue = deque([(0, 0)])

while queue:
    steps, position = queue.popleft()

    for neighbor in [position - 1, position + 1, position - 1j, position + 1j]:
        if bottom <= neighbor.imag <= top and left <= neighbor.real <= right:
            if neighbor not in find_position and peta_laluan.get(neighbor) != "#":
                
                if peta_laluan.get(neighbor) == "E":
                    print(steps + 1)
                    exit(0)

                find_position.add(neighbor)
                queue.append((steps + 1, neighbor))

steps_max = 75
visit = {0}
queue = deque([(0, 0)])
total_space = 0

while queue:
    steps, position = queue.popleft()

    if steps > steps_max:
        continue

    total_space += 1

    for neighbor in [position - 1, position + 1, position - 1j, position + 1j]:
        if bottom <= neighbor.imag <= top and left <= neighbor.real <= right:
            if peta_laluan.get(neighbor) != "#" and neighbor not in visit:
                visit.add (neighbor)
                queue.append((steps + 1, neighbor))

print(total_space)

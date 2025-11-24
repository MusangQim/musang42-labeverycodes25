#######################################
#  ___                  _     _ ____  #
# / _ \ _   _  ___  ___| |_  / | ___| #
#| | | | | | |/ _ \/ __| __| | |___ \ #
#| |_| | |_| |  __/\__ \ |_  | |___) |#
# \__\_\\__,_|\___||___/\__| |_|____/ #
#                                     #
#######################################
# ------------------------PART I------------------------------------

from collections import deque

raw_notes = "L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"
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

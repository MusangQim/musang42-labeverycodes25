########################################
#  ___                  _     _ _  _   #
# / _ \ _   _  ___  ___| |_  / | || |  #
#| | | | | | |/ _ \/ __| __| | | || |_ #
#| |_| | |_| |  __/\__ \ |_  | |__   _|#
# \__\_\\__,_|\___||___/\__| |_|  |_|  #
#                                      #
########################################
# ---------------------------PART I-------------------------------

given_input = """
#.#.##.##.
..#..#.##.
.#.##.##..
#####.#...
##..#...#.
.##...#..#
..#..#.###
####...#.#
....#..###
.##.#..###
"""
clean_input = given_input.strip()
floor_rows = clean_input.splitlines()
floor_notes = [[ch == "#" for ch in row] for row in floor_rows]


def decide_tiles(floor_notes, r, c):
    diagonal_touch = [
            (r - 1, c - 1), # bucu atas KIRI
            (r - 1, c + 1), # bucu atas KANAN
            (r + 1, c - 1), # bucu bwh KIRI
            (r + 1, c + 1)  # bucu bwh KANAN
    ]

    diagonal_active = []
    for nr, nc in diagonal_touch:
        if 0 <= nr < len(floor_notes) and 0 <= nc < len(floor_notes[nr]):
            diagonal_active.append(floor_notes[nr][nc])

    count_active = sum(diagonal_active)
    current_tile = floor_notes[r][c]

    if current_tile:
        return (count_active % 2) == 1
    else:
        return (count_active % 2) == 0

def decide_round(floor_notes):
    return [
        [decide_tiles(floor_notes, r, c) for c in range(len(floor_notes[r]))]
        for r in range(len(floor_notes))
    ]

def decide_count(floor_notes):
    return sum(map(sum, floor_notes))

total_active = 0

# partt I mintak 10 rounds je
for _ in range(10): 
    floor_notes = decide_round(floor_notes)
    total_active += decide_count(floor_notes)

print(total_active)

from collections import deque

# Dragon knight moves (L-shape)
moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def simulate(grid, rounds):
    R, C = len(grid), len(grid[0])
    sheep_eaten = 0

    # cari posisi dragon
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'D':
                dragon_start = (r, c)

    # list of sheep positions
    sheep_pos = []
    hideouts = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sheep_pos.append((r,c))
            if grid[r][c] == '#':
                hideouts.add((r,c))

    # setiap giliran
    dragon_positions = set([dragon_start])

    for _ in range(rounds):
        # === Dragon move ===
        new_dragons = set()
        for r, c in dragon_positions:
            for dr, dc in moves:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C:
                    new_dragons.add((nr,nc))
        dragon_positions = new_dragons

        # === Sheep move ===
        new_sheep_pos = []
        for r, c in sheep_pos:
            nr = r + 1  # sheep move 1 down
            nc = c
            if nr >= R:
                continue  # sheep reached bottom → safe
            # jika dragon ada di situ dan bukan hideout → eaten
            if (nr, nc) in dragon_positions and (nr, nc) not in hideouts:
                sheep_eaten += 1
            else:
                new_sheep_pos.append((nr, nc))
        sheep_pos = new_sheep_pos

    return sheep_eaten

# =====================
# GRID INPUT (triple quotes)
# =====================
grid_text = """
...SSS##.....
.S#.##..S#SS.
..S.##.S#..S.
.#..#S##..SS.
..SSSS.#.S.#.
.##..SS.#S.#S
SS##.#D.S.#..
S.S..S..S###.
.##.S#.#....S
.SSS.#SS..##.
..#.##...S##.
.#...#.S#...S
SS...#.S.#S..
"""

grid = [line for line in grid_text.strip().splitlines()]

# simulate 3 rounds as example
print(simulate(grid, 3))  # output = 27 in example


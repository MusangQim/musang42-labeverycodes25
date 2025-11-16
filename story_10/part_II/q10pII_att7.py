def solve_dragon_sheep_game(board_str, rounds=20):
    """
    Simulate dragon and sheep game.
    
    Rules:
    - Dragon moves first (like chess king, 8 directions)
    - Then all sheep move down 1 square
    - Sheep on hideout (#) with dragon are safe
    - Count total sheep eaten across ALL possible dragon paths
    """
    lines = board_str.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    
    # Parse board
    dragon_start = None
    sheep = set()
    hideouts = set()
    
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == 'D':
                dragon_start = (r, c)
            elif char == 'S':
                sheep.add((r, c))
            elif char == '#':
                hideouts.add((r, c))
    
    # All possible dragon positions (set, not counting paths)
    dragon_positions = {dragon_start}
    total_eaten = 0
    
    # 8 directions for dragon (chess king moves)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for round_num in range(1, rounds + 1):
        # DRAGON TURN: Move to all reachable positions
        new_dragon_pos = set()
        for dr, dc in dragon_positions:
            for dy, dx in directions:
                nr, nc = dr + dy, dc + dx
                if 0 <= nr < height and 0 <= nc < width:
                    new_dragon_pos.add((nr, nc))
        dragon_positions = new_dragon_pos
        
        # SHEEP TURN: All sheep move down
        new_sheep = set()
        for sr, sc in sheep:
            new_r = sr + 1
            if new_r < height:  # Not escaped yet
                new_sheep.add((new_r, sc))
        sheep = new_sheep
        
        # COUNT EATEN: Sheep on dragon position and NOT on hideout
        eaten = set()
        for pos in sheep:
            if pos in dragon_positions and pos not in hideouts:
                eaten.add(pos)
        
        # Remove eaten sheep
        sheep -= eaten
        total_eaten += len(eaten)
    
    return total_eaten


# Example from problem
example = """...SSS##.....
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
SS...#.S.#S.."""

# Test with 3 rounds (expected: 27)
result = solve_dragon_sheep_game(example, rounds=3)
print(f"Example with 3 rounds: {result} (expected: 27)")

# Full 20 rounds
result = solve_dragon_sheep_game(example, rounds=20)
print(f"Example with 20 rounds: {result}")

print("\n" + "="*60)
print("PASTE YOUR INPUT BELOW:")
print("="*60)

# Your puzzle input here
your_input = """
....S..#.S#.S..SS.S..S.S...#S.SSS###SS.S.##...S.S#..##SS.SSS#..SS..#S##..#..S..#.#..#.S.S.SSS..S...SS
S#..#S.#SS#..S#S.###S..S..S.S.#..S.SS...#.....SS..#S.SS.#S.S....##S#..SS##.SS..###...#SS##....S.....S
.SS..#.SSS..S#..#SS#SS..S#S.#SSS#S.S..##..#.SSS...#S#.S#S..SSSS.##S.S##SS.##S.##.#.S#S#.S.S.SS.#..SS#
.S.##..S.S#...SS.#.#.#SS....S.#S.S....SSSS#S#S.SS.SS#S#.#S#.SSS.#S#..#S..SSS#S#####.SS#...........S#.
#..#....SS.....##SSSS.S#...##.#S##SSS.#S...#S.#S#S..S.#.#.S.....SS.#SS#.#S##..SSS#S#SSSS.S.S...S..S..
..S...#...SS.....S..S..S.S.S.S.S.S.#S#S.#SS.S####.S..S##......S#S#.S..S##S.S#..S#SS...#SS#.S..SS..S.S
##S#S#SS..#...#.S.#.S#..SS.......##.S#S#..S.SS.#SS..#SS##S.SSS#.#..#.#.#SS.#.S..#..#..#SS.SSSSS#SS#..
SS.SSS.SS.....S..SS...S##.#.S#.#S#...##.#S.##.SS.##..SS...#S...S.S.SS..S..S.SSSS#S.#S.##SSS.SS.....S.
S#.#....S.#S..SSSSSSS#SS...#S....#S.#.#SS.##..S#.#....#.SS.S#..S###.#S..SS....S.##.....#..SSSS...S#..
.#.SSSSSSSS#S.#.S.S#....SS#..#....#S.S#S.SSSSS.S.SS#...S#S#....SSSS#S.#S#..S#.#SS..SS#.#S##S#S.##...#
S#.SSS..SSSS..#.S.#S.S.#..S.##..#.#SS.S#.....S.S..#SSS...S.S.#.S..#SS.#..S..#.#SS#..SS...S.SS..S...SS
.#...#SS.#.SS#SS...S.S.SS..S.#.#..S.#SS.SS..S......#S......S#.S#SS.S.S#SS..#.SS.#SS..SSS##.SS##S.....
S.S.S#.S.S#..SS.S.S....S.SS...SS#.S#.#..#.S...S#..#.##.SSS#SS...S.S#...S.#..#.#..#...S#..S#S.......#.
.SS.S#.SS#..S.....S.S.#..S......#.##....#...S.S#S.#S#S#...S#.S.#S..#...S#..SS.#.S#..#S#.#.##..S..S#..
.S.#S.S..SSS..#.#S.##S.##.S.S.SS.SS.#SS#SS..#.S..#SS..S.S....S.SS..##......S.SSSSSS##S..SSSS.SS##S...
.#SS.S...SS.S.........S..S.S.#SSS.#S#.S.S#SS..#S..S##S.......S#..#S##S...S#.#.#..SSS...S#.SSS.#.#SS#S
.#SSS.#.#.#S..S.S...##.SSS..#.S#.S.S..S.##SS.S..#..S.....S.S.SSS.#S.##.SS.#.S#.S#.SS#.S.#SS.#..SS#.#S
.S.###.#.S.....S##.S.##S##SSS.S##.#S......S.##...S..S..#..SS.S..#S..SS....SS.#.#S...S.#...S.S..S.S.SS
#S.S..S#S.SSS..SSS..S#.S....S...S#.#S.S..S..#S.S.##.S..SSSS#....S...#S.S.#S..##..SSS.SSS......#....S.
..#.SS..S..S..#S#S......#.#...S.S##...#S..##SS#.#SS.....S..##S.S.S.SS#...S#S.#.##....#S.SSS..S..#S.#.
#S.S...S#SS...##...S.S#...#S...S.#S.#S#.S.S....SSS##..##.##.SS.#.#S#.S...#SS...#.S.SSSS#.S...S..#S.#.
..##S.SS.##..S.##S.S.SS#SS.S.#..S##S..SS.SS.S.S...S...#S#S.SS.##...S..#S.S.##SS##SS#.#..SS##....#S#.S
#S.....##S#S#S.S..S.#..SS.##S..S..##S..S....#..#S..S.S....##.S.SS.#.#..S.##S.#.S##S#.S##S#S...SS.....
.#S..S.S.S..S.SS#S..#.#...#.S.S####SSS.SS.S....SS#SS.#.#.##.S.#..S#S.S..SS...#S.S.S####..S.#..S#.S#..
..#.#.....SS#.S.#..S##.S.##..SSS..#SSSS.......##.S##SSSS#.S.#S..S#..S.###..S###.S.SS#S..S..S.S....S..
S.##.SSS#..SS.#S.S.S#..#..S#..S##S##SS.S...S###.S#.#.S##...SS.###S.#.#.#SS.S..S..SS#....S.#....#..S#S
#S...#.#..##..SS#SS.#.S.#.#S#S##SS.S#S...##S.S#SS##S.S.SSS..SS..#..#.SS#.S....S..SS.#.#S.##SS##....#.
S.#SS#..##..#S.#.SS.#S.S..S...S.S..###..S..S##.S#S..SS.S.......#.#.#.##..SS.SS.....#..SS#.S#####.#...
S#..S..#S#.#.S.#SSS#.#.......##..S#.S#S....#.#S#.S.SS.SS#....S#...SS......##.S..SS.S##...SS.S.S.S.##S
SSSSS..S#SS...##S..S..S###.SS.#.SS.S.#...SSS..S.S#.#S.SSSS.SSS...S.S........#S.###S.SS#SSSS#S#S....#S
#..SSS#..#SS.#S...SS#.#S....#.SS#SS.S#S#S..SS#.S#.SSSSS#S.SS#S.S#.##SSS....##SS.S.SS##S..S#SSSSS#.###
S#.S.#S.SS...##.#.SSS.#.S..SS...S.##SS..S.S..S.##.S.SS#.S.SS.S#S.S..#.S...S..#..S...#.#.#..#.#..#..SS
..#..SS..S##...SS#SS.#SS#S.#.#S.SS.#S.SSS..SS.#S.S#.S...#S###S..SS..SS.##.S#....S.SS#.SS...S.#..#..S.
#S.#.#S.S..SS..#S.S#S#.....##.SSSS##S.S.S.#..##.#S.S###SS.#SSS#SS.S.#..S.#.S#.....S#.S.##S.S.#..S.SSS
##...#S..#S..#SS#SS##S...S#..S#.#.#.#..SS#.S.#.#SS.S.#S##SSS#...S#S#.S...SS..SS#..#S##..S.#S..#SS.S.#
SS.S..#S......#..S#SSSS.S.#S.S...S.S..##.##SSS...S...S#S..S.S.S.....#S......S........#.SS#.SS.S#S#SSS
..S.S..S..SSS#S.S...#S.S.#.S.#.#S..#SSS#S#...#....S.S#.S.#..#..S....#S.#SS##..#....#.SSSSS#.#.SSSSSS#
#.#S#.S#..S.....##S#.S.S..#..S#.#..SSS##S.SSS#..SS#.S...#....SSS##...S.S#SS#.#SS#S#S#.#..S.S#SS.#...S
...#S..S.SS#SS#SS.S#.S.S##S#S#.S#.S.SSS.S...#S#S##SSS.#...SSS.#.#..S.SSS..SS#.#.#.SSS#...#.SS.#S..S.S
#S####..##SSS....S.#.SS..SS...#S.SS.......#.SS..S##.S#S.SS.S#SS.S..#.S.##.S#.S#.##.S.#.#.S.....SS.#.S
SSS..S##.#.S.#..#S##..##..SS...S#S#SS.S.S..S.....#..SS.#.#.SSS.#..#.SSS#.SSS.SSS.......#.#S.S..##S#..
S...S#..SSS.S.S#S#...S.S.S.SS...SS..#.SSSS#.#.....#S.S.S#SSS..SSS#S...SS...S.##..SS#.SS..S.S#.S#.#S.S
#..S.#.#.#S#.SS.S.SSS..#.S.S.S#S..#.#.S..S....SS..S.#.S.S..#SS#.S.S#...S#.S#.....##SSSS.S#.S.SS.S#.SS
#.#.S.S.#.SS.S...SS#.SS###S..SS##..#.##SS......S#S.#SS.S#...S.#....#S...SS.S....#####.S.#.SS..S#.#SS.
SS..SS#SSS#.#S#.S.#...#SS#.#...#.S#.#S.....S#.#S.SS.#...##..#.#S..#.SS#.S.#S....#..S..##SS.#.SSSS#..S
SS.#.#S.S#..##.S#..SS.#..S....SS##S.S..S.#....#...##.S.S#....S#S.SS.S#S.S#SSSS.#...#.....S#SS.#S..#..
..SSS##.SS.S#..##SSS#.SS#S#.S..S.SS.SS..S.S.#S.S.#...#...S.S..S..#S...SS#..#..S...S.S.S.S#.....#S####
..S.#..S#.S.SS........SSSS###..#.#S...S#...####...S.S#.#SSS##..S..SSS.S#S##..#S.#..#SS..S.S.#...SS#.S
....#S...#....S..#..SS#.SS...#SSS..S.S#S#S....#.###SS...S#.S.#...SS#...S###S..#SS.S..#SSS.#S.S..#.#S.
#..S###S.#.#SSSS..#S..#SS.#.S....S.SS.S.SS..#..#SSS.S#.SS.#..SSSSS##..#.S..S#S..S#SSS..S.SS.##.SS...S
.#S#.#...S..SS...S...#S.S..SSS....#.....#S.#.SSS..DSSS.S#..#S.S.S...##.##.#.#.S.S#S....SS.S.S.S##.S.#
#SS..##..S.#S#SS.#..SS##..#...#.S..#S...###...#...S.....S#...S....#..#S.#.#..#SSS#S...##.S#SSSSS...#S
.SSS.##S###S##.#S#..SS.S..##S##SSS#.S.S.##.#..SS...S.S#.S##SSS..#.S#S.SS..SSS.SS.....#.#..#.S.SSS...S
.S#..S..S..S...SS#..S#S..S.SS..SS.#.#.#.#..SSSS.SSSS.#S.#SS.##.SS.S.S.S.S....S#S.S...#.#SS..S#..S#S.#
#S#S#..####.S.SS.#.S.......#..SS#S...S.#S##.S.#.......S..SS..SSSSS#S.#....#...S.S..S#S.S.#S#..SSS.##S
...S.S#S#SS#S.#S..####..#S..#S...S..#S.#.#S.S#S...#SS..S.SS.##......S####S......#.##S..S.S##S...SSS.#
#.SS.#S..##....S.#.SS..SSSS.S...#.....SS.S#..SS.#S###..SS#S...S..#S#.S..#.S.SS.S.S.#..S.#S..##SSS.SS.
SSS##......#SSS....#S#....###S..S#.SS.#.....S..SS..##S##.SS...#..S#.S..SSSS..S.S.S#..SSSS.#S#S..SSSS.
##.#S#S..#..S.##...#S..##.S.S.#SSS.S..S.##SS.#S#.SS..S.##.#S..SS#S.##SS.S.S#SS.S.#.S...#S..S....#S.#.
S#..SS#S#S.S.#S.#S#S.#..S#.#SS.S.##...##.#.S.SS.#SS...S.S..S...#...S.SS###.....#.SSS....SS...#..#SS..
...S.SSS.S#S..#SS.#SS#..S..#...#..SS..SSS..SSSS...S##SS.S##S.#S#...S.##..#.S..SS.#..S#...#.SS.....S.S
#S....SS..SS..S#.##SS#S#.S....SS##S##..#S..S.##......SSSSSS#.S##SS#S#.S......S.#S..S.S.SS..####SS#S.S
SS.##.#.S.S#S.SSS#..SS.#S.SS..S.S##.##...S#.S....SS.#S.##S.#..##.##...####.#.#...S..SS..SSS.#.S#..#S.
..S..S.##.S.....SSS.SSSSS.SS.S#S#.S.SS#.#####......##....S#.###.#S###..SS###SS##SS#...SS.....S.#.##S.
.#S.SSS...SSS.#S#S###...#...#.##..S.S..S...#SS#SSS.##...SS##S#SS...S...S.S.....#S####..........SS.SSS
...#S#.S.#..SS.S.#SSSSSSS..S#.S#...#...S#SSS...SSSSSS.S.S..SS.##.SSS#S.SS#.SS.#..S.S.S..#S..SS.S#....
....S..SS.#S#SSSS.#..#..#.S.##..SS.#..#.S...S#SS...#.SS...###.S.#.#SS...S.S...S.#SS..S...SS...SS..S#.
.S#.#..##..SS.S#..##SS#.S.....#.##.#.#S.SS#...SS.SS...#...S.#S....S#S#.S..S#..#SSSS#.S####.#SS##S.###
..S#SS#SSS#.#.SS..SS.....S.#..#SS.SS.#.#S.#S...S...##S#SS..S#.S..S..#.###.S.S..S.S.SSSS##...SSS#S..#.
#.S#.S....S#S.###.........SS.S#..SS.#...#...S.#S.S.#.S.#..#S#SS...SS.....S..#.S#SSS.S.SS.S#.....S#..S
S.##SS..S#..SS#S....#SS#..S##.S#.S..##S.##..#..#SS.##.SS.##..SS.##.##S##SS..S###.#.#S.S.S.S.#SSSSS#.#
...#.#SSS..S#SS.SSS#..##...S#SS...#SS.S...#S#....#S##.##.#S.#S#.....S#S.SSS##..S#S#..SS##.S.S.#S#.S#S
S.#SS..#S.#SS#...SS#.S#S.S..SS.S....S..SS..S#S.#.S.S.#.#S#..SS.S.SS#S....S....##..##..SS.S.SS#SS.##..
.S....#S#.S.S.##..SSSSSS....S.#..S#.S###.S.S.SS..#SS.S.S#..#...#S..SS#....#....SSS.SSS#.SS.###.#SS..S
S#..SS.SS..S#SSS.##S.S.SS#.SS..SSS...#.SSS#SSSS..S.#.S.#S#.#.S##...SS##..#.S.#...##S#....S...S.SS#.#.
S...#S.SS..SSS##S...#SS.#S.#S#S.....#S#.S.S....S.....S#..#S.SS..S.S##..SS...S#...#.#...S####.#SS....#
.SS.SS#.SS.##....#.SSSS#.#....#S#.S..S.#SS..###.S.#....S#.S#..S..S##.S#.##.S.##SSS.#.#.....#S.SS.#.#S
.S.#S#S.#.#..S#S#SS..SSSS#S..SS.S..##..#S.SS#.S...S...S#..S.S.#.SSSS..##....#....SS.S.##...#S..#..#.#
#S.SSS#S...S#.#SS#..S#.S.S...S.S#.S...#SS.##.S.S#.#.SS.......SS.S.SSSSS...##..S.SSS...S.SS...S.SS..##
#S.S...SS#..SS#.S##......S.S.S.S.#S.SS.#.SS#S#SSS..S.##S.S#..SSSS..#S#..S.#S.SS..S.S.#SS#.SS.#S#.S.#.
...#S.#.S.#SSS....SSSS.S.SSS.SSSS#..##SS.S.#S....S.S.#SSS..SSS.#.#...S.#.#S.SS...SS.SS.S#.SSS#S#SS#.S
SS...SS...#.##S...S...#.SS.S#.S#...S.SS##.S#S.......#SSS##.#S..#S.S##SSS.##.#S#S.S.S.S..SS#S#..S##..S
...#SS#.SSS.SS..S.....SSSSS#...S.#SS..SSS.S.S.#SSSS..S.S.S.S#SS.#S.SS.#S...S..S..#S.S.#SS..S.S..S..SS
#S..#S.SS#.S.#S.SSSSS#.##S..S.S.S.SS.S.S.SSS..#SS.S.##...SS.S..SS#S#S#S.SS#SS..S.S.S.S.SSS.S.S#S.#.S.
S..SSS..SS..#S##S..#.S.S.S..S#S......#S..S.S..#.#.SSS#SS.S.SSS#.S...#.#.S#S..#.....###..SS#...S..SSS.
.#S..S.S..S.S#S..###..##.SSSS.#SS.S...S#S.S.##...S...SS.#.S..SS.SS##S.###....SSSS.#.#S#.SS#.S#..SSSS.
S##S...S..#.#..S#S.S##SS.SS#..S.S..S.S#.#.S.SSS..##S#.#S##S#S#.##SSSS#.S.SSS#S#.SS.SS..S.SSSS...S.S.S
S.###.S.SS#..SSSSSSS#S.#S...##SSSS.#S.......#.#.S..SSS.S....S.#.SSSS##..SS..#S#S...SSS#.#...#.S.#S...
S.#..S.S#S.#.S.SS#.SS.#..S.##S.....#..S#S##S..#.S##S##.SSSS##.SS.S...#SS.SS#.#..S..SS...#.SSS..#.S#..
...#.S.#..S###S..#...#S#..SS#.##S...SSS.S.S..#..S##.#.S#.#.S.S#.#.###..#.S##S##...#.....S........#.#.
S.##.S....#...#SSS.S...S.....##S.#S.#SS#....#.S##....#..#SS#.S.#S..S#.SS..S.#...###SS...S#..#S...SSS#
....SS.###.S.#..#...##...S#S..S.#S..#S.S#.#.S..#.#SSSS#.#S.S..S.#S.#...##SSS.SS#S...#S.S.#.#SS.#S....
S.SS...S..#.#..##.S#..SS.#..#.#S...SS.#.##...SSS....S.S...S.S..S.#.#S.S.....#SS.SSS..#S..##..#SSSS#S#
...S#.S.SS.S..#.##SS..SSS.S..S#.#SS#SSSSSS.S..S...SSS.SS...#SS..#S.#..S#....SS..S....#..#.S.S##.S#.S.
..##.#S....S..#.#S..SS.#S.S..#..###..S....SSS...S.SSS#.#SSS.#SS.#.......S..S.SS#.#SS.SSS#S.#S#..#.S..
.S.SS.S.SS#S###.#S...#S#..S.S.#.S#SS....#..#S....S.SSS.S....S..S.##....S.#SS#SS....S###..#S..S#SSS##.
#.S#S.S.S.#S.#....SSS#.#..SSS.##..SS#..##S#S.#S.###.S...SSS....S.S...S##....#SS#..SS.S...S#.#S....#SS
##S..#.S#.S##..S##..#..#.#...S..#SSS..S......SSS.#.S.S...S#S..SSS....###S.SS#..#S.##.SS.#..#.S.S...S#
.SS##S..SSSS.S...SS.S..S#..S#S.....S#.#SS#S.##S.SS#..S.S.S#S...##.##S.S.S.#S...S.SSS...#S.#S#..S..S#.
#..SSSSS..S.SSS#..#.S.SS.##.......SSSSS...#.#...S#.SS.S.S#SS.SS...SSS#.SS..SS#..#.....#S.S###S#....#.
#S.S.SSSSS#S..#SS#..SS.#S.S#.#SSSS..SS.#S..S#SSS#SS...#.#.S.SSSS#S..#S#....SS...#SS..#..S..S.#S.#S.S#
"""

if your_input.strip():
    answer = solve_dragon_sheep_game(your_input, rounds=20)
    print(f"\n🎯 ANSWER: {answer}")

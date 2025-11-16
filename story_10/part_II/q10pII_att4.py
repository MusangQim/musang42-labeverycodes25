def simulate_dragon_sheep_game(board_str, rounds=20):
    """
    Simulate the dragon and sheep game for given number of rounds.
    Returns total number of sheep that can be eaten across all dragon move variants.
    """
    lines = board_str.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    
    # Parse initial board
    dragon_pos = None
    sheep_positions = set()
    hideouts = set()
    
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == 'D':
                dragon_pos = (r, c)
            elif char == 'S':
                sheep_positions.add((r, c))
            elif char == '#':
                hideouts.add((r, c))
    
    # Track all possible dragon positions with their count
    dragon_positions = {dragon_pos: 1}
    total_eaten = 0
    
    # Dragon move directions (8 directions like chess king)
    dragon_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for round_num in range(rounds):
        # Dragon turn: expand all possible positions
        new_dragon_positions = {}
        for (dr, dc), count in dragon_positions.items():
            for dmr, dmc in dragon_moves:
                new_r, new_c = dr + dmr, dc + dmc
                # Check bounds
                if 0 <= new_r < height and 0 <= new_c < width:
                    new_dragon_positions[(new_r, new_c)] = new_dragon_positions.get((new_r, new_c), 0) + count
        
        dragon_positions = new_dragon_positions
        
        # Count eaten sheep at each dragon position
        for (dr, dc), count in dragon_positions.items():
            if (dr, dc) in sheep_positions:
                # Check if it's a hideout
                if (dr, dc) not in hideouts:
                    total_eaten += count
        
        # Remove eaten sheep (not on hideouts where dragon is)
        sheep_to_remove = set()
        for sheep_pos in sheep_positions:
            if sheep_pos in dragon_positions and sheep_pos not in hideouts:
                sheep_to_remove.add(sheep_pos)
        sheep_positions -= sheep_to_remove
        
        # Sheep turn: move all sheep down one row
        new_sheep_positions = set()
        for sr, sc in sheep_positions:
            new_r = sr + 1
            # Only keep sheep that haven't escaped (reached bottom and moved off)
            if new_r < height:
                new_sheep_positions.add((new_r, sc))
        sheep_positions = new_sheep_positions
    
    return total_eaten


# Example from the problem
'''
example_board = """...SSS##.....
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
'''
example_board = """....S..#.S#.S..SS.S..S.S...#S.SSS###SS.S.##...S.S#..##SS.SSS#..SS..#S##..#..S..#.#..#.S.S.SSS..S...SS
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
#S.S.SSSSS#S..#SS#..SS.#S.S#.#SSSS..SS.#S..S#SSS#SS...#.#.S.SSSS#S..#S#....SS...#SS..#..S..S.#S.#S.S#"""

# Test with 3 rounds (should give 27)
result_3 = simulate_dragon_sheep_game(example_board, rounds=3)
print(f"Example with 3 rounds: {result_3} sheep eaten (expected: 27)")

# Full simulation with 20 rounds
result_20 = simulate_dragon_sheep_game(example_board, rounds=20)
print(f"Example with 20 rounds: {result_20} sheep eaten")

# Read your actual puzzle input
print("\n--- PASTE YOUR PUZZLE INPUT BELOW ---")
print("(Run this code with your input to get the answer)")

#####################################
#  ___                  _       _ _ #
# / _ \ _   _  ___  ___| |_    / / |#
#| | | | | | |/ _ \/ __| __|   | | |#
#| |_| | |_| |  __/\__ \ |_    | | |#
# \__\_\\__,_|\___||___/\__|___|_|_|#
#                         |_____|   #
#####################################
# ---------------PART I-------------------------------------

def simulate_ducks(columns, rounds):
    """Simulate duck movement for given rounds"""
    columns = list(columns)  # Make a copy
    
    print(f"Round 0: {columns} -> Checksum: {calculate_checksum(columns)}")
    
    for round_num in range(1, rounds + 1):
        # Each round: compare adjacent pairs left to right
        for i in range(len(columns) - 1):
            # If left column has MORE ducks than right, move one from left to right
            if columns[i] > columns[i + 1]:
                columns[i] -= 1
                columns[i + 1] += 1
        
        checksum = calculate_checksum(columns)
        print(f"Round {round_num}: {columns} -> Checksum: {checksum}")
    
    return calculate_checksum(columns)

def calculate_checksum(columns):
    """Calculate checksum: sum of (position * count)"""
    return sum((i + 1) * count for i, count in enumerate(columns))

# Your input
input_data = [2, 1, 17, 12, 19, 9]

print("=== Simulating 10 rounds ===\n")
final_checksum = simulate_ducks(input_data, 10)
print(f"\n✓ Final answer after 10 rounds: {final_checksum}")

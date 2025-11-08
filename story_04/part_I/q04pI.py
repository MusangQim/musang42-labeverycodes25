#############################################
#  ___                  _       ___  _  _   #
# / _ \ _   _  ___  ___| |_    / _ \| || |  #
#| | | | | | |/ _ \/ __| __|  | | | | || |_ #
#| |_| | |_| |  __/\__ \ |_   | |_| |__   _|#
# \__\_\\__,_|\___||___/\__|___\___/   |_|  #
#                         |_____|           #
#############################################
# ---------------------PART I--------------------------------------------------------------------
'''
each gear's number reperesent to number of teeth it has , if gear 2 , have 2 teeth and so on lah..
so recreate formula:
    turn next gear = turn previous gear x (teeth previous / teeth next)
    given 2025 turns as 1st gear
'''
def formula(gears, turn_first=2025):
    turns = turn_first
    for i in range(len(gears) - 1):
        turns *= gears[i] / gears[i + 1]
    return round(turns)

example_gears = [128, 64, 32, 16, 8]
print(formula(example_gears))

another_example_gears = [102, 75, 50, 35, 13]
print(formula(another_example_gears))

question_gears = [1000, 972, 943, 927, 918, 909, 904, 898, 880, 858, 831, 827, 811, 786, 761, 751, 722, 720, 701, 676, 665, 647, 623, 603, 580, 559, 557, 555, 546, 521, 496, 470, 452, 443, 427, 403, 378, 363, 342, 327, 325, 302, 276, 256, 237, 224, 213, 201, 200, 189]
print(formula(question_gears))

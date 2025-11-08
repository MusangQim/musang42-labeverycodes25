#############################################
#  ___                  _       ___  _  _   #
# / _ \ _   _  ___  ___| |_    / _ \| || |  #
#| | | | | | |/ _ \/ __| __|  | | | | || |_ #
#| |_| | |_| |  __/\__ \ |_   | |_| |__   _|#
# \__\_\\__,_|\___||___/\__|___\___/   |_|  #
#                         |_____|           #
#############################################
# ---------------------PART II-------------------------------------------------------------------
'''
part I nk tau how many turns for last gear turns kan..
part II nak tau number of full turns untuk 1st gear plak, target kita bagi 10x10^12
10 000 000 000 000 times
formula mcm ni lah:
    1st_turn = target x (last teeth / first teeth)
'''
def formula_pII(gears, target=10000000000000):
    first_gear = gears[0]
    last_gear = gears[-1]
    result = (target * last_gear+ first_gear - 1) // first_gear
    return result

ex1_gears = [128, 64, 32, 16, 8]
ex2_gears = [102, 75, 50, 32, 13]
question_gears = [961, 956, 951, 932, 913, 884, 865, 856, 842, 831, 829, 804, 801, 791, 763, 752, 740, 721, 703, 681, 662, 644, 630, 614, 610, 601, 581, 562, 558, 556, 528, 519, 504, 498, 475, 462, 447, 423, 403, 396, 386, 362, 353, 339, 332, 319, 304, 297, 284, 247]

print("Answer for example 1:", formula_pII(ex1_gears))
print("Answer for example 2:", formula_pII(ex2_gears))
print("Answer for question given:", formula_pII(question_gears))


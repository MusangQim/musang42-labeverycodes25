#########################################
#  ___                  _       _ _____ #
# / _ \ _   _  ___  ___| |_    / |___ / #
#| | | | | | |/ _ \/ __| __|   | | |_ \ #
#| |_| | |_| |  __/\__ \ |_    | |___) |#
# \__\_\\__,_|\___||___/\__|___|_|____/ #
#                         |_____|       #
#########################################
# --------------------------PART I-------------------------------
"""
list_notes = """
72
58
47
61
67
"""
"""

list_notes = """
908
108
751
642
123
253
408
712
633
885
709
616
343
665
969
273
646
574
395
245
848
758
334
101
120
267
778
893
104
420
392
661
136
220
469
873
664
479
816
887
190
349
148
699
983
399
779
468
260
820
"""

clean_notes = list_notes.strip()
notes = clean_notes.splitlines()

roda = [1]

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

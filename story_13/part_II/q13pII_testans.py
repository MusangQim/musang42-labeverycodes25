#########################################
#  ___                  _       _ _____ #
# / _ \ _   _  ___  ___| |_    / |___ / #
#| | | | | | |/ _ \/ __| __|   | | |_ \ #
#| |_| | |_| |  __/\__ \ |_    | |___) |#
# \__\_\\__,_|\___||___/\__|___|_|____/ #
#                         |_____|       #
#########################################
# --------------------------PART II-------------------------------
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
9107-10946
4143-12761
5246-13053
6715-15675
9067-11751
5512-7045
4100-12974
7730-14684
9046-16931
6338-14373
4958-14537
8372-15874
1079-8923
1003-6889
3118-9270
2622-8934
3362-12091
7243-8504
7815-9338
5732-7503
9400-12410
7788-16180
9280-12160
2282-8138
5710-7926
1417-9012
9565-11845
5021-11911
7704-15741
3964-7161
3741-12958
9051-10796
6435-13160
7135-14052
3834-11037
9631-18820
5401-14804
1172-11149
9431-17687
2832-8351
8855-14701
9728-13280
4594-11631
8819-14940
9568-18744
9838-17586
7321-15098
3710-5744
2896-3953
4077-7875
"""

clean_notes = list_notes.strip()
notes = clean_notes.splitlines()

roda = [1]
put_right = True

"""
for start_num, end_num in notes:
    if start_num <= end_num:
        expand_num = list(range(start_num, end_num + 1))
    else:
        expand_num = list(range(start_num, end_num - 1, -1))
"""

for n in notes:
    value = int(n)
    expand_num = [value]

    if put_right:
        roda += expand_num
    else:
        roda = expand_num + roda

    put_right = not put_right

no_of_steps = 20252025

start_position = roda.index(1)
final_position = (start_position + no_of_steps) %len(roda)

print(roda[final_position])


# ----------------PART I punya------------------------------
"""
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
"""

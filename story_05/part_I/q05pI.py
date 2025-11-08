############################################
#  ___                  _       ___  ____  #
# / _ \ _   _  ___  ___| |_    / _ \| ___| #
#| | | | | | |/ _ \/ __| __|  | | | |___ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| |___) |#
# \__\_\\__,_|\___||___/\__|___\___/|____/ #
#                         |_____|          #
############################################
# ---------------------PART I-------------------------------------------------------------------

numbers = [8,4,2,4,8,3,9,4,2,3,4,7,4,7,8,2,9,6,1,1,4,5,3,3,7,1,9,5,6,1] # [5,3,7,8,9,10,4,5,7,8,8]

spine = []
left_right = []

for num in numbers:
    placed = False
    for i in range(len(spine)):
        spine_num = spine[i]
        left, right = left_right[i]
        if num < spine_num and right is None:
            left_right[i][1] = num
            placed = True
            break
        elif num > spine_num and left is None:
            left_right[i][0] = num
            placed = True
            break
    if not placed:
        spine.append(num)
        left_right.append([None, None])

quality = int(''.join(str(n) for n in spine))
print(quality)

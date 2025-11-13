############################################
#  ___                  _       ___   ___  #
# / _ \ _   _  ___  ___| |_    / _ \ ( _ ) #
#| | | | | | |/ _ \/ __| __|  | | | |/ _ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| | (_) |#
# \__\_\\__,_|\___||___/\__|___\___/ \___/ #
#                         |_____|          #
############################################
#------------------------PART I---------------------------------------
'''
quest ni macam menjahit, but this using 8 pins/nails
setiap nail ade number, 1 -> 8 ikut clockwise
setiap benang yang lalu centre dikira 1 , berikutan kepada list number
'''
def pass_tengah(sequence, n):
    count = 0
    for i in range (len(sequence) - 1):
        a, b = sequence[i], sequence[i + 1]
        if abs(a - b) == n // 2:
            count += 1
    return count

# list_number = [1,5,2,6,8,4,1,7,3]
question_number = [1,32,16,32,16,32,16,32,16,32,16,32,13,27,11,27,11,27,11,23,8,21,5,21,2,19,3,19,3,19,7,23,7,23,7,23,7,19,3,16,4,20,8,24,9,23,7,23,5,18,2,18,2,18,4,19,4,20,4,23,7,22,6,22,6,20,5,23,11,30,14,1,17,32,16,32,14,30,12,28,12,28,13,29,12,27,11,23,3,16,32,16,30,14,30,17,1,17,4,20]

# print(pass_tengah(list_number, 8))   # 8 is nails contoh je , guna 32 utk jawap quest
print(pass_tengah(question_number, 32))

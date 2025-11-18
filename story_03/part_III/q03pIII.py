###########################################
#  ___                  _       ___ _____ #
# / _ \ _   _  ___  ___| |_    / _ \___ / #
#| | | | | | |/ _ \/ __| __|  | | | ||_ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| |__) |#
# \__\_\\__,_|\___||___/\__|___\___/____/ #
#                         |_____|         #
###########################################i
# ---------------------PART II-------------------------------------------------------------------
'''
On my opinion...ade banyak kotak and pelbagai size
ni list kotak = 4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77
Kotak ade 32 , Mushroom ni nk 20 crates , tak nak kecik sangat sbb ade ruang utk udara, lagi 12 ignore dulu focus on mushroom
'''

# kotak = [4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77]
# kotak_list = "153,2,113,178,68,30,53,46,131,89,161,81,64,42,101,35,31,140,176,128,40,93,173,55,148,143,1,150,75,23,130,26,119,184,145,72,162,20,183,22,175,174,109,106,106,48,59,164,10,154,143,18,5,168,56,58,50,125,128,176,78,5,57,123,97,135,20,66,5,100,122,88,62,81,37,120,111,71,21,164,118,5,106,32,140,97,122,85,136,115,58,6,83,14,152,20,80,141,7,17,71,48,64,82,69,113,47,125,178,7,52,16,20,144,83,25,188,65,124,140,138,12,142,47,39,34,80,25,188,24,43,22,113,82,137,49,37,145,52,165,24,53,178,5,93,177,94,105,170,158,120,135,158,68,140,165,143,157,128,66,33,48,126,131,121,186,2,13,66,10,158,129,67,175,117,54,26,14,123,47,84,156,6,128,111,137,55,79,70,175,10,21,102,116,26,26,63,171,26,147,45,67,161,165,105,26,131,55,3,94,22,156,20,58,55,130,161,110,184,18,41,139,12,74,167,62,137,162,23,98,50,179,69,71,81,57,48,156,90,85,93,60,170,149,169,80,127,147,165,153,115,52,143,149,119,114,66,59,112,168,102,114,70,45,56,43,141,93,60,59,38,89,21,96,171,12,84,11,111,128,1,98,131,65,58,139,188,53,175,167,44,43,44,77,40,55,161,94,133,180"
kotak_list = "4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77"

kotak = list(map(int, kotak_list.split(',')))
mushroom_kotak = list(set(kotak))
mushroom_kotak.sort()
kotak_kecik = mushroom_kotak[:20]
kotak_kecik_descending = sorted(kotak_kecik, reverse=True)

total_size = sum(kotak_kecik)

print("20 kotak utk mushroom:")
print(" > ".join(map(str, kotak_kecik_descending)))
print("\nTotal size:", total_size)


# -----------------------------------------------------------------------------------------------
# wanna give up but cannot , this is good for me , continue trying....
'''
kotak_sorted = sorted(kotak, reverse=True)

mushroom_kotak = kotak_sorted[:20]

for i in range(19, -1, -1):
    for j in range(20, len(kotak_sorted)):
        if kotak_sorted[j] < mushroom_kotak[i]:
            if i == 19 or kotak_sorted[j] <= mushroom_kotak[i-1]:
                mushroom_kotak[i] = kotak_sorted[j]
                break

kotak_counter = {}
for x in kotak:
    kotak_counter[x] = kotak_counter.get(x, 0) + 1

for x in mushroom_kotak:
    kotak_counter[x] -= 1
lebih_kotak = []
for x, y in kotak_counter.items():
    lebih_kotak += [x]*y

total_size = sum(mushroom_kotak)

print("20 kotak utk mushroom:", mushroom_kotak)
print("Semua size?:", total_size)
print("Kotak lebih?:", lebih_kotak)
'''

# -----------------------------------------------------------------------------------------------
# damn so hard to understand as beginner dho

'''
min_total = float('inf')
min_combo = None

# kita main looping utk set 20 kotak
for combo in combinations(kotak, 20):
    total = sum(combo)
    if total < min_total:
        min_total = total
        min_combo = combo

mushroom_kotak = list(min_combo) # ambik 20 kotak dari 32 tadi
mushroom_counter = Counter(mushroom_kotak)
lebih_kotak = list((kotak_counter - mushroom_counter).elements())

total_size = sum(mushroom_kotak)

print("20 kotak utk mushroom:", mushroom_kotak)
print("Semua size?:", total_size)
print("Kotak lebih?:", lebih_kotak)
'''

# -----------------------------------------------------------------------------------------------
# try try try tryyyyyyyyyyyy
'''
kotak = [4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77] # 32 kotak
kotak_sorted = sorted(kotak, reverse=True) # susun beso ke kecik

mushroom_kotak = kotak_sorted[:20] # ambik 20 kotak dari 32 tadi
lebih_kotak = kotak_sorted[20:] # lebih tu tak pakai

total_size = sum(mushroom_kotak)

print("20 kotak utk mushroom:", mushroom_kotak)
print("Semua size?:", total_size)
print("Kotak lebih?:", lebih_kotak)
'''

###########################################
#  ___                  _       ___ _____ #
# / _ \ _   _  ___  ___| |_    / _ \___ / #
#| | | | | | |/ _ \/ __| __|  | | | ||_ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| |__) |#
# \__\_\\__,_|\___||___/\__|___\___/____/ #
#                         |_____|         #
###########################################i
# ---------------------PART I--------------------------------------------------------------------
'''
Task dia mcm kotak yang banyak size berbeza actually, dlm kotak besar ade kotak kecik and dlm kotak kecik ade kotak lagi and so on.. 
that the short story utk quest ni (tapi mcm ade related things dgn youtube cite pasal cubic problem , is that????
'''
# kotak = [10,5,1,10,3,8,5,2,2] #(ni contoh dari quest bagi) answer is 29
kotak = [85,65,4,74,39,57,87,61,54,68,32,57,2,23,45,65,32,61,16,38,11,42,44,86,7,65,13,65,89,53,11,36,84,72,2,63,81,85,26,18,85,52,54,17,32,26,50,38,25,38,10,55,40,25,84,43,16,16,10,6,15,48,80,74,14,19,12,12,41,56,25,12,44,44,22,32,8,37,59,33,66,17,78,7,75,55,58,34,84,42,7,61,31,9,63,16,75,26,33,2]

kotak.sort(reverse=True)
print("Kotak sorted:", kotak)

#start dari awal 0
max_sum = [0] * len(kotak)

for i in range(len(kotak)):
    max_sum[i] = kotak[i]
    print("Check:", max_sum[i]) # ni just check dari beso to kecik je
    for j in range(i):
        if kotak[i] < kotak[j]:
            max_sum[i] = max(max_sum[i], kotak[i] + max_sum[j])

print("Largest sum of kotak set ialah:", max(max_sum))

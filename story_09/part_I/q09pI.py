############################################
#  ___                  _       ___   ___  #
# / _ \ _   _  ___  ___| |_    / _ \ / _ \ #
#| | | | | | |/ _ \/ __| __|  | | | | (_) |#
#| |_| | |_| |  __/\__ \ |_   | |_| |\__, |#
# \__\_\\__,_|\___||___/\__|___\___/   /_/ #
#                         |_____|          #
############################################
# ---------------------------PART I---------------------------
'''
this quest play with DNA, so ade 4 symbol A T C G
ade order 1:2:3, satu scale ialah child , yang lain parents,
child mesti ikut salah satu parents
setiap scale , 32 huruf
Parents	Child	Maksud
A & A	A	✔ OK — anak ikut parent
A & T	A/T	✔ OK — ikut salah satu
A & T	C	❌ FAIL — child pelik
C & C	C	✔ OK — semua sama
C & C	G	❌ FAIL — tak boleh diwarisi
task:
    find child's scale and kira degree of similarity
'''
'''
ex_scales = [
        "CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG",
        "CTTGAATTGGGCCGTTTACCTGGTTTAACCAT",
        "CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG",
]
'''
scales = [
        "CTGATAGCACTCGAAGTCATTAGTCTTGCGCCTCAGGGGGTTGGTTCTTCAACTTTAACAGTCTCAATCACACAGTTAGACACCGGTTGGTGTCCAAGCTAGTTTATAAACGAGAGACGTTTTGCAGA",
        "CCAAGATAATCTCGGCAGTCAAAGCTTACCATAGGGTTGAGCCGGTCACCCGCCAGCCTACGGGAGTATGATGTACTAATCGCTGATGCTTCTGACCAACGGTGTTAACGGGAGCCTGCCTCTTGGGC",
        "CCGAGAGCATTCGGACAGTTTAGGCTTACCCTTGAGGGGGTTCGTTCATCAACCTGACTAGTCTCAATCACTCAGCTAGTCACTGGTGGTTCTGACAAATAGTTTTTACACGAGCCACGTTCTTCAGA",
]

for i in range(3):
    candidate = scales[i]
    others = [scales[j] for j in range(3) if j != i]
    if all(candidate[k] == others[0][k] or candidate[k] == others[1][k] for k in range(len(candidate))):
        child_idx = i
        parents_idx = [j for j in range(3) if j != i]
        break
matches1 = sum(child == scales[parents_idx[0]][k] for k, child in enumerate(scales[child_idx]))
matches2 = sum(child == scales[parents_idx[1]][k] for k, child in enumerate(scales[child_idx]))
similarity = matches1 * matches2

print(f"Child: Scale {child_idx+1}")
print(f"Matches with Parent {parents_idx[0]+1}: {matches1}")
print(f"Matches with Parent {parents_idx[1]+1}: {matches2}")
print(f"Degree of similarity: {similarity}")


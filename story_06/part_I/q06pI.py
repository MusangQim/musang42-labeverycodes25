############################################
#  ___                  _       ___   __   #
# / _ \ _   _  ___  ___| |_    / _ \ / /_  #
#| | | | | | |/ _ \/ __| __|  | | | | '_ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| | (_) |#
# \__\_\\__,_|\___||___/\__|___\___/ \___/ #
#                         |_____|          #
############################################
# -----------------------PART I------------------------------------------------------------
'''
so for this quest,
Aa = sword fight Bb = archery Cc = magic
uppercase A B C = mentors
lowercase a b c = novices
'''
# ex_notes = "ABabACacBCbca"
notes = "ABCaCbBcAbBABCCCbbCCbAcCBAbaAcBBCacBCcAAAcaaABCAcaBBBcaCACBaaABAbbacCAcCAccaAbBCAAaBCCBACcacBcCCaBAB"

sword_notes = [roles for roles in notes if roles in 'Aa']

total_pair = 0
mentor_count = 0

for roles in sword_notes:
    if roles == 'A':
        mentor_count += 1
    elif roles == 'a':
        total_pair += mentor_count

print("Total", total_pair)

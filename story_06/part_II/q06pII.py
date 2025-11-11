############################################
#  ___                  _       ___   __   #
# / _ \ _   _  ___  ___| |_    / _ \ / /_  #
#| | | | | | |/ _ \/ __| __|  | | | | '_ \ #
#| |_| | |_| |  __/\__ \ |_   | |_| | (_) |#
# \__\_\\__,_|\___||___/\__|___\___/ \___/ #
#                         |_____|          #
############################################
# -----------------------PART II------------------------------------------------------------
'''
quest still sama mcm bawah ni:
Aa = sword fight Bb = archery Cc = magic
uppercase A B C = mentors
lowercase a b c = novices
cuma......kena care 3 category skali, utk each novice, kira berapa ramai mentor dlm sama role

'''
# ex_notes = "ABabACacBCbca"
notes = "ABCbCbCbcbaBcBaBbccbcCBACcAAcBAbbCaACBbABaBcCAcCBbCCBbAABcCAAacAAbbaBCAAAAbACaBCAAcBCaccCbAcaACbCcbCcCCAccCbAcCbCACcCBaAbaabAabBABCAACBbACbACABABcCCBbbCaaCBcAAcbcBcbbcacAaaCcAbABaBBAaCbbbaCcBacCaBbAcbCAaCAABAabaABBAcAAccCcaCbbaBBAbcCABaABaabCbCCbAAbCCbcaBCBBaAbbbBCacBbbBCaCBabBcAcBcCBcBaCBBcBAcbBcac"

category = ['A', 'B', 'C']
total_pair = 0

for cat in category:
    mentor_count = 0
    for roles in notes:
        if roles == cat:
            mentor_count += 1
        elif roles == cat.lower():
            total_pair += mentor_count

print("Total", total_pair)

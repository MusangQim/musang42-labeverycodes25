#######################################
#  ___                  _     _  __   #
# / _ \ _   _  ___  ___| |_  / |/ /_  #
#| | | | | | |/ _ \/ __| __| | | '_ \ #
#| |_| | |_| |  __/\__ \ |_  | | (_) |#
# \__\_\\__,_|\___||___/\__| |_|\___/ #
#                                     #
#######################################
# -------------------------------PART I----------------------------------

raw_notes = "1,2,3,5,9"
quest_notes = "1,4,7,9,12,15,16,19,22,25,28,29,30,33,36,38,40,42,45,48,49"

notes = []
ans_notes = []
for x in raw_notes.split(","):
    notes.append(int(x))

for y in quest_notes.split(","):
    ans_notes.append(int(y))

answer = 0
answer_quest = 0

for step in notes:
    answer = answer + (90 // step)

for steps in ans_notes:
    answer_quest = answer_quest + (90 // steps)

print("The answer is:", answer)
print("The answer for quest PI:", answer_quest)

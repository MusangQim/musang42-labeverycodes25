#######################################
#  ___                  _     _  __   #
# / _ \ _   _  ___  ___| |_  / |/ /_  #
#| | | | | | |/ _ \/ __| __| | | '_ \ #
#| |_| | |_| |  __/\__ \ |_  | | (_) |#
# \__\_\\__,_|\___||___/\__| |_|\___/ #
#                                     #
#######################################
# -------------------------------PART II----------------------------------

raw_notes = "1,2,2,2,2,3,1,2,3,3,1,3,1,2,3,2,1,4,1,3,2,2,1,3,2,2"
quest_notes = "1,2,1,3,1,2,1,4,1,2,2,3,1,2,1,5,1,2,1,3,2,3,1,5,1,2,2,3,1,2,2,5,2,2,1,4,1,2,1,4,1,3,1,4,1,2,1,6,1,2,1,3,1,3,2,4,1,2,1,3,1,3,2,5,1,3,1,3,1,2,1,6,1,2,1,3,2,2,1,5,2,2,1,4,1,2,1,5,1,2,1,3,2,2,1,6,1,2,2,3,1,2,1,4,2,2,1,5,1,3,1,5,1,2,1,3,1,2,1,5,2,2,1,4,1,3,1,5,1,2,1,4,1,2,2,4,1,2,1,3,1,2,2,7,1,2,2,3,1,2,1,4,1,3,2,3,1,2,1,5,1,3,1,3,2,2,1,6,1,2,1,3,1,2,1,6,1,2,1,4,1,2,1,4,1,3,2,3,3,2,1,6,1,2,1,3,1,3,1,4,1,2,1,3,1,2,1,5,2,3,1,3,1,2,1,7,2,2,1,4,1,2,1,5,1,2,1,3,1,2,3,4,1,2,1,3,1,2,1,6,1,3,2,3,1,2,1,5,1,2,1,5,2,2,1,5"

raw_nums = []
for part in raw_notes.split(","):
    raw_nums.append(int(part))

raw_ans = []
raw_result = 1

for i in range(len(raw_nums)):
    x = raw_nums[i]

    for j in range(i):
        if (i + 1) % (j + 1) == 0:
            x = x - raw_ans[j]

    if x > 0:
        raw_result = raw_result * (i + 1)

    raw_ans.append(x)

print("The answer is:",raw_result)



quest_nums = []
for parts in quest_notes.split(","):
    quest_nums.append(int(parts))

quest_ans = []
quest_result = 1

for a in range(len(quest_nums)):
    y = quest_nums[a]

    for b in range(a):
        if (a + 1) % (b + 1) == 0:
            y = y - quest_ans[b]

    if y > 0:
        quest_result = quest_result * (a + 1)

    quest_ans.append(y)

print("The answer for PII:",quest_result)

# ------------------PART I punya------------------
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

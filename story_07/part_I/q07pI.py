###########################################
#  ___                  _       ___ _____ #
# / _ \ _   _  ___  ___| |_    / _ \___  |#
#| | | | | | |/ _ \/ __| __|  | | | | / / #
#| |_| | |_| |  __/\__ \ |_   | |_| |/ /  #
# \__\_\\__,_|\___||___/\__|___\___//_/   #
#                         |_____|         #
###########################################

# -------------PART I------------------------------------------------------
'''
'''

def parse_rules(rules_lines):
    rules = {}
    for line in rules_lines:
        line = line.strip()
        if not line:
            continue
        if '>' not in line:
            continue
        left, right = line.split('>', 1)
        left = left.strip()
        allowed = [c.strip() for c in right.split(',')if c.strip()]
        rules[left] = set(allowed)
    return rules

def name_valid(name, rules):
    for i in range(len(name) - 1):
        a = name[i]
        b = name[i + 1]
        allowed = rules.get(a)
        if allowed is None or b not in allowed:
            print(f"X {name} failed at pair {a+b}: '{a}' can only go to {allowed}")
            return False
    print (f"{name} follow all the rules")
    return True

# names = ["Oronris", "Urakris", "Oroneth", "Uraketh"]

names = ["Felndar", "Ulsyx", "Uldar", "Felnthyris", "Felnsyx", "Urakthyris", "Ulthyris", "Urakdar", "Uraksyx"]

rules_lines = [
        "s > y",
        "U > l,r",
        "d > a",
        "l > t,n,b",
        "t > h",
        "h > y",
        "k > s,d,t",
        "a > r,k",
        "e > b",
        "F > e",
        "y > r,x",
        "r > i,b",
        "n > s,d,t",
        "i > s",
]
'''
rules_lines = [
        "r > a,i,o",
        "i > p,w",
        "n > e,r",
        "o > n,m",
        "k > f,r",
        "a > k",
        "U > r",
        "e > t",
        "O > r",
        "t > h",
]
'''
rules = parse_rules(rules_lines)

for name in names:
    name_valid(name, rules)

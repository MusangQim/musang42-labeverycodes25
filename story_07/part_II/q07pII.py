###########################################
#  ___                  _       ___ _____ #
# / _ \ _   _  ___  ___| |_    / _ \___  |#
#| | | | | | |/ _ \/ __| __|  | | | | / / #
#| |_| | |_| |  __/\__ \ |_   | |_| |/ /  #
# \__\_\\__,_|\___||___/\__|___\___//_/   #
#                         |_____|         #
###########################################

# -------------PART II------------------------------------------------------
'''
btw it just use same function jela, cuma ade tambah sikit utk calculation
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

# names = ["Felndar", "Ulsyx", "Uldar", "Felnthyris", "Felnsyx", "Urakthyris", "Ulthyris", "Urakdar", "Uraksyx"]

names = "Belmirix,Qalzorin,Kronmirix,Kronrilor,Axalmirix,Kroncyth,Pylartor,Garcyth,Naldtor,Pylariral,Axalorath,Axalther,Belphor,Pylarmirix,Azmaraxis,Garther,Qaltor,Quarnzorin,Pylarorath,Xendorath,Quarntor,Axalphor,Azmarzorin,Belcyth,Qalorath,Axaliral,Belaxis,Kronaxis,Beliral,Belzorin,Naldther,Xendtor,Naldcyth,Pylarcyth,Garmirix,Axalcyth,Quarnphor,Beltor,Azmarphor,Garrilor,Azmarther,Naldzorin,Krontor,Garaxis,Qalrilor,Xendmirix,Qalther,Belorath,Kronzorin,Kronphor,Xendiral,Pylarther,Gartor,Xendaxis,Pylarphor,Qalmirix,Xendther,Pylarzorin,Garorath,Belther,Naldaxis,Qalphor,Qalcyth,Kronther,Pylaraxis,Belrilor,Azmarrilor,Quarniral,Pylarrilor,Azmariral,Azmarorath,Quarnther,Gariral,Azmartor,Qalaxis,Naldmirix,Quarnrilor,Qaliral,Naldorath,Xendcyth,Xendrilor,Axaltor,Axalrilor,Naldphor,Quarnorath,Axalzorin,Xendphor,Axalaxis,Quarnaxis,Azmarmirix,Garzorin,Kronorath,Quarncyth,Xendzorin,Naldiral,Quarnmirix,Naldrilor,Garphor,Kroniral,Azmarcyth".split(',')

rules_lines = [
        "h > e,o",
        "G > a",
        "m > i,a",
        "P > y",
        "c > y",
        "z > o,v",
        "t > o,h",
        "K > r",
        "x > i,v",
        "d > i,t,p,o,z,m,a,c,r",
        "Q > a,u",
        "y > l,t,v",
        "r > t,a,i,v,p,o,z,m,c,r,n",
        "i > r,n,x,s,l",
        "a > r,l,t,x,v",
        "e > v,r",
        "l > a,o,i,t,p,z,m,c,r,d",
        "n > d,i,t,p,o,z,m,a,c,r",
        "u > v",
        "o > r,n",
        "B > e",
        "p > h",
        "A > x,z",
        "N > a",
        "X > e",
]

'''
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

total_index = 0
for i, name in enumerate(names, start=1):
    if name_valid(name, rules):
        total_index += i

print("Total index:", total_index)

'''
for name in names:
    name_valid(name, rules)
'''

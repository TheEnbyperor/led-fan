import sys
f = open(sys.argv[1])

for l in f.readlines():
    l = l.strip()
    num = int(l, 16)
    print(f"{l}\t{num:b}")

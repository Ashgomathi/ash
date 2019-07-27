from itertools import combinations
numb ,v1 = input().split()
v1 = int(v1)
v2 = []
hj = combinations(numb,len(numb)-v1)
for d in hj:
    v2.append("".join(d))
print(min(v2))

set=int(input())
pl=list(map(int,input().split()[:set]))
pl.sort()
for l in pl:
        print(l,end=" ")

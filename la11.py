ashram=int(input())
get=list(map(int,input().split()[:ashram]))
get.sort()
for i in get:
  print(i,end=" ")

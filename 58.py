d1,g1=map(int,input().split())
vnt=list(map(int,input().split()[:d1]))
count=0
for i in vnt:
   if(i==g1):
      print("yes")
      break
else:
   print("no")

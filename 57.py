vns1,vns2=map(int,input().split())
dm=list(map(int,input().split()[:vns1]))
count=0
for i in dm:
   if(i==vns2):
      count=count+1
print(count)      

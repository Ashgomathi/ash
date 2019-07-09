weig=int(input())
if(weig>1):
 for i in range(2,weig):
  if(weig%i==0):
   print("yes")
   break
 else:
   print("no")

ashuu=int(input())
if(ashuu>1):
   for l in range(2,ashuu):
      if(ashuu%l)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")

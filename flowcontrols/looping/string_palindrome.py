name="luminar"
#ranimul
#print(len(name))
#for i in range(6,0,-1):
#print(name[i]) #name[7]
length=len(name)-1#6

reverse=""
while(length>=0):

    reverse+=reverse+name[length]  #reverse="+name[6]=ranimul
   # print(name[length],end="")     #you can use this step instead of above reverse step
length-=1
print(reverse)  #if u use reverse step,then u can use should use this step too

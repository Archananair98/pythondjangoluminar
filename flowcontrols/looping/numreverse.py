num=int(input("enter num")) #123
res=""
while(num>0): #123<0  12<0
  digit=num%10 #123%10=3 12%10=2 1%10=1
  #res=res*10+digit                #multiply with 10 +digit
  res=res+str(digit)
  #print(digit,end="") #3 2 1
  num=num//10 #12 12//10
  print("res=",res)

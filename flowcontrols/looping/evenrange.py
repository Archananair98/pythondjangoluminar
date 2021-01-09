limit=int(input("enter limit")) #8(1,8)
#print all even numbers upto this limit

i=1
while(i<=limit): #1<=5 2<=5 3<=5 4<=5 5<=5 6<=5
  if(i%2==0):      #1%2==0 2%2==0 3%2==0 4%2==0 5%2==0
                  # print(i) #1 2 3 4 5 6 7 8 we have to check each one is even
   print(i) #2 4
i+=1 #i=2 3 4 5 6
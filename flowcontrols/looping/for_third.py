#check given number is prime or not
#num=(1,num)


num=int(input("enter number"))#13  (2,...12)
flg=0
for i in range(2,num):

    if(num%i==0):
      flg=flg+1
      break
         #not prime block
    else:
      flg=0
        #prime

if flg==0:
     print("prime")
else:
     print("not prime")



#q1
#low 5 upp=50 print all prime numbers b/w 5 to 50




#q2
#read a number=2
#read low=4
#read upp=30
#1**2=1(low,upp)

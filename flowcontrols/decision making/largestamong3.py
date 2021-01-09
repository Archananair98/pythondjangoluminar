num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
#find the highest number among 3:

#if((num1>num2)&(num1>num3)):
    #print("num1 is highest")
#elif((num2>num1)&(num2>num3)):
#    print("num2 is highest")
#elif((num3>num1)&(num3>num2)):
 #   print("num3 is highest")
#elif((num1==num2)&(num1==num3)):
 #   print("3 num are equal")





#find 2nd largest:
if ((num1<num2)&(num1>num3)|(num3>num1)&(num1>num2)):
   print("num1 is nd largest  ")
elif((num2<num1)&(num2>num3)|(num3>num2)&(num2>num1)):
    print("num2 is nd largest")
elif((num3<num1)&(num3>num2)|(num3<num2)&(num3>num1)):
   print("num3 is nd largest")
#elif((num2>num1)&(num2>num3)|(num1<num2)&(num1>num3)):
 #   print("num2 is largest and num1 is 2nd largest")
#if((num3>num1)&(num3>num2)|(num2>num1)&(num2<num3)):
 #   print("num3 is largest and num2 is 2nd largest")
#elif((num3>num1)&(num3>num2)|(num1<num3)&(num1>num2)):
 #   print("num3 is largest and num1 is 2nd largest")
#elif((num1==num2==num3)):
 #   print("3 numbers are equal")



#f((num1>num2>num3)|(num3>num2<num1))
 #  print("num1,num2, num3")
  # elif(n): #
#rint("num1,num2,num3)

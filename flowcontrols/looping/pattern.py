num=input("enter num") #2
i=1
data=0
pattern="+"
while(i<=int(num)): #1<=2 2<=2 3<=2
    res=num*i#"2"*1=2 "2"*2=22
    #print(res)
    pattern=pattern+"+"+res

    data+=int(res) #0+2=2 2+22=24
    i+=1 #i=2 i=3
    pattern=pattern.lstrip("+")
    print(pattern)
print("=",data)#24
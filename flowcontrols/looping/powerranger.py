#2
#low=4
#upper=30

num=int(input("enter number"))

low=int(input("enter lowerlimit"))
upper=int(input("enter upperlimit"))

for i in range(1,(upper+1)):
    if i**num in range(low,upper):
        print(i)


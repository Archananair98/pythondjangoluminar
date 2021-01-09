#*
#**
#***
#****

 #for row in range(1,5):
  # for col in range(row): #1 in range (0,1) (0,2)

   #     print("*",end="")
    #print()


#for print a table of numbers

#for row in range(1,5):#row=1
  #  for col in range(1,row+1):#col=0

     #   print(col,end="")
   # print()


#triangle pattern
for row in range (1,5):#row=1
    for col in range(1,8):#col=1,2,3,4
        if (row==4)|(row+col==5)|(col-row==3):
            print("*",end="")
        else:
            print(end="")
    print()


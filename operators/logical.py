#(&,|,^)
#rule of &,if one is false,entire is false
  #  rule of | one is true,entire is true
#rule of ^ if both end same bit, it will return false
#if both end different ,it will return true
print(2&4) #010&100=(000)
           #(0&1=0)(1&1=1)(1&0=0)

print(2|4) #(0|1=1)(1|0=1)(1|1=1)
           #010|100=(110)

print(2^4) #(0^0=0)(1^1=0)(1^0=1)
          # if same ,it is 0 and if it is different ,ie,1
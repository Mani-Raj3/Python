"""For Loop......."""

# # a = range (1, 20 , 1)  -->> isme pehle nmbr Default hota h Or dsura nmbr Jaha tk Stop krna h wo  
#                         hota hai or Last wala nmbr v default hi hota h -- Hum agr dono starting or 
#                        Ending default de ya nhi de Complier Automatic Default bna dega Or jo stop
#                     value hoga mtlb jaha tk print krna hoga waha tk chlga 0 se se uss nmber tk
# Syntax of range function is simple range(start, stop, steps)

""" Loops for numbers"""

# for i in range(21):
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)    

"""Let's print the table of 5"""

# for i in range(5, 51, 5):
#     print(i)

# n = int(input("which table you want ? "))

# for i in range( n, n*10, n):
#     print(i)

"""Loops in Strings"""

# a = "SHERYIANS TEACHES INDUSRTY THINGS"
# print(len(a))

# for i in range (len(a)):
#     print(a[i])

# a = "mani is good boy"

# for i in a:
#     print(i)

# for i in range(1, 21):
#     if i == 15:
#         continue      isme 15 ko skip kr ke aage badh jyga 1 se 20 tk 
#     print(i)

# for i in range(1, 21):
#     if i == 15:
#         break         isme 1 se 14 tk hi chlega
#     print(i)

"""break and else"""

for i in range(1, 21):
    if i == 56:
          print("break statement is executed")
          break
    print(i)

else:
     print("Break statement is not executed")    

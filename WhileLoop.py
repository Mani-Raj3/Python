# a = 1

# while (a <= 30):
#     print(a)
#     a = a + 1

"""1. Separate each digit of a number and print it on the new line"""

# a = int(input("tell your number"))

# while( a > 0):
#     print( a% 10)
#     a = a // 10

""""2. Accept a number and print its reverse"""

# a = int(input("tell your number"))

# rev = 0
# while( a > 0):
#      rev = rev * 10 + a % 10
#      a = a // 10

#      print(rev)


""" 3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)"""

a = int(input("Tell your number"))

copy = a
rev = 0

while (a>0):
    rev = rev * 10 + a % 10
    a = a //10

    if copy == rev:
        print("Pallindromic number")
    else:
        print("not a pallindromic number")    
# test case
number1 = 123
number2 = -123
number3 = 12.3
number4 = -12.3
number5 = "abc"
number6 = '7f'
x = True

# 1. boolean class
result = bool(x)
print(result)

# 2.integer class int()
print(int(number1))
print(int(number2))
print(int(number3))
print(int(number4))
# print(int(number5)) # it does not work string to integer
print(int(number6, 2))  # (number, base)


# Floating class float()
print(float(number1))
print(float(number2))
print(float(number3))
print(float(number4))
# print(float(number5)) # it does not work string to floating value
print(float(number6, 16))  # number system does not work

# String class float()
print(str(number1))
print(str(number2))
print(str(number3))
print(str(number4))
print(str(number5))
# print(str(number6, 16))# number system does not work

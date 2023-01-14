import math

def factorial(num):
    if num == 0 or num == 1 :
        return num
    else :
        return num * factorial(num - 1)
    
def main():
    num = int(input("number1 :"))
    result = math.factorial(num) 
    # result = factorial(num)
    print("Number1: {0} => Result: {1}".format(num, result))

if __name__=="__main__":
    main()
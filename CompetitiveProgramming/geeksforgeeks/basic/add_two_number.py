add = lambda num1, num2 : num1 + num2

def main():
    num1 = float(input("number1 :"))
    num2 = float(input("number2 :"))
    result = float(add(num1, num2))
    print("Sum of {0} and {1} is {2}".format(num1, num2, result))
    
if __name__=="__main__":
    main()

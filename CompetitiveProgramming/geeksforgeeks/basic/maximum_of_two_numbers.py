def max_number(num1, num2):
    if num1 >= num2 :
        return num1
    else :
        return num2
    
def main():
    num1 = float(input("number1 :"))
    num2 = float(input("number2 :"))
    result = max(num1, num2)
    print("Number1: {0} and NUmber2: {1} => Result: {2}".format(num1, num2, result))

if __name__=="__main__":
    main()
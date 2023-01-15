import math


def main():
    R = int(input("R: "))
    result = math.pi * pow(R, 2)
    print("Area of %.6f" %result)

if __name__=="__main__":
    main()
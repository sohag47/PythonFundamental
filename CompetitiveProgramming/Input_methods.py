# n = int(input())

# arr = [int(x) for x in input().split()]
# # arr = list(map(int, input().split()))

# sum = 0
# for x in arr:
#     sum += x

# print(n, arr, x)

#! for faster 
from sys import stdin, stdout

def get_int(): 
    return [int(x) for x in stdin.readline().split()]

def main():
    arr = get_int()
    stdout.write(str(arr))

    sum = 0
    for x in arr:
        sum += x

    stdout.write(str(sum))

if __name__=="__main__":
    main()
def isPrime(n):
    if n==2 or n==3: 
        return True
    if n%2==0 or n<2: 
        return False
    flag = True
    
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            flag =  False    

    return flag


def findMaxNumber(a: int, b: int):
    if a < b: 
        return b
    else: 
        return a


def recursive_sum(pyramid, i, j, row):
    if i==row:
        return 0
    else:
        # to check which one is bigger and add
        
        # 1      j=0
        #8 4    for 8 j is 0, for 4 j is 1(j+1)
        return pyramid[i][j] + findMaxNumber(recursive_sum(pyramid, i+1, j, row), recursive_sum(pyramid, i+1, j+1, row)) 


def main():
    
    with open('input.txt', 'r') as file:
        # read line by line
        pyramidList = [[int(x) for x in line.split()] for line in file]

    #pyramid row number
    row = len(pyramidList) 
    maxSum = 0

    # remove prime numbers 
    for i in range(0, row):
        for j in range(0, i+1):
            if pyramidList[i][j] != None and isPrime(pyramidList[i][j]): pyramidList[i][j] = float('-inf')

    # to check the starting number is prime or not
    if pyramidList[0][0] == float('-inf'): return print("There is no path")
    # call recursive sum func
    maxSum = recursive_sum(pyramidList, 0, 0, row)
    print(maxSum)


if __name__ == "__main__":
    main()
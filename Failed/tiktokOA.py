# given an array of numbers find the largest possible value you can get by
# multiplying 5 of them together
def magicNumber(arr):
    arr.sort() # ascending

    n = len(arr)

    if n < 5:
        return None
    
    # filter out all zeros
    arr = [item for item in arr if item != 0]

    if len(arr) < 5:
        return 0
    
    else:
        # 3 different possibilities, 5 pos, 3 pos + 2 neg, 4 neg + 1 pos
        allPos = 1
        for i in range(1,6):
            allPos *= arr[-i]
        
        halfHalf = allPos / arr[-4] / arr[-5]
        halfHalf *= arr[0]* arr[1]

        mostNeg = arr[-1]
        for i in range(4):
            mostNeg *= arr[i]
    
   
    return max(allPos, halfHalf, mostNeg)

def main():
    tests = {
    'ordered': [1, 2, 3, 4, 5, 6, 7], #2520
    'neg': [-1, -2, -3, -4, -5, -6, -7], # -120
    'random1' : [1, -10, -10, 5, 6, -20, 7, 0, 0], #42000
    'random2' : [0, -10, -20, 5, 6, 7, 8], #67200
    'posWithZero' : [0, 1, 2, 3, 4, 5, 0, 6, 7], #2520
    'zero' : [0, 0, 0, 0, 0, 0, 0], # 0
    'short' : [1, 2, 3], # None
    'fiveNum' : [3, 4, -5, 6, 7], # -2520
    'large' : [-1000, -999, 1, 2, 3, 1000, 999], #2997000000
    'identical' : [3, 3, 3, 3, 3, 3, 3], #243
    'mixed' : [-1, -2, -3, -4, 100] #2400
    }

    for t in tests:
        print(magicNumber(tests[t]))

if __name__ == "__main__":
    main()

    
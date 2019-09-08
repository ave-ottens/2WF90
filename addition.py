listX = [3, 2, 15]
listY = [15, 3]
radix = 16
listXY = listX, listY

maxLen = max(map(len, listXY))
minLen = min(map(len, listXY))

for digits in listXY:
    while len(digits) < maxLen:
        digits.insert(0, 0)

def addition():
    sumXY = [sum(x) for x in zip(*listXY)]
    
    for i in range(maxLen):
        carryXY = [item // radix for item in sumXY]
        carryXY.append(0)
    print(carryXY)

    sumcarryXY = sumXY, carryXY
    print(sumcarryXY)
    
    maxLenSum = max(map(len, sumcarryXY))

    for words in sumcarryXY:
        while len(words) < maxLenSum:
            digits.insert(0, 0)

    addcarryXY = [sum(x) for x in zip(*sumcarryXY)]

        # modXY = [item % radix for item in sumXY]
        


    print(maxLenSum, sumcarryXY, addcarryXY)
addition()
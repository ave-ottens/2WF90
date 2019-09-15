# listX = [13, 15, 9, 14, 7, 6, 13, 1, 1, 3, 8, 9, 5, 8, 2, 1, 12, 5, 6, 7]
# listY = [6, 10, 2, 0, 11, 1, 8, 8, 6, 7, 5, 10, 11, 3, 9, 14, 1, 7, 10, 2]
listX = [1, 3, 4]
listY = [2, 3]
positiveX = False
positiveY = True
radix = 10
listXY = listX, listY

maxLen = max(map(len, listXY))
minLen = min(map(len, listXY))

def addition(inputX, positiveX, inputY, positiveY, b):
    if (positiveX == False) and (positiveY == False):
        positiveX = True
        positiveY = True
        output = subtraction(inputX, positiveY, inputY, positiveX, b)
        return 'negative', output

    # if X is a negative number, then subtract Y from X
    elif (positiveX == False) and (positiveY == True):
        positiveX = True
        output = subtraction(inputX, positiveY, inputY, positiveX, b)
        return 'negative', output
    # if Y is a negative number, then subtract X from Y 
    elif (positiveY == False) and (positiveX == True):
        positiveY = True
        output = subtraction(inputX, positiveX, inputY, positiveY, b) 
        return output

    # if both X and Y are positive, then add both digits
    if (positiveX == True) and (positiveY == True):
        # add digits 
        for digits in listXY:
            while len(digits) < maxLen:
                digits.insert(0, 0)
        
        # sum the digits from listX with listY according to index in each list
        sumXY = [sum(x) for x in zip(*listXY)]
        
        # calculate if there is a carry for each element and then add a zero to the end, to make sure the carry goes to the digit on the right side of the element
        for i in range(maxLen):
            carryXY = [item // radix for item in sumXY]
            carryXY.append(0)
            
        sumcarryXY = sumXY, carryXY
        maxLenSum = max(map(len, sumcarryXY))

        # make sure that the length of both sumXY and carryXY is the same 
        for digits in sumcarryXY:
            while len(digits) < maxLenSum:
                digits.insert(0, 0)

        # add the carry stored in carryXY to sumXY
        addcarryXY = [sum(x) for x in zip(*sumcarryXY)]
        # now only keep the mod of the digit, since the carry is already added to the digit on the right
        output = [item % radix for item in addcarryXY]
            
        return output

# def subtraction(x, positiveX, y, positiveY, b)
#     if (positiveY == False):
#         positiveY = True
#         addition(x, positiveX, y, positiveY, b) 
    

def subtraction(inputX, positiveX, inputY, positiveY, b):
    result = []
    lenX = len(inputX)
    lenY = len(inputY)
    reverseX = inputX[::-1]
    reverseY = inputY[::-1] #reverse the list

    if (positiveX == False) and (positiveY == False):
        positiveX = True
        output = addition(inputX, positiveX, inputY, positiveY, b)
        return 'negative', output
    elif (positiveX == True) and (positiveY == False):
        positiveY = True
        output = addition(inputX, positiveX, inputY, positiveY, b) 
        return output 
    elif (positiveX == False) and (positiveY == True):
        positiveX = True 
        output = addition(inputX, positiveX, inputY, positiveY, b)
        return 'negative', output
    else:
        for i in range(minLen,maxLen):
            if lenX < lenY: reverseX.append(0)
            if lenX > lenY: reverseY.append(0) #fill up with zeros to balance length
        
        inputX = reverseX[::-1]
        inputY = reverseY[::-1]

        for i in range(0,maxLen):
            digit = inputX[i] - inputY[i]
            result.append(digit)

            if b != 0:
                result[i] %= b
                
            if inputX[i] < inputY[i]:
                result[i-1] = result[i-1] - 1

        p = result

        # remove preceding zeroes
        while p[0] == 0 and not len(p) == 1:
            p = p[1:]

        return p


def multiplication(inputX, positiveX, inputY, positiveY, b):
    for digits in listXY:
        while len(digits) < maxLen:
            digits.insert(0, 0)

    n = len(inputX)
    output = [0]*2*n

    for i in range(0, n):
        digit2 = inputY[-(i+1)]
        for j in range(0, n):
            digit1 = inputX[-(j+1)]
            outputNumber = digit1 * digit2
            output[-(1+i+j)] += outputNumber
    print(output)

    for i in range(1, len(output)+1):
        if output[-i] >= b:
            carry = output[-i] // b
            output[-i] = output[-i] % b
            output[-(i+1)] += carry

    print(output, 2*n)

multiplication(listX, positiveX, listY, positiveY, radix)
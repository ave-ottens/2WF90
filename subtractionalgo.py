def subtraction(inputX, inputY, b):
    result = []
    lenX = len(inputX)
    lenY = len(inputY)
    maxLen = max(lenX, lenY)
    minLen = min(lenX, lenY)
    reverseX = inputX[::-1]
    reverseY = inputY[::-1] #reverse the list
    
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

    return {
        "answer": p
    }

# print(subtract_poly([11,1,4,15,12,6,7,5],[8,3,9,14,10,2,4,7], 16))
subtraction([4, 3, 1], [2, 4, 0], 5)
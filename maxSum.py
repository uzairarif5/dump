selectedIn = []
selectedOut = []

def S(A):
    bestSum = A[0]
    for i in range(len(A)):
        sum = A[i]
        tempA = [A[i]]
        bestInnerSum = A[i]
        for j in range(i+1,len(A)):
            sum += A[j]
            tempA.append(A[j])
            if(sum > bestInnerSum):
                bestInnerSum = sum
                selectedIn = tempA
        if(bestInnerSum > bestSum):
            bestSum = bestInnerSum
            selectedOut = selectedIn
        
    return (selectedOut,bestSum)

print(S([4,-5,3,-2,9,1,3]))

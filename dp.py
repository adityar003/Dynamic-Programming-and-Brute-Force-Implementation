import audioop
import sys
import fileinput
import datetime
import time
from collections import OrderedDict

start = time.time()


def longestrepeatedsubseq_dp(A):
    n = len(A)
    lrs = 0
    lrs = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 0 or j == 0:
                return 0;
            elif (A[i - 1] == A[j - 1] and i != j):
                lrs[i][j] = 1 + lrs[i - 1][j - 1]
            else:
                lrs[i][j] = max(lrs[i][j - 1], lrs[i - 1][j])

    # string using lrs[][] Initialize result
    seq = ''
    # Traverse lrs[][] from bottom right
    for x in lrs:
        print(x)
    i = n
    j = n
    isResultFound = False
    #while (i > 0 and j > 0):
    while (i >=0  and j <= n):
        if (lrs[i][j] == lrs[i - 1][j - 1] + 1):
            seq = seq + A[i - 1]
            i = i - 1
            j = j - 1
            isResultFound = True
        # Otherwise we move to the side
        # that gave us maximum result.
        elif (lrs[i][j] == lrs[i - 1][j]):
            i = i - 1
        elif(lrs[i][j] == lrs[i][j - 1]):
            j = j - 1

    # Since we traverse lrs[][] from bottom,
    # we get result in reverse order.
    if (not isResultFound):
        print("Result not found")
    seq = seq[::-1]
    ordered = "".join(OrderedDict.fromkeys(seq))
    return ordered
    return seq;


A = input("Enter the input:")
output = longestrepeatedsubseq_dp(A)
if (len(A) > 2):
    print(output)
    print("Length of the LRS:",len(output))
elif (len(A) == 2):
    print("Incorrect input")
    print(A)
else:
    print("Invalid input")

end = time.time()
final = end - start
print("Total time taken is:", final)

# str = 'ATACTCGGA'
# print(longestrepeatedsubseq_dp(A))

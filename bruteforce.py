import time
import sys
start = time.time()
from collections import Counter

def isSame(string1, left, right): #check if the index of Left and right element are different
    while right > left:
        if string1[left + 1] != string1[right - 1]:
            return False
    return True

def lrs(string1):
    list1=[]  #initialize an empty list

    length1 = len(string1)
    var = Counter(string1) #assign a counter to the string

    print(var)
    for i in range(0, length1):
        var[string1[i]]

        if var[string1[i]] >= 2: # if the occurence of the character is greater than equal to 2, append the list
            for key in var.keys():
                print(key)
                list1.append(key)
            print(list1)
            str1 = ''.join(x for x in list1) # to store string in a list
            print(str1)
            return
    k = 0
    for i in range(0, length1): #if the character occours once, mit will be null
        if var[string1[i]] > 1:
            string1[k + 1] = string1[i]
            string1[k] = '\0'
            print(string1[k])

    if isSame(string1, 0, k - 1):  #no of occourences
        if k and 1:
            return string1[k / 2] == string1[k / 2 - 1]
        return False
    return True
A = sys.argv[1]
print("Length:",lrs(A))
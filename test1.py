import unittest
import hashlib

def isOddNumber(n):

    if n%2 == 0:
        return False
    return True

def printOddNumbers(s,e):

    e = e + 1 # add 1 to print it
    for l in range(s,e):
        if isOddNumber(l):
            print l


def get_nonce():
    """ Functions gets the nonce values using zeros, more zero values
    harder it becomes"""
    i = 0
    j =0

    # Start the loop
    print "running"
    while True:

        string1 = "hello" + str(j)
        h = hashlib.sha256(string1).hexdigest()
        print string1
        print h
        j = j + 1
        zeros = "000000"
        if h.startswith(zeros):
            print j
            break
        continue
    return 0

def bubble_sort(array):
    "Sorts array with bubble sort algorithm"

    j = len(array)

    # if only one, no point in iterating
    if j == 1:
        return array

    # create two loops, while loop for looping through
    # arrays everytime and decrementing everytime
    # for loop to go through the smaller array
    while j > 0:

        for i in range(0,j):
            # if reaching in the end i+1 will cause error
            if i == j-1:
                break
            #print array
            # if greater Swap
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i + 1] = array[i]
                array[i] = temp

        # Decrement j
        j = j - 1
    return array


print bubble_sort([10,6,6,8,9,10,11,12,13,14,20,19,18,17])

print bubble_sort([7,6,6,6,7])


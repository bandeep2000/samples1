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

    j = len(array)
    print j

    while j > 0:

        for i in range(0,j):
            if i == j-1:
                break
            print array
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i + 1] = array[i]
                array[i] = temp



        print j
        j = j - 1
    print array
    return 0

bubble_sort([10,5,2,1,3])


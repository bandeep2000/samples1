
def isEven(number):
    if number % 2 == 0:
        return True
    return False

def divideStringReverse(string1):

    len1 = len(string1)

    if isEven(int(len1)):
        mIndex = len1/2
        begin_string = string1[:mIndex]
        revere_end_string = string1[mIndex:][::-1]
    else:
        # If Odd, Subtract 1
        lengthMinusOne = len1 - 1

        mIndex = lengthMinusOne / 2
        # mChar = string1[mIndex]

        begin_string = string1[:(mIndex)]
        revere_end_string = string1[(mIndex + 1):][::-1]

    return begin_string,revere_end_string


def isAnagram(string1):

    begin_string,end_reverse_string = divideStringReverse(string1)

    if begin_string == end_reverse_string:
        return True
    return False


print isAnagram("hegdo1")
print isAnagram("hegdb")

print isAnagram("md")

def test1():
   assert isAnagram("md") == False
   #assert isAnagram("md") == True




"""
    First Part: Fix it.


    The next class is filled with failing or bad implemented methods.
    Fix them according to what the documentation expects them to do.

    Some errors can also be when calling the methods.
"""

class failingClass():

    def __init__(self):
        self.aList = [1, 2, 3, 4, 5]
        self.aDict = {'doNotDeleteMe': 1337,}

    def addNewList(self):
        """
        addNewList - this method adds 4 new elements to the instance list
                     aList
        """
        self.aList.extend([6, 7, 8, 9]) #fix: use extend method to join both lists
    
    def checkKey(self, key):
        """
        checkKey - this method verifies if a key exists within the instance
                   dictionary aDict.
        @key: key to be verified.

        Return: True if key exists, False otherwise
        """
        if key in self.aDict : #fix: check if key is in aDict keys
            return True
        
        return False

    def sumOfThree(self, a, b, c):
        """
        sumOfThree - this method returns the sum of a, b and c
        @a: first integer in the sum
        @b: second integer in the sum
        @c: thrid integer in the sum
        """
        return a + b + c
    
    def fillaDict(self, numbers):
        """
        fillaDict - adds to the instance dictionary aDict all the
                    key-values from the dictionary numbers.
        @numbers: dictionary to be use to fill the instance dictionary
        """
        self.aDict.update(numbers) #fix: merge numbers dict into aDict


if __name__ == '__main__':
    letsee = failingClass()

    print(letsee.aList)

    letsee.addNewList()

    # This should print the result of 3 + 7
    print(letsee.aList[2] + letsee.aList[6])

    res = letsee.checkKey('capital')

    print(res)

    numbers = {'a': 1, 'b': 2, 'c': 3}

    result = letsee.sumOfThree(**numbers) #fix: pass numbers dict as kwargs

    # This should print "6"   -> 1 + 2 + 3
    print(result)

    letsee.fillaDict(numbers)

    print(letsee.aDict)


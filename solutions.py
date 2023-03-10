''' Python debugging Compulsory Task
L Jordaan
9 March 2023

1. Finding the errors in the Python code and fix them'''


numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def quick_sort(numbers):
    '''Fixed indentation'''
    quick_sort_helper(numbers, 0, len(numbers)-1) #sorting out the len/range of numbers

def quick_sort_helper(numbers, first, last):
        '''Fixed indentation in this code'''
        if first < last:
            splitpoint = partition(numbers, first, last)
            quick_sort_helper(numbers, first, splitpoint-1)
            quick_sort_helper(numbers, splitpoint+1, last)
        return numbers

def partition(numbers, first, last):
    '''Indentation everything inside the def function'''
    pivotvalue = numbers[first]
    leftmark = first+1
    print('leftmark', leftmark)
    rightmark = last
    print('rightmark',rightmark)

    done = False
    while not done:  #changed the while loop conditions
        while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
            leftmark += 1 #changed the code here

        while rightmark >= leftmark and numbers[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:  #fixed the else statement
            temp = numbers[leftmark]
            numbers[leftmark] = numbers[rightmark]
            numbers[rightmark] = temp

    temp = numbers[first]
    numbers[first] = numbers[rightmark]
    numbers[rightmark] = temp

    return rightmark
    

print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))

# Name: Casey Lowe
# OSU Email: lowecas@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1 - Python Fundamental Review
# Due Date: October 25th, 2023
# Description: Initial assignment with python fundamentals being reviewed/tested. There are ten sections of this
# assignment to test these fundamentals.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    sorts through an array and returns the min and max elements in a tuple
    """
    min_val = arr[0]
    max_val = arr[0]

    # walks through the array using a for loop at the number of sequences equal to the length of the array/tuple.
    for index in range(arr.length()):

        # comparing each value to the original minimum value in position 0 and revaluing the minimum value if it is
        # less than current value.
        if arr[index] < min_val:
            min_val = arr[index]

        # comparing each value to the original maximum value in position 0 and revaluing the maximum value if it is
        # greater than current value.
        if arr[index] > max_val:
            max_val = arr[index]

    return (min_val, max_val)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

#
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Function that returns a new array with string "fizz" if the number in the original array is divisible by 3, with
    string "buzz" if the number in the original array is divisible by 5, and string "fizzbuzz" if the number in the
    original array is both a multiple of 3 and a multiple of 5.
    """
    new_arr = StaticArray(arr.length())

    # walks through the array using a for loop at the number of sequences equal to the length of the array.
    for index in range(arr.length()):
        if arr[index] % 3 == 0 and arr[index] % 5 == 0:
            new_arr[index] = "fizzbuzz"
        elif arr[index] % 3 == 0:
            new_arr[index] = "fizz"
        elif arr[index] % 5 == 0:
            new_arr[index] = "buzz"
        else:
            new_arr[index] = arr[index]
    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Function that receives a StaticArray and reverses the order of the elements in the array.
    The reversal is done in place, meaning the original input array will be modified.
    """
    # end_index = the last index of the StaticArray
    end_index = arr.length() - 1
    # swapping the beginning and end indexes of the StaticArray until the middle index
    for index in range(arr.length() // 2):
        temp = arr[end_index - index]
        arr[end_index - index] = arr[index]
        arr[index] = temp


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Uses the existing array and creates a new array, shifting their positions based on the values of steps, if steps
    are positive integer elements they are shifted to the right, negative integer elements are shifted to the left.
    """

    new_arr = StaticArray(arr.length())
    for index in range(arr.length()):
        if steps > 0:
            move = (index + steps) % arr.length()
            new_arr[move] = arr[index]
        elif steps < 0:
            move = (index + steps + arr.length()) % arr.length()
            new_arr[move] = arr[index]
        else:
            new_arr[index] = arr[index]
    return new_arr
# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Function that receives two integers, the start and end of a new StaticArray. Then it returns a StaticArray that
    contains all the sequence integers between start and end.
    """
    # setting up a counter to be used to keep track of array size
    counter = 0
    startingValue = start

    # if statement that determines the size of the array by incrementing counter for each value
    if start <= end:
        while (startingValue <= end):
            counter += 1
            startingValue += 1
    else:
        while (end <= startingValue):
            counter += 1
            startingValue -= 1

    # setting up a new StaticArray named newArray
    newArray = StaticArray(counter)

    # the array will be ascending if the starting value is less than or equal to ending value
    if (start <= end):
        for index in range(newArray.length()):
            newArray[index] = start
            start += 1
    # the array will be descending if the starting value is greater than the ending value
    else:
        for index in range(newArray.length()):
            newArray[index] = start
            start -= 1

    return newArray

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Function that returns a value of 1 if the array is in ascending order, -1 if the array is in descending order,
    and 0 if the array is neither.
    """
    ascending = 0
    descending = 0

    # initial array verification that the length is greater than 1 to continue a step through otherwise it will return
    # a value of 1 indicated ascending.
    if arr.length() == 1:
        return 1
    else:
        # comparing each element in the array
        for index in range(arr.length() - 1):
            if arr[index] < arr[index + 1]:
                ascending += 1
            elif arr[index] > arr[index + 1]:
                descending += 1
        # based on the length of the array and the counting it will give the final result of ascending, descending,
        # or other.
        if ascending == arr.length() - 1:
            return 1
        elif descending == arr.length() - 1:
            return -1
        else:
            return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Function returns a tuple of the mode of the given array and its frequency. Additionally, double checks  that if
    there is more than one element that has the highest frequency, select the one that occurs first in the array.
    """
    count = 1
    mode = arr[0]
    frequency = 1
    for index in range(1, arr.length()):
        if arr[index] == arr[index - 1]:
            count += 1
            if count > frequency:
                mode = arr[index]
                frequency = count
        else:
            count = 1
    return mode, frequency

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Function that receives a StaticArray, assumes the elements are in ascending order, and returns a new StaticArray
    with any duplicate element removed.
    """
    if arr.length() == 1:
        newArray = StaticArray(arr.length())
        newArray[0] = arr[0]
        return newArray
    else:
        copiedArray = StaticArray(arr.length())
        # setting up a secondary array for comparisons inputting
        copiedArray[0] = arr[0]
        arrSize = 1
        # step through the original array and comparing it to the copied array to verify any duplicates
        for index in range(arr.length() - 1):
            if arr[index] != arr[index + 1]:
                arrSize += 1
                copiedArray[index + 1] = arr[index + 1]

        newArray = StaticArray(arrSize)

        # duplicating the first value of the original array into the first value of newArray
        newArray[0] = arr[0]
        # steps into the next position since the initial position will be filled
        arrIndex = 1
        counter = 0
        while arrIndex != arrSize:
            tempIndex = arrIndex + counter
            # checks for a None value in the copiedArray or if the preceding element in newArray is equal to the current
            # value of the copiedArray step into the next available index
            while (copiedArray[tempIndex]) is None or newArray[arrIndex-1] == copiedArray[tempIndex]:
                tempIndex += 1
                counter += 1
            newArray[arrIndex] = copiedArray[tempIndex]
            arrIndex += 1
        return newArray

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    Function to return a new array with the same elements of the original array sorted in non-ascending order.
    """
    min_num = min_max(arr)[0]
    max_num = min_max(arr)[1]
    num_range = max_num - min_num + 1
    # setting up the new counting array
    count_arr = StaticArray(num_range)
    # setting up the new StaticArray equal in length to the original array
    new_arr = StaticArray(arr.length())

    for index in range(num_range):
        count_arr[index] = 0
    for index in range(arr.length()):
        count_arr[num_range - (arr[index] - min_num) - 1] += 1
    for index in range(1, num_range):
        count_arr[index] += count_arr[index - 1]
    for index in range(arr.length()):
        new_arr[count_arr[num_range - (arr[index] - min_num) - 1] - 1] = arr[index]
        count_arr[num_range - (arr[index] - min_num) - 1] -= 1

    return new_arr


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Function that takes an array of elements, squares the element and returns the squared values into a new array,
    along with sorting in ascending order.
    """
    result = StaticArray(arr.length())

    # Initialize two pointers start and end
    left, right = 0, arr.length() - 1

    # populate array from end to start
    for i in range(arr.length() - 1, -1, -1):
        if abs(arr[left]) >= abs(arr[right]):
            result[i] = arr[left] ** 2
            left += 1
        else:
            result[i] = arr[right] ** 2
            right -= 1

    return result

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')

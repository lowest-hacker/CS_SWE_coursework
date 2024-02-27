# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the underlying storage capacity for the elements in the dynamic array.
        It does not change the values or the order of any elements currently stored in the array.
        """

        if new_capacity <= 0 or new_capacity < self.length():
            return None

        # create a new static array
        new_arr = StaticArray(new_capacity)
        index = 0

        # if the new_capacity is smaller than the StaticArray's current length
        if new_capacity < self._data.length():
            while index < new_capacity:
                new_arr[index] = self._data[index]
                index += 1
        else:
            # transfer over the values from the previous static array
            while index < self._data.length():
                new_arr[index] = self._data[index]
                index += 1

        # set new capacity to the current array's capacity
        self._capacity = new_capacity

        # set the current data to refer to the newly created Static Array
        self._data = new_arr

    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.
        If the internal storage associated with the dynamic array is already full, it will double its capacity beforee
        before adding the new value.
        """

        # check if an array is full, call resize, double capacity
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        # add value and increase size
        self._data[self._size] = value
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index.
        If the provided index is invalid, then it will raise an exception.
        """

        # checking for invalid index.
        if index < 0 or index > self._size:
            raise DynamicArrayException

        # if exception is not raised then moving forward with inserting at the given index.
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        This method removes a value at the specified index.
        If the provided index is invalid, then it will raise an exception.
        """
        if index < 0 or index > self._size - 1:
            raise DynamicArrayException

        # if the number of elements is strictly less than .25 of the current capacity
        # capacity must be reduced to 2 * number of elements
        saved_capacity = self._capacity

        if self._capacity < 10:
            pass
        elif self._size < (.25 * self._capacity):
            self._capacity = self._size * 2
            # if the capacity reaches below 10, move it back up to 10
            if self._capacity < 10:
                self._capacity = (10 - self._capacity) + self._capacity
        # remove the element
        self._size -= 1
        # shift over every element after the index
        for index in range(index + 1, self._data.length()):
            self._data[index - 1] = self._data[index]

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This method returns a new DynamicArray object with the requested number of elements from the original array.
        """

        # verifies the starting index and the size to raise and exception if needed
        if start_index < 0 or start_index > self._size - 1 or size < 0 or start_index + size > self._size:
            raise DynamicArrayException

        # creates the new array
        new_arr = DynamicArray()

        # stepping through from the starting point through the array if an exception is not raised
        for index in range(start_index, start_index + size):
            new_arr.append(self._data[index])
        return new_arr

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes another DynamicArray object as a parameter, and appends all elements from this array onto the
        current one, in the same order in which they are stored in the input array.
        """
        # conditional check if second_da is not an instance raise error
        for index in range(second_da.length()):
            # Append the current element from the second DynamicArray to first
            self.append(second_da.get_at_index(index))

    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new dynamic array where the value of each element is derived by applying a given map_func
        to the corresponding value from the original array.
        """
        # setting up the new array
        new_arr = DynamicArray()

        for index in range(self._size):
            new_arr.append(map_func(self._data[index]))

        return new_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new dynamic array populated only with those elements from the original array for which
        filter_func returns True.
        """

        # setting up the new array
        new_array = DynamicArray()

        for index in range(self.length()):
            if filter_func(self[index]):
                new_array.append(self[index])

        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the dynamic array and returns the
        resulting value. It takes an optional initializer parameter. If this parameter is not provided, the first
        value in the array is used as the initializer. If the dynamic array is empty, the method returns the value
        of the initializer (or None, if one was not provided).
        """
        if initializer:
            start = 0
            result = initializer
        else:
            start = 1
            result = self._data[0]
        for index in range(start, self._size):
            result = reduce_func(result, self._data[index])
        return result


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    This function is outside the DynamicArray class and receives a dynamic array already in a sorted order.
    The function returns a tuple containing a dynamic array comprising the mode value(s) of the array, and an integer
    that represents the highest frequency. If there is more than one value that has the highest frequency, all values
    at that frequency will be included in the array being returned.
    """
    # setting up the new array
    new_arr = DynamicArray()

    # setting initial counters to zero including the "mode" of the array being searched through
    count = 0
    frequency = 0
    mode = arr[0]

    # stepping through the array increasing the count of each integer finding the mode and frequency
    for index in range(arr.length()):
        if arr[index] == mode:
            count += 1
        else:
            if count > frequency:
                frequency = count
            mode = arr[index]
            count = 1
    if count > frequency:
        most_appear = count
    else:
        most_appear = frequency
    frequency = 0
    for index in range(arr.length()):
        if arr[index] == mode:
            frequency += 1
        else:
            if frequency == most_appear:
                new_arr.append(mode)
            mode = arr[index]
            frequency = 1
    if frequency == most_appear:
        new_arr.append(mode)
    return new_arr, most_appear


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")

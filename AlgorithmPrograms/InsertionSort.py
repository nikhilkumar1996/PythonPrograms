"""
Program 3: Reads in strings and prints them in sorted order using insertion sort.
"""


def insertion_sort(array_input):
    """
    Sorting the elements using insertion sort.
    :param array_input: Input array provided by user for sorting.
    :return: sorted list.
    """
    # Traversing from 1 to length of the array
    for elements in range(1, len(array_input)):
        cur_pos = array_input[elements]
        # Move elements of array that are greater than k to one position ahead of their current
        next_pos = cur_pos - 1
        while next_pos >= 0 and cur_pos < array_input[next_pos]:
            array_input[next_pos + 1] = array_input[next_pos]
            next_pos -= 1
            array_input[next_pos + 1] = cur_pos
        return array_input


if __name__ == "__main__":
    no_of_elements = int(input("Enter number of elements : "))
    arr_input = []
    # Taking inputs from the user to fill up the values in the list
    for element in range(no_of_elements):
        _element = int(input("Enter a number: "))
        arr_input.append(_element)
    sorted_array = insertion_sort(arr_input)
    print("Sorted array: ")
    for index in sorted_array:
        print(index)

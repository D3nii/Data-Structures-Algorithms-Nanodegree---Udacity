def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or number is None or input_list == []:
        return -1

    first, last = input_list[0], input_list[len(input_list) - 1]

    idx = rotated_array_pivot(input_list)
    pivot = input_list[idx]

    if number == pivot:
        return idx

    # Checking the first half
    num = binary(input_list[0: idx], number)
    if num != -1:
        return num

    # Checking the next half
    num = binary(input_list[pivot: len(input_list)], number)
    if num != -1:
        return num + idx

    return -1


def rotated_array_pivot(input_list):
    pivot = -1
    first, last = 0, len(input_list) - 1

    while first <= last:
        mid = (first + last) // 2
        fitem = input_list[first]
        litem = input_list[last]
        mitem = input_list[mid]

        if fitem <= litem:
            pivot = first
            break
        elif fitem <= mitem:
            first = mid + 1
        elif mitem <= litem:
            last = mid
        else:
            break

    return pivot


def binary(arr, target):
    first, last = 0, len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        temp = arr[mid]

        if target == temp:
            return mid
        elif target < temp:
            last = mid - 1
        else:
            first = mid + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Extra cases
test_function([[], -1])
test_function([[1], 0])

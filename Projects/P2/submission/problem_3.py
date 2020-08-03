def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

    temp = reverse_sort(input_list)
    temp1, temp2 = list(), list()

    for i in temp:
        if len(temp1) > len(temp2):
            temp2.append(str(i))
        else:
            temp1.append(str(i))

    ans1, ans2 = ''.join(temp1), ''.join(temp2)

    return [int(ans1), int(ans2)]

def reverse_sort(list):
    if len(list) <= 1:
        return list

    idx = len(list) // 2
    left = list[:idx]
    right = list[idx:]

    left = reverse_sort(left)
    right = reverse_sort(right)

    return merge(left, right)

def merge(left, right):
    answer = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            answer.append(right[r])
            r += 1
        else:
            answer.append(left[l])
            l += 1

    answer += left[l:]
    answer += right[r:]

    return answer

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

print(rearrange_digits([4, 6, 2, 5, 9, 8]))  # [964, 852]]
print(rearrange_digits([2, 1]))  # [2, 1]
print(rearrange_digits([42]))  # [42]
print(rearrange_digits(None))  # None
print(rearrange_digits([2, 1, 9, 7, 8]))  # [971, 82]
print(rearrange_digits([8, 7, 6, 4, 2, 1]))  # [862, 741]
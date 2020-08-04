def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    max, min = -float('inf'), float('inf')

    for i in ints:
        if i > max:
            max = i
        elif i < min:
            min = i

    return (min, max)

## Example Test Case of Ten Integers
import random

# Testing

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(-20, 20)]  # a list containing -12 - 19
random.shuffle(l)
print ("Pass" if ((-20, 19) == get_min_max(l)) else "Fail")

l = []  # an empty list
random.shuffle(l)
print ("Pass" if (None == get_min_max(l)) else "Fail")

l = [i for i in range(-20, -10)]  # an list containing -20 - 11
random.shuffle(l)
print ("Pass" if ((-20, -11) == get_min_max(l)) else "Fail")

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Special Cases
    if number is None or number < 0:
        return None
    if number == 1 or number == 0:
        return number

    start, end = 0, number // 2

    while start <= end:
        mid = (start + end) // 2
        temp = mid * mid

        if temp == number:
            return mid

        elif temp < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans

print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Extra tests
print ("Pass" if  (None == sqrt(-27)) else "Fail")
print ("Pass" if  (99380 == sqrt(9876543210)) else "Fail")

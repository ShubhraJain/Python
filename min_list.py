def two_min_values(a):
    """
    Returns first 2 minimum values in a list
    """
    l = len(a)
    if l < 2:
        return "List is too small"
    else:
        min1 = a[0]
        min2 = a[1]
        if min2 < min1:
            c = min1
            min1 = min2
            min2 = c
        for n in range(2, l):
            if a[n] < min1:
                min2 = min1
                min1 = a[n]
            elif a[n] > min1 and a[n] < min2:
                min2 = a[n]
    return ("1st min value is %d and 2nd min value is %d" %(min1, min2))

print(two_min_values([33, 45, 9, 7, 2, 8, 19, 10, 60, 32]))
print(two_min_values([4]))
print(two_min_values([3,1]))
print(two_min_values([33, 5, 9]))
print(two_min_values([33, 33]))
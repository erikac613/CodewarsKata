def remove_smallest(numbers):
    if(len(numbers) == 0):
        return []

    sval = None
    sidx = None

    for idx,num in enumerate(numbers):
        if (sval == None) or (num < sval):
            sval = num
            sidx = idx

    numbers.pop(sidx)

    return numbers

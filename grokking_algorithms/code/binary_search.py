def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low < high:
        mid = (low + high) / 2
        if item == l[mid]:
            return mid
        elif item < mid:
            high = mid - 1
        else:
            low = mid + 1
    return None

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
item = 5
print(binary_search(l, item))

def binary_search_recursive(l, item, low, high):
    mid = int((low + high) / 2)
    if item == l[mid]:
        return mid
    elif item < l[mid]:
        return binary_search_recursive(l, item, low, mid - 1)
    else:
        return binary_search_recursive(l, item, mid + 1, high)
    return None

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
item = 5
print(binary_search_recursive(l, item, 0, len(l) - 1))
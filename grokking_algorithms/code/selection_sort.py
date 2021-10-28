def selection_sort(l):
    src = l
    dest = []
    while len(src) != 0:
        lowest = src[0]
        for i in src:
            if i < lowest:
                lowest = i
        dest.append(lowest)
        l.remove(lowest)
    return dest

l = [8,6,7,5,3,0,9,-1,-1000]
print(selection_sort(l))
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_list([1,2,3,4,5], 2))  # [3, 4, 5, 1, 2]
print(rotate_list([1,2,3,4,5], 5))  # [1, 2, 3, 4, 5]
print(rotate_list([1,2,3,4,5], 7))  # [3, 4, 5, 1, 2]

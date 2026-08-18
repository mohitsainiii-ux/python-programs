def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1 & set2
    return list(intersection)
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
result = find_intersection(list1, list2)
print("Intersection of the two lists:", result)
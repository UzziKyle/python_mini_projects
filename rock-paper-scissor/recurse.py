def recurse(list = list) -> int:
    if len(list) == 1:
        return list[0]
    else:
        mid = len(list)//2
        return recurse(list[:mid]) + recurse(list[mid:])
list = [1,2,3,4,5]
print(recurse(list))
print(sum(list))
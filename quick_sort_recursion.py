def quick_sort(s: list) -> list:
    if len(s) <= 1:
        return s
    middle = len(s) // 2
    right = []
    left = []
    if s:
        center = s.pop(middle)
    for i in s:
        if i > center:
            right.append(i)
        if i <= center:
            left.append(i)
    return quick_sort(left) + [center] + quick_sort(right)
    
print(quick_sort([11, 15, 33, 19, 20, 20, 6, 4, 16, 8, -2, 33,]))

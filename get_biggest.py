def get_biggest(numbers: list) -> int:
    """Find the largest number of all the numbers that can be made from the combinations of digits in each number"""
    if not numbers:
        return -1
    else:
        lst = list(map(str, numbers))
        n = len(max(lst, key=len))
        numbers.sort(key=lambda x: str(x) * n, reverse=True)
        return int(''.join([str(i) for i in numbers]))

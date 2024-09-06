n = 2
k = 1

warriors = list(range(1, n + 1))

while len(warriors) > 1:
    count = 0
    while count < k - 1:
        warriors.append(warriors.pop(0))
        count += 1
    warriors.remove(warriors[0])

print(*warriors)
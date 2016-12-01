pair = input().split()
i = 0
while int(pair[0]) and int(pair[1]):
    if not int(pair[0])%2:
        if not int(pair[1])%7:
            if len(pair[0]) >=3 and len(pair[1]) >= 3:
                i += 1
    pair = input().split()
print(i)
values = [int(i) for i in str(input()).split()]
m = 0
count = 1
for x in values:
    if x == 0:
        break
    elif x > m:
        m = x
        count = 1
    elif x == m:
        count += 1
print(count)
N = int(input())
data = str(input()).split()
dictionary = {}
for i in range(len(data)):
    if data[i] in dictionary.keys():
        dictionary[data[i]] += 1
    else:
        dictionary[data[i]] = 1

popular_goods = sorted(dictionary, key = dictionary.get, reverse = True)

number_of_equals = 0

values = list(dictionary.values())
for i in range(len(values)):
    for j in range(len(values)):
        if values[i] == values[j] and i != j:
            number_of_equals += 1

print(number_of_equals) #кол-во совпавших
print(dictionary[popular_goods[1]]) #вторые по популярности
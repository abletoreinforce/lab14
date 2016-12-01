values = [str(i) for i in str(input()).split()]
N_10 = int(values[1],int(values[0]))
N_new_base = ''
while N_10:
    char = str(N_10%int(values[2]))
    N_10 = N_10//int(values[2])
    N_new_base += char
print(N_new_base[::-1])
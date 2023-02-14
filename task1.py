n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
list_1 = []
for i in range(n):
    num = int(input("Введите число: "))
    list_1.append(num)
list_2 = []
for j in range(m):
    num = int(input("Введите число: "))
    list_2.append(num)
col_1 = set(list_1)
col_2 = set(list_2)
cross = col_1.intersection(col_2)
list = list(cross)
list.sort()
print(list)

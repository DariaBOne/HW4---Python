N = int(input("Введите количество кустов: "))
if N<3:
    print("кустов минимум 3!!!")
berry = []
for i in range(N):
    num = int(input("Введите число: "))
    berry.append(num)
var_first = berry[0]+berry[N-1]+berry[1]
var_last = berry[0]+berry[N-1]+berry[N-2]
if var_first>var_last:
    var_max = var_first
else: var_max = var_last
j = 1
while j<N-1:
    var = berry[j]+berry[j-1]+berry[j+1]
    if var>var_max:
        var_max = var
    j+=1
print(var_max)
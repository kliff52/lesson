a = 1
b = 2
c = 3
print(a,b,c)
print("-------next-------")
time = float(input("Введите время в секундах - "))
minutes = time / 60
hour = minutes / 60
print(round(time),"секунд это -", round(hour),"часа или", round(minutes), "минут")
print("------next-----")
n = input("Введите число n")
n1 = n+n
n2 = n+n+n
p = int(n) + int(n1) + int(n2)
print(n,"+",n1,"+",n2,"=",p)
x = int(input("Введите целое положительное число"))
ls = []
while x > 10:
    ls.append(x % 10) # Записываем остаток от деления
    x //= 10 # Целая часть от деления
r = max(ls)
print(r)
print("------next-----")
viruchka = int(input("Введите выручку"))
izderjki = int(input("Введите издержки фирмы"))
if viruchka > izderjki:
    print("прибыль")
    r = (viruchka - izderjki) # Прибыль
    e = (r / viruchka)*100
    print(e, "- Рентабельность", r,"-прибыль")

else:
    print("Убыток")

man = int(input("Введите количество сотрудников"))
var = r / man
print(round(var), "рублей на одного сотрудника")
print("--------next---------")
a2 = int(input("Введите количество км"))
a3 = int(input("Введите желаемое"))
d = 1
while a2 < a3:
    a2 = a2 * 1.1
    d = d + 1
    print(a2)
print("За", d, " дней")
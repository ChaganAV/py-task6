sNumber = input("Введите номер билета: ")
sum1 = 0
sum2 = 0
count = 0
number = int(sNumber)
min = 99999
max = 1000000
if min < number < max:
    count = len(sNumber)/2
    while number > 0:
        sum+=number//max
        num = num%max
        max = max//10
else:
    print("Вам выпал не счастливый билетик :(")
print(sum)
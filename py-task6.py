sNumber = input("Введите номер билета: ")
sum1 = 0
sum2 = 0
count = 0
number = int(sNumber)
if len(sNumber)%2 != 0:
    print("Сожалею, вам выпал не счастливый билетик :(")
else:
    middle = len(sNumber)//2
    max = 10**len(sNumber)
    while number > 0:
        max = max//10
        if count < middle:
            sum1+=number//max
        else:
            sum2+=number//max
        number = number%max
        count+= 1
    if sum1 == sum2:
        print("Поздравляю, вам выпал счастливый билетик, возмите с полки пирожок :)")
    else:
        print("Сожалею, вам выпал не счастливый билетик :(")



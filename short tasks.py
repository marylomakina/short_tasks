#На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму.
# Если сумма больше 21 и среди чисел есть 11, то уменьшить общую сумму на 10.
# И, наконец, если сумма в тч после уменьшения превышает 21, вернуть BUST
def bust(nums):
    if sum(nums) > 21 and 11 in nums:
        return sum(nums) - 10 if sum(nums) - 10 <= 21 else 'BUST'
    return sum(nums)


#вернуть сумму чисел в массиве, кроме набора чисел, который начинается с 6 и заканчивается 9
# ( для каждого числа 6 далее где-то будет число 9). Вернуть 0, если чисел нет.

def summer_69(arr):
    _sum = 0
    add = True
    for num in arr:
        if num != 6 and add is True:
            _sum += num
        elif num == 6:
            add = False
        elif num == 9:
            add = True
    return(_sum)
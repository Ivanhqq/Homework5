# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(n):
    count = 1
    res = ''
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            count += 1
        else:
            res = res + str(count) + n[i]
            count = 1
    if count > 1 or (n[len(n)-2] != n[-1]):
        res = res + str(count) + n[-1]
    return res

def decompression(n):
    number = ''
    res = ''
    for i in range(len(n)):
        if not n[i].isalpha():
            number += n[i]
        else:
            res = res + n[i] * int(number)
            number = ''
    return res

i = input("Сжать (1) или Восстановить (2): ")

if i == 1:
    s = input("Введите текст для сжатия: ")
    print(f"Текст после сжатия: {compression(s)}")
else:
    p = input("Введите текст для восстановления: ")
    print(f"Текст после восстановления: {decompression((p))}")
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


from subprocess import list2cmdline


def remove_text(lis):
    for i in lis:
        if "абв" in i:
            lis.remove(i)
    lis2 = " ".join(lis)
    return lis2


x = input('Введи текст: ')

sort = x.split()

print(remove_text(x))

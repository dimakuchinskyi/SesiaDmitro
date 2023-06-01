numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parni = []
for i in numbers:
    if i % 2 == 0:
        parni.append(i)
print('Список парних чисел:', parni)
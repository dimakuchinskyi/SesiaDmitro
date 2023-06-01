start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))
sum_of_range = 0
for num in range(start + 1, end):
    sum_of_range += num
print("Сума діапазону чисел:", sum_of_range)

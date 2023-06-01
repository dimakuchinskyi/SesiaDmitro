def filter_capitalized_strings(strings):
    filtered_strings = []
    for string in strings:
        if string[0].isupper():
            filtered_strings.append(string)
    return filtered_strings
user_input = input("Введіть рядки, розділені пробілами: ")
input_list = user_input.split()
filtered_list = filter_capitalized_strings(input_list)
print("Результат:")
for string in filtered_list:
    print(string)

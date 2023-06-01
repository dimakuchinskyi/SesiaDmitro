def filter_python_strings(string_list):
    python_strings = []
    for string in string_list:
        if 'Python' in string:
            python_strings.append(string)
    return python_strings
user_strings = ['Python чудова мова програмування', 'Я люблю мову програмування Python', 'Джава також чудова мова програмування']
filtered_strings = filter_python_strings(user_strings)
print(filtered_strings)

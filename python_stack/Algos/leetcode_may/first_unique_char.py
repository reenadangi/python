def first_unique_char(string):
    for i in range(len(string)):
        if string[i] not in string[i+1:] and string[i] not in string[:i]:
            return string[i]
print(first_unique_char("asacbsdj"))
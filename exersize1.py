string = input("Enter the string:")
i = 0
while i < len(string):
    if (not string[i].isalnum()) and string[i] != ' ':
        string = string[: i] + ' ' + string[i + 1:]
    else:
        i += 1
string = string.lower().split()
dict = {}
for i in string:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1

dict = sorted(dict.items())
for i in dict:
    print(i[0], ': ', str(i[1]))

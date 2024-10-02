first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

f_s = list(zip(first,second))
first_result = (abs(len(x[0])-len(x[1])) for x in f_s if len(x[0]) != len(x[1]))
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))

print(list(first_result))
print(list(second_result))
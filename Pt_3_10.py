s = str(input('Введите предложение: ')).lower()
s_list = list(s.replace(" ", ""))
print(s_list)
my_dict = {s_list[i]: s.count(s_list[i]) for i in range(0, len(s_list))}
print(my_dict)

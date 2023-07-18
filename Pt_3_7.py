s = str(input('Введите предложение: '))
s_list = list(s.replace(" ", ""))
my_dict = {s_list[i]: (True if s_list[i] in 'ауоыиэяюёе' else False) for i in range(len(s_list))}
print(my_dict)

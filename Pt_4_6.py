alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
smeshenie = int(input('Введите количество сдвигов: '))
message = input("Введите предложение: ")
rez = ''
for i in message:
    ind = alfavit.find(i)
    new_ind = ind + smeshenie
    if i in alfavit:
        rez += alfavit[new_ind]
    else:
        rez += i
print(rez)

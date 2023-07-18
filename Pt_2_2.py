arr = ['Вечерний Ургант', 'Поедем поедим', 'Уральские пельмени', 'Орёл и решка']
for i in range(len(arr)):
    s = arr[i]
    print(s)
name = str(input('Введите название передачи: '))
number = int(input('Введите номер позиции: '))
print()
arr.insert(number - 1, name)
for i in range(len(arr)):
    s = arr[i]
    print(s)

import random
arr=['красный','голубой','жёлтый','зелёный','розовый']
print(*arr)
print()
a=str(input('Введите название цвета: '))
i=random.randint(0,len(arr)-1)
while arr[i]!=a:
 if arr[i]=='красный':
  print('На этот цвет нельзя переходить дорогу')
  a=str(input('Ведите название цвета: '))
 elif arr[i]=='голубой':
  print('Цвет неба')
  a=str(input('Ведите название цвета: '))
 elif arr[i]=='желтый':
  print('Цвет солнца')
  a=str(input('Ведите название цвета: '))
 elif arr[i]=='зелёный':
  print('Можно переходить дорогу')
  a=str(input('Ведите название цвета: '))
 elif arr[i]=='розовый':
  print('Можно переходить дорогу')
  a=str(input('Цвет Барби: '))
print("Отлично!")

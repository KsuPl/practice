import pandas as pd

df = pd.read_csv('books.csv')
y1 = int(input('Введите начальный год: '))
y2 = int(input('Введите конечный год: '))
if max(df['Год выпуска'].astype(int)) >= y1 and \
        min(df['Год выпуска'].astype(int)) <= y2:
    print(df.loc[(df['Год выпуска'].astype(int) >= y1) & (
            df['Год выпуска'].astype(int) <= y2)])
else:
    print('Книги не найдены')

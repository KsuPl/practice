import pandas as pd

df = pd.read_csv('books.csv')
n = int(input('Введите число книг: '))
for i in range(n):
    dop_books = {'Книга': input('Название книги: '),
                 'Автор': input('Автор: '),
                 'Год выпуска': input('Год выпуска: ')}
    df.loc[len(df.index)] = dop_books
df.to_csv('books.csv', index=False)
print(df)
s = str(input('Введите автора: '))
df2 = df.loc[(df['Автор'] == s)]
if df2.empty:
    print('Автор не найден')
else:
    print(df2)

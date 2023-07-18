import pandas as pd

name = ['Гордость и предубеждение', 'Горе от ума',
        'Великий Гэтсби', 'Триумфальная арка']
author = ['Джейн Остин', 'А.С.Грибоедов',
          'Фрэнсис Скотт Фицджеральд', 'Эрих Мария Ремарк']
year = ['1813', '1825', '1925', '1945']
favorite_books = {'Книга': name,
                  'Автор': author,
                  'Год выпуска': year}
favorite_books_df = pd.DataFrame(favorite_books)
print(favorite_books_df)
favorite_books_df.to_csv('books.csv', index=False)

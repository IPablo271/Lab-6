import pandas as pd

# Cargar los datos de los CSV en DataFrames
ratings = pd.read_csv('./data/ratings.csv')
books = pd.read_csv('./data/books.csv')

# Eliminar las columnas no deseadas del DataFrame 'books'
books = books.drop(['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1)

# Realizar la unión basada en la columna ISBN
merged_data = pd.merge(ratings, books, on='ISBN', how='inner')

# Guardar los resultados en un nuevo archivo CSV
merged_data.to_csv('merged_data.csv', index=False)

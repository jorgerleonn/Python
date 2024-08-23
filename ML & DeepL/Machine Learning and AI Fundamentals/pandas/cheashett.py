#.......................para renombrar una columna en concreto....................
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns = {
  'name': 'movie_title'
}, 
inplace = True)
print(df)

#.......................multi merge..............................
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
  orders,
  products.rename(columns = {'id': 'product_id'})
  )
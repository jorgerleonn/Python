#EJEMPLO DE COMO UTILIZAR LA LIBRERIA CSV PARA ABRIR Y SACAR DATOS CONCRETOS DE CHUNKS DE TEXTO
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [
    book['ISBN'] 
    for book 
    in books_reader
    ]
  
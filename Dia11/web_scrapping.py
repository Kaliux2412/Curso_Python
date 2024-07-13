#Para hacer web scrapping debemos de prestar atención a los permisos
# que el sitio cuenta para ver si podemos realizar el scrapping o no
#porque si no prestamos atención podemos bloquear nuesta IP que accede a
#el sitio que queremos usar para nuestro programa


############
#  PARCING ES UNA ACCIÓN QUE LAS COMPUTADORAS Y PROGRAMAS HACEN PARA COMBETIR UN TIPO DE DATO STRING
#  EN EL TIPO DE DATO QUE NECESITAMOS
#############

#importar beautifulsoup4 y requests

import bs4
import requests

"""busqueda = requests.get("https://losinterrogantes.com/series")
#Convertir el texto y estructura html en un objeto
sopa = bs4.BeautifulSoup(busqueda.text, "lxml")

imagenes = sopa.select('.cwvlazyload')
for i in imagenes:
    print(i)

columna = sopa.select('.preview-mini-wrap')
for b in columna:
    print(b.getText())
"""
#Scraping BOOKS

#crear url modificable
url_base = 'http://books.toscrape.com/catalogue/category/books_1/page-{}.html'
#lista de titulos con rating de 4 a 5 estrellas
titulos_rating = []

#paginas de la cantidad de libros
for pagina in range(1,51):
    #crear sopa par CADAPAGINA
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    #seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    #enumerar libros
    for libro in libros:
        #checamos que tengan las estrellas que queremos
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            #guardar el titulo del libro que cumple con la función
            titulo_libro = libro.select("a")[1]["title"]

            #agregar libro a la lista de libros asignada
            titulos_rating.append(titulo_libro)

#ver libros seleccionados
for l in titulos_rating:
    print(l)



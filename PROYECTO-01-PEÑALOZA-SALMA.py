#Login de usuario, basado en dos variables definidas para accesar.
if __name__ == "__main__":
    USUARIO = 'Administracion1'
    CONTRASENA = 'Tepoztlan2021'
username = input('Ingrese su nombre de usuario:\n > ')
password = input('Ingrese la contraseña:\n > ')

if username== USUARIO:
    if password == CONTRASENA:
        print("Bienvenido al programa de Lifestore:"
        )
    else:
        print('Contraseña erronea')
else: ('El usuario no existe')


from lifestore_file import lifestore_products,lifestore_sales, lifestore_searches

#Obtención de ventas netas, el proceso crea una lista de ventas 
# que no contemple las devoluciones:
ventas=[]
for sales in lifestore_sales:
    refund=sales[4]
    if refund==1:
        continue
    else:
        ventas.append(sales)


#El proceso crea una lista para agrupar las ventas por mes:
meses=['/01/','/02/','/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']

ventas_por_mes=[]
for mes in meses:
    lista_vacia=[]
    ventas_por_mes.append(lista_vacia)

for venta in ventas:
    id_venta=venta[0]
    fecha=venta[3]

    contador_de_mes=0

    for mes in meses:
        if mes in fecha:
            ventas_por_mes[contador_de_mes].append(id_venta)
            continue
        contador_de_mes=contador_de_mes+1

contador_de_mes=0
for venta_mensual in ventas_por_mes:
    print(f'En el mes de {meses[contador_de_mes]} hubo {len(venta_mensual)} ventas')
    contador_de_mes=contador_de_mes+1 

#El proceso genera una lista con las ganancias mensuales:
ganancias_mensuales=[]
for venta_mensual in ventas_por_mes:
    ganancia_del_mes=0
    for id_venta in venta_mensual:
        indice_de_venta=id_venta-1
        info_de_venta=lifestore_sales[indice_de_venta]
        
        id_prod=info_de_venta[1]
        indice_de_prod=id_prod-1
        info_del_prod=lifestore_products[indice_de_prod]
        precio_de_prod=info_del_prod[2]
        ganancia_del_mes=ganancia_del_mes+precio_de_prod
    ganancias_mensuales.append(ganancia_del_mes)
print('Las ganancias mensuales son: ',ganancias_mensuales)


#El proceso genera a partir de una lista vacía las ventas por categoría:
category=[]
for products in lifestore_products:
    type_of_category=products[3]
    category.append(products)

categoria=['procesadores','tarjetas de video','tarjetas madre',
'discos duros','memorias usb','pantallas','bocinas','audifonos']
categoria_lista=[]
for categ in categoria:
    vacia_lista=[]
    categoria_lista.append(vacia_lista)

for categories in category:
    id_venta=categories[0]
    por_categoria=categories[3]

    contador_categoria=0

    for categ in categoria:
        if categ in por_categoria:
            categoria_lista[contador_categoria].append(id_venta)
            continue
        contador_categoria=contador_categoria+1 

contador_categoria=0
for categoria_mensual in categoria_lista:
    print(f'En la categoria de {categoria[contador_categoria]} hubo {len(categoria_mensual)} ventas')
    contador_categoria=contador_categoria+1

#El proceso crea primero una lista para agrupar los datos referentes
# a las Reseñas:
prod_reviews = []
for prod in lifestore_products:
    id_prod = prod[0]
    sublista = [id_prod, 0 , 0]
    prod_reviews.append(sublista)
for venta in lifestore_sales:
    id_prod = venta[1]
    review = venta[2]
    
    indice = id_prod - 1
    prod_reviews[indice][1] += review
    prod_reviews[indice][2] += 1
    
for indice, lista in enumerate(prod_reviews):
   suma = lista[1]
   cant = lista[2]
   if cant > 0:
       calf_prom = suma / cant
       prod_reviews[indice][1] = calf_prom

# Basados en la lista anterior, se pretende con este proceso
# crear una sublista para encontrar, clasificar y ordenar a los productos
# mejor calificados:

mejores_calificados=[]

for lista in prod_reviews:
    sublista = [lista[1], lista[0]]
    mejores_calificados.append(sublista)

mejores_calificados.sort(reverse=True)
for rev in mejores_calificados[:5]:
    print('Los cinco productos con la máxima puntuación en reseña son: ',
    rev)

# Basados en la lista anterior, se pretende con este proceso
# crear una sublista para encontrar, clasificar y ordenar a los productos
# mejor vendidos:

mejores_vendidos= []
for lista in prod_reviews:
    sublista = [lista[2], lista[0], lista[1]]
    mejores_vendidos.append(sublista)

mejores_vendidos.sort(reverse=True)
for rev in mejores_vendidos[:5]:
    print('Los 5 productos mejor vendidos son: ', rev)












   

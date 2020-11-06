from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

# print(lifestore_products) para comprobar que se hayan importado bien

admistrador= "pedro"
password= 123
usuarios_admin=[["pedro",123], ["Juan",321]]

usr_name  = input("Ingresa tu usuario: ")
usr_pasword = int(input("Ingresa tu contraseña: "))

es_admin=0 #no es  administrador

for usuario in usuarios_admin:
    if usuario[0]== usr_name and usuario [1] == usr_pasword:
        es_admin =1 #es administrador

if es_admin==1:
  print("Bienvenido")
  print("elige una opción")
  print("Ventas totales por producto")
  print("1.-Ventas totales por producto\n 2.-reporte por mes\n 3.- productos rezagados")
  opcion = int( input("opcion seleccionada ->  "))

  if opcion==1:
    contador = 0
    lista_de_ventas_producto = []
    for producto in lifestore_products:
      for venta in lifestore_sales: 
        fecha=venta[3]
        if producto[0]==venta[1] and fecha[3:5]=="10":
          contador +=1
      lista_de_ventas_producto.append([producto[0],contador])
      contador = 0
    print(lista_de_ventas_producto)
    lista_ordenada=[]
    
    while lista_de_ventas_producto:
        mayor = lista_de_ventas_producto[0][1]
        lista_actual=lista_de_ventas_producto[0]
        for producto in lista_de_ventas_producto:
            if producto[1]>mayor:
                mayor=producto[1]
                lista_actual=producto
        lista_ordenada.append(lista_actual)
        lista_de_ventas_producto.remove(lista_actual)


    print(lista_ordenada)
else:
    print("No eres administrador, acceso denegado")
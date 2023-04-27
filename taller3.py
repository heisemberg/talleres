# #Punto 1
# try:
#     a = int(input('Ingrese número 1: '))
#     b = int(input('Ingrese número 2: '))
#     if a > b:
#         print (b,a)
#     else:
#         print(a,b)

# except ValueError:
#     print('Ingrese un valor numerico')


#Punto 2

# n1 = int(input('Ingrese un numero entre 1 y 10: '))
 
# if 1<= n1 <=10:
#     match n1:
#         case 2:
#             print('Es par')

#         case 4:
#             print('Es par')

#         case 6:
#             print('Es par')

#         case 8:
#             print('Es par')

#         case 10:
#             print('Es par')  

#         case other:
#             print('Es impar')  
# else:
#     print('El rango no es válido')     


#Punto 3

# n1 = int(input('Ingrese un numero entre 1 y 10: '))
 
# if 1<= n1 <=10:
#     match n1:
#         case 1:
#             print('Uno')

#         case 2:
#             print('Dos')

#         case 3:
#             print('Tres')

#         case 4:
#             print('Cuatro')

#         case 5:
#             print('Cinco')  

#         case 6:
#             print('Seis')

#         case 7:
#             print('Siete')

#         case 8:
#             print('Ocho')

#         case 9:
#             print('Nueve')

#         case 10:
#             print('Diez')  
         
# else:
#     print('El rango no es válido')   

#Punto 4
# llamada = float (input('Cuanto duró la llamada?: '))
# if llamada <= 3:
#     costo = 200
#     print('El costo de la llamada es de', costo, 'pesos')
# else:
#     costo = 200 + (llamada - 3)*100
#     print('El costo de la llamada es de', costo, 'pesos')

#Punto 5

# y = int(input('Ingrese cantidad conejos blancos vendidos: '))
# x = int(input('Ingrese cantidad conejos negros vendidos: '))
# n = y + x

# p1 = float(input('Ingrese precio conejos blancos: '))
# p2 = float(input('Ingrese precio conejos negros: '))
# pt = (p1 *y) + (p2 * x)

# print('Se vendieron', n, 'conejos en total')

# print ('El monto total vendido es de', pt, 'pesos')

# if y > x:
#     print('Se vendieron mas conejos blancos')
# elif y == x:
#     print('Se vendieron igual cantidad de conejos')
# else:
#     print('Se vendieron mas conejos negros')


#Punto 6

try:
    
    np1 = float(input('Ingrese nota previo 1: '))
    np2 = float(input('Ingrese nota previo 2: '))
    np3 = float(input('Ingrese nota previo 3: '))
    nt1 = float(input('Ingrese nota trabajo 1: '))
    nt2 = float(input('Ingrese nota trabajo 2: '))

    if 1<= np1 and np2 and np3 and nt1 and nt2 <=5:

        ntp = ((np1 + np2 + np3) / 3) * 0.60
        ntt = ((nt1 + nt2) / 2) * 0.40
        nf = ntp + ntt
        print ('La nota final es de', nf)
    
    else:
        print('Uno de los valores se encuentra fuera del rango válido')

except ValueError:
    print('Ingrese solo caracteres numericos')

#Punto 7
# nombreArt = input('Ingrese el nombre del articulo: ')
# clave = int(input('Ingrese la clave: '))
# precio = float(input('Ingrese el valor de producto: '))
# cantidad = input ('Ingrese la cantidad de procuctos: ')

# if clave == 1:
#     precioDes = precio - (precio * 0.1)
# elif clave == 2:
#     precioDes = precio - (precio * 0.2)

# print('Articulo: ', nombreArt, '\n', 'Clave: ',clave,'\n', 'Precio: ', precio,'\n', 'Cantidad: ',cantidad, '\n', 'Valor con Descuento: ',precioDes)

#Punto 8

# presupuesto = float(input("Ingrese el presupuesto anual: "))
# ppsiq = int(input("Cuanto porcentaje (%) Psiquiatría: "))
# pped = int(input("Cuanto porcentaje (%) Pediatría: "))
# ptrau = int(input("Cuanto porcentaje (%) Traumatología: "))

# pt = ppsiq + pped + ptrau

# if pped + ppsiq + ptrau == 100:
#     p1 = ((presupuesto*ppsiq) /100)
#     p2 = ((presupuesto*pped) /100)
#     p3 = ((presupuesto*ptrau) /100)
#     print("Al área de Psiquiatría le corresponde:", p1 , "Pediatría:", p2 , "Traumatología:", p3)
#     print("Para un total de :", p1+p2+p3)
# else:
#     print("ERROR, RANGO DE PORCENTAJE FUERA DE LIMITE 100%")


#Punto 9

# ida = int(input("Para que día del mes actual necesita el pasaje de ida:"))
# vuelta = int(input("Para que día del mes actual necesita el pasaje de vuelta:"))
# kms = int(input("Cuantos km tiene el vuelo como trayectoría ?"))

# if vuelta - ida >= 7:
#     if kms >800:
#         nato = (kms*2.5)- ((kms*2.5)*0.30)    
#         print("Se le aplicó un descuento del 30 a tu ticket y ahora vale:", nato)
#     else:
#         print("El valor de tu ticket es de:", (kms*2.5))
# else:
#         print("El valor de tu ticket es de:", (kms*2.5))




#crear ciclo for que permita ingresar n temperaturas donde n es un numero ingresado por teclado
#mostrar cuantas temperaturas estan por sobre cero y cuantas estan bajo o igual a cero.
sobrecero=0
bajocero=0
veces=int(input("Cuantas temperaturas quiere ingresar?: "))
for i in range(veces):
    tempe= float(input("Ingrese temperatura: "))
    if(tempe>0):
        sobrecero=sobrecero+1
    else:
        bajocero=bajocero+1
#mostrar daots
print("La cantidad de temperatras mayores a ceros es: "+str(sobrecero))
print("La cantidad de temperatras menores o iguales a ceros es: "+str(bajocero))
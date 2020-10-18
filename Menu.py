import os
def Numeros():
    print("****** Opcion de Nunemros*****")
    #ingresar n números, donde n es un número ingresado por teclado, calcular y mostrar: 
    #cantidad de números positivos, cantidad de números negativos, y cantidad de iguales a cero
    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
    for i in range(veces):
        nume=int(input("Ingrese un numero "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1
    print("Cantidad de números positivos: " + str(pos)+ 
        "\n Cantidad de números negativos : "+ str(neg)+ 
        "\n Cantidad de números iguales a cero: " + str(cero))    
    pausa=input("Presione una tecla para continuar")
def Datos():
    print("****** Opcion de datos de personas**")
    #ingresar para n personas donde n es un número ingresado por teclado: nombre y edad. 
    #calcular y mostrar: cantidad de personas mayores de edad y cantidad de menores de edad. 
    #subir la modificación a github con el siguiente mensaje: "se programo la opción 2 del menú"
    veces= int(input("Cuantos Personas desea ingresar?: "))
    menor=0
    mayor=0
    for i in range(veces):
        nume=int(input("Ingrese un edad "))
        if(nume<18):
            menor=menor+1
        else:
            mayor=mayor+1
    print("Cantidad de personas Menores de edad es de: "+str(menor)+
    "\n Cantidad de Personas Mayores de edad es de: "+str(mayor))


    pausa=input("Presione una tecla para continuar")
seguir=True
while(seguir):
    os.system('cls')
    print("1. Opcion numeros")
    print("2. Opcion Datos de Personas ")
    print("3. Finalizar ")
    op=int(input("Ingrese opcion "))
    if(op==1):
        Numeros()
    if(op==2):
        Datos()
    if(op==3):
        seguir=False
        break
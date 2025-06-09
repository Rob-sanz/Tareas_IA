##Recive un numero y muestra ese numero multiplicado del 1 al 10

numero = float(input("Ingrese un numero:"))

contador = 1
while contador <=10:
    res= numero * contador
    print(f'{numero}X{contador}: {res}')
    contador +=1
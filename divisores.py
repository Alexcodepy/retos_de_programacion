#Calcula los divisores de un número usando map, bucle for dentro de 
#una lista, y .join

n = 20
divisores = [i for i in range(1, n+ 1) if n% i == 0]
cantidad = len(divisores)

texto = ", ".join(map(str, divisores[:-1])) + " y " + str(divisores[-1])

print(texto)

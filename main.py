import numpy as np
def mostrarPantalla(fila, matriz):
  for fila in matriz:
    print("[", end=" ")
    for element in fila:
      print("{:3.0f}".format(element), end=" ")
    print("]")
  print()    
    
filas=int(input("Ingrese filas de la matriz: "))
columnas=int(input("Ingrese columnas de la matriz: "))
matriz1= []
for i in range(filas):
  matriz1.append([])
  for j in range(columnas):
    valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
    matriz1[i].append(valor)
print() 
mostrarPantalla(filas,matriz1)
print(matriz1)    

print("Matriz numero 2")
filas=int(input("Ingrese filas de la matriz: "))
columnas=int(input("Ingrese columnas de la matriz: "))
matriz2= []
for i in range(filas):
  matriz2.append([])
  for j in range(columnas):
    valor = int(input("Fila {}, Columna {} : ".format(i+1, j+1)))
    matriz2[i].append(valor)
print()
mostrarPantalla(filas,matriz2)

C = np.matmul(matriz1, matriz2)
print("resultado= \n", C)
def elevarCuadrado(num):
    return pow(num,2)

numeros=list(range(1,11))
print (numeros)

numerosElevados=list(map(elevarCuadrado))
print(numerosElevados)
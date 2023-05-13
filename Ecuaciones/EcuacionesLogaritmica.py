import math

def resolver_ecuacion_logaritmica(base, resultado):
    if base > 0 and base != 1 and resultado > 0:
        x = math.log(resultado, base)
        return x
    elif base == 1:
        if resultado == 1:
            return "Infinitas soluciones"
        else:
            return "No hay solución"
    else:
        return "No hay solución"

# Ejemplo de uso
base = int(input('Ingrese valor de la base:'))
resultado = int(input('Ingrese valor de resultado:'))

solucion = resolver_ecuacion_logaritmica(base, resultado)

print("La solución es:", solucion)

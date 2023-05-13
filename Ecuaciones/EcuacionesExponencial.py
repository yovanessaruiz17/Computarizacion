import math

def resolver_ecuacion_exponencial(base, exponente, resultado):
    if base > 0 and base != 1:
        x = math.log(resultado, base) / exponente
        return x
    elif base == 1:
        if exponente != 0:
            return "No hay solución"
        else:
            return "Infinitas soluciones"
    else:
        return "No existe solución"

# Ejemplo de uso
base = int(input('Ingrese valor de la base:'))
exponente = int(input('Ingrese valor del exponente:'))
resultado = int(input('Ingrese valor de resultado:'))

solucion = resolver_ecuacion_exponencial(base, exponente, resultado)

print("La solución es:", solucion)

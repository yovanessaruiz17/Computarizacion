def resolver_ecuacion_lineal(a, b):
    if a != 0:
        x = -b / a
        return x
    elif a == 0 and b == 0:
        return "Infinitas soluciones"
    else:
        return "No hay solución"

# Ejemplo de uso
a = int(input('Ingrese valor de a:'))
b = int(input('Ingrese valor de b:'))

solucion = resolver_ecuacion_lineal(a, b)

print("La solución es:", solucion)

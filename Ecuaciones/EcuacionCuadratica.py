import math
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    else:
        return "La ecuación no tiene soluciones reales."
# Ejemplo de uso
a=float(input('Ingrese valor de a:'))
b = float(input('Ingrese valor de b:'))
c = float(input('Ingrese valor de c:'))

soluciones = resolver_ecuacion_cuadratica(a, b, c)

print("Las soluciones son:", soluciones)

import numpy as np

def resolver_ecuacion_grado(coeficientes):
    grado = len(coeficientes) - 1
    raices = np.roots(coeficientes)
    return raices

# Ejemplo de uso
coeficientes = [1, -3, 2]  # Ecuación: x^2 - 3x + 2 = 0

soluciones = resolver_ecuacion_grado(coeficientes)

print("Las soluciones son:", soluciones)

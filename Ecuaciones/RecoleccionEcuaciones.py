import math
while True:
    print("MENU")
    print("1. Ecuacion Cuadratica")
    print("2. Ecuacion Cubica")
    print("3. Ecuacion Exponencial")
    print("4. Ecuacion de Grado")
    print("5. Ecuacion Logaritmica")
    print("6. Ecuacion Lineal")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")
    if opcion == 1:
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
    elif opcion==2:
        def resolver_ecuacion_cubica(a, b, c, d):
            discriminante0 = b**2 - 3*a*c
            discriminante1 = 2*b**3 - 9*a*b*c + 27*a**2*d
            C = ((discriminante1 + (discriminante1**2 - 4*discriminante0**3)**0.5)/2)**(1/3)
            if C == 0:
                x1 = -b/(3*a)
                x2 = x1
                x3 = x1
            else:
                x1 = (-1/(3*a)) * (b + C + (discriminante0/C)**0.5)
                x2_real = (-1/(3*a)) * (b + C - (discriminante0/C)**0.5)
                x2_imag = (3**0.5/(3*a)) * (b - C)
                x3_real = (-1/(3*a)) * (b - (C + (discriminante0/C)**0.5))
                x3_imag = (-3**0.5/(3*a)) * (b - C)
                x2 = complex(x2_real, x2_imag)
                x3 = complex(x3_real, x3_imag)
                return x1, x2, x3

        # Ejemplo de uso
        a = int(input('Ingrese valor de a:'))
        b = int(input('Ingrese valor de b:'))
        c = int(input('Ingrese valor de c:'))
        d = int(input('Ingrese valor de d:'))

        soluciones = resolver_ecuacion_cubica(a, b, c, d)

        print("Las soluciones son:", soluciones)
    elif opcion==3:
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
    elif opcion==4:
        import numpy as np

        def resolver_ecuacion_grado(coeficientes):
            grado = len(coeficientes) - 1
            raices = np.roots(coeficientes)
            return raices

        # Ejemplo de uso
        coeficientes = [1, -3, 2]  # Ecuación: x^2 - 3x + 2 = 0

        soluciones = resolver_ecuacion_grado(coeficientes)

        print("Las soluciones son:", soluciones)
    elif opcion==5:
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
    elif opcion==6:
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
    elif opcion==0:
        break



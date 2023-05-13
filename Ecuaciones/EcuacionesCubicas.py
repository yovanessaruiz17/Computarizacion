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

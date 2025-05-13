#Transformar la temperatura.

t = float(input("Ingrese la temperatura: "))
co = int(input("Ingrese el código 1  o 2: "))

if co == 1:
    c = 5/9 * (t - 32)
    
    print("La temperatura en grados Celsius es: ", c)
elif co == 2:
    f = 32 + 9*t/5
    
    print("La temperatura en grados Fahrenheit es: ", f)
    
else:
    print("Código inválido. Debe ser 1 o 2.")

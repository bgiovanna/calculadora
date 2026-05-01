from calculadora.operaciones import sumar, restar, multiplicar, dividir

print("Suma:", sumar(2, 2))
print("Resta:", restar(5, 3))
print("Multiplicación:", multiplicar(3, 4))

try:
    print("División:", dividir(10, 0))
except ValueError as e:
    print("Error:", e)
def fn_suma(a, b):
    total_suma = a + b
    return total_suma

if __name__ == "__main__":
    # Ejemplo de uso de la función
    a = input('ingrese un numero ')
    b = input('ingrese otro numero ')
    resultado = fn_suma(int(a), int(b))  # Aquí puedes pasar los valores que desees
    print("La suma es:", resultado)

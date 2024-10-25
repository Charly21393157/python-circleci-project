# math_operations.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    # Pruebas simples
    result_add = add(5, 3)
    result_subtract = subtract(5, 3)

    print(f"Suma: {result_add}")       # Debe imprimir "Suma: 8"
    print(f"Resta: {result_subtract}")  # Debe imprimir "Resta: 2"

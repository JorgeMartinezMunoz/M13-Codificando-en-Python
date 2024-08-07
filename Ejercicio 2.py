def convert_to_16_9(x, y):
    # Calculando la nueva resolución X manteniendo la altura Y
    new_x = round((16 / 9) * y)
    return (new_x, y)

# Ejemplo de uso
x = 1440
y = 1080
print(convert_to_16_9(x, y))  # Output: (1920, 1080)
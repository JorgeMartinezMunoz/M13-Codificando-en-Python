def calculate_water_intake(hours):
    # Nathan bebe 0,5 litros de agua por hora
    water_per_hour = 0.5
    # Calculamos la cantidad total de agua
    total_water = hours * water_per_hour
    # Redondeamos al valor entero más pequeño
    rounded_water = int(total_water)
    return rounded_water

# Ejemplo de uso
hours = 3
print(calculate_water_intake(hours))  # Output: 1
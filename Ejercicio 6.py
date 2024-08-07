def calculate_mango_cost(quantity, price_per_mango):
    # Calculamos la cantidad de mangos que se pagarán
    paid_mangos = (quantity // 3) * 2 + (quantity % 3)
    # Calculamos el costo total
    total_cost = paid_mangos * price_per_mango
    return total_cost

# Ejemplo de uso
quantity = 7
price_per_mango = 5
print(calculate_mango_cost(quantity, price_per_mango))  # Output: 25
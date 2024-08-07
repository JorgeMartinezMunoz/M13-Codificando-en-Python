def usd_to_cny(usd_amount):
    # Tasa de cambio fija: 1 USD = 6.75 CNY
    exchange_rate = 6.75
    # Convertir USD a CNY
    cny_amount = usd_amount * exchange_rate
    # Crear la cadena de salida
    result = f"{cny_amount:.2f} Yuan chino"
    return result

# Ejemplo de uso
usd_amount = 100
print(usd_to_cny(usd_amount))  # Output: "675.00 Yuan chino"
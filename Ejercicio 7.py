def calcular_presion_total(m1, M1, m2, M2, V, T):
    # Constante universal de los gases ideales en J/(mol·K)
    R = 8.314
    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * (R * T) / V
    return P_total

# Ejemplo de uso
m1 = 2.0   # masa de la primera molécula en gramos
M1 = 18.0  # masa molecular de la primera molécula en g/mol (por ejemplo, agua H2O)
m2 = 3.0   # masa de la segunda molécula en gramos
M2 = 44.0  # masa molecular de la segunda molécula en g/mol (por ejemplo, CO2)
V = 22.4   # volumen en litros
T = 298    # temperatura en Kelvin

print(calcular_presion_total(m1, M1, m2, M2, V, T))  # Output: la presión total en Pascales
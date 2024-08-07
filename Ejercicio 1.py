def calculate_pet_ages(human_years):
    if human_years < 1:
        return "Los años humanos deben ser al menos 1"

    # Calculando los años de gato
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculando los años de perro
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]


# Ejemplo de uso
human_years = 5
print(calculate_pet_ages(human_years))  # Output: [5, 36, 39]
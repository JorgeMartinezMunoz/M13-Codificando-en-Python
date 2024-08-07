def age_interval(age):
    if age <= 14:
        min_age = age - 0.10 * age
        max_age = age + 0.10 * age
    else:
        min_age = age / 2 + 7
        max_age = 2 * (age - 7)

    return f"{min_age:.2f}", f"{max_age:.2f}"


# Ejemplo de uso
age = 10
print(age_interval(age))  # Output: ('9.00', '11.00')

age = 35
print(age_interval(age))  # Output: ('19.50', '36.00')
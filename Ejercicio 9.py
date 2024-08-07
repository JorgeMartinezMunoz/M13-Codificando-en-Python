import math


def age_interval(age):
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor(2 * (age - 7))

    return min_age, max_age


# Ejemplo de uso
age = 10
print(age_interval(age))  # Output: (9, 11)

age = 25
print(age_interval(age))  # Output: (19, 36)
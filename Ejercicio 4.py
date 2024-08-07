def find_third_angle(angle1, angle2):
    # Suma de los ángulos interiores de un triángulo es 180 grados
    total_angle_sum = 180
    # Calculamos el tercer ángulo
    third_angle = total_angle_sum - (angle1 + angle2)
    return third_angle

# Ejemplo de uso
angle1 = 60
angle2 = 70
print(find_third_angle(angle1, angle2))  # Output: 50
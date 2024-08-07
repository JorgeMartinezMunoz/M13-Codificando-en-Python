def extrapolate_ppg(ppg, mpg):
    if mpg == 0:
        return 0.0
    ppg_48 = (ppg / mpg) * 48
    return round(ppg_48, 1)

# Ejemplo de uso
ppg = 25
mpg = 30
print(extrapolate_ppg(ppg, mpg))  # Output: 40.0
b = float(input("Введите BPM: "))
if b <= 0: raise ValueError("BPM должно быть положительным")
print("\n".join(
    f"{'Начальное' if n == 0 else f'Деление {n}'}: {(60000/b)/2**n:.3f} мс"
    for n in range(11)
))

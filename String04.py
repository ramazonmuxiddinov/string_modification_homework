def main(s, n):
    """
    Ism va son n berilgan. Ismni uzunligi n bo'lgan satr markaziga joylashtiring, bo'sh joylar "*" bilan to'ldirilsin (center()).
    Argumentlar:
        s(str): ism
        n(int): natija uzunligi
    Qaytaradi:
        str: natija satri
    """
    return s.center(n,'*')
print(main("Ramazon",15))

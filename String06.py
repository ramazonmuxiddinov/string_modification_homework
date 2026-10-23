def main(s, n):
    """
    Son satr ko'rinishida berilgan. Uni o'ngga tekislab, chap tomonini "0" bilan uzunlik n gacha to'ldiring (rjust()).
    Argumentlar:
        s(str): son
        n(int): natija uzunligi
    Qaytaradi:
        str: natija satri
    """
    return s.rjust(n,"0")
print(main("Ramazon",10))


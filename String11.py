def main(s):
    """
    Allamurodning ismi ikki tomonida bo'sh joylar bilan, kichik harflarda kiritildi. Bo'sh joylarni olib tashlang, bosh harfini katta qiling va uzunligi 20 bo'lgan satr markaziga "=" bilan joylashtiring (strip(), capitalize(), center()).
    Argumentlar:
        s(str): ism
    Qaytaradi:
        str: natija satri
    """
    return s.capitalize().strip().center(20,"=")
print(main("     ramazon    "))

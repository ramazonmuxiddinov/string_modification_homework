def main(sana):
    """
    Sana "kun/oy/yil" ko'rinishida berilgan. "/" belgilarini "." ga almashtiring va natijani uzunligi 16 bo'lgan satr markaziga "-" bilan joylashtiring (replace(), center()).
    Argumentlar:
        sana(str): sana
    Qaytaradi:
        str: natija satri
    """
    return sana.replace("/",".").center(16,"-")
print(main("04/10/2007"))

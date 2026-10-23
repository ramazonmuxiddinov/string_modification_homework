def main(s):
    """
    Login berilgan, ikki tomonida bo'sh joylar bor. Bo'sh joylarni olib tashlang, nuqtani "_" ga almashtiring, kichik harfga o'tkazing va natijani uzunligi 20 bo'lguncha o'ng tomondan "#" bilan to'ldiring (strip(), replace(), lower(), ljust()).
    Argumentlar:
        s(str): login
    Qaytaradi:
        str: natija satri
    """
    return s.strip().replace(" ","_").lower().ljust(20,"#")
print(main("  Ramazon.Muxiddinov "))
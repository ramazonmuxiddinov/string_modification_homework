def main(fayl):
    """
    Fayl nomi berilgan, oxirida ortiqcha bo'sh joylar va .txt kengaytmasi bor. Avval o'ng tomondagi bo'sh joylarni, so'ng .txt ni olib tashlab, faqat nomni qaytaring (rstrip(), replace()).
    Argumentlar:
        fayl(str): fayl nomi
    Qaytaradi:
        str: natija satri
    """
    return fayl.rstrip().replace(".txt","")
print(main("ramazon_cv.txt"))
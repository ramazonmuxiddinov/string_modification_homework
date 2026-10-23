def main(tel):
    """
    Telefon raqami bo'sh joy, chiziqcha va qavslar bilan yozilgan. Barcha " ", "-", "(" va ")" belgilarini olib tashlab qaytaring (replace()).
    Argumentlar:
        tel(str): telefon raqami
    Qaytaradi:
        str: natija satri
    """
    return tel.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
print(main("+998 (90) 123-45-67"))
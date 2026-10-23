def main(ism, baho):
    """
    Talaba ismi va bahosi (satr) berilgan. Ismni 10 belgigacha bo'sh joy bilan chapga, bahoni 3 belgigacha "0" bilan o'ngga tekislab, orasiga " | " qo'yib qaytaring (ljust(), rjust()).
    Argumentlar:
        ism(str): ism
        baho(str): baho
    Qaytaradi:
        str: natija satri
    """
    return ism.ljust(10)+"| "+baho.rjust(3,"0")
print(main("Ramazon","99"))
print(main("Ali","77"))


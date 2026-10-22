# Satrlarni o'zgartirish

## String01

Matn berilgan. Undagi barcha `"a"` harflarini `"o"` harfiga almashtirib qaytaring (`replace()`).

**Misol 1:**

```Python
Kirish: s="Allamurod Xakimov"
Chiqarish: "Allomurod Xokimov"
```

---

## String02

Matn berilgan. Undagi barcha bo'sh joylarni `"_"` belgisiga almashtirib qaytaring (`replace()`).

**Misol 1:**

```Python
Kirish: s="Allamurod Xakimov Toshkent"
Chiqarish: "Allamurod_Xakimov_Toshkent"
```

---

## String03

Matn berilgan. Undagi birinchi `"-"` belgisini `"."` ga almashtiring, qolganlari o'zgarmasin (`replace()`, `count` parametri).

**Misol 1:**

```Python
Kirish: s="15-03-2000"
Chiqarish: "15.03-2000"
```

---

## String04

Ism va son `n` berilgan. Ismni uzunligi `n` bo'lgan satr markaziga joylashtiring, bo'sh joylar `"*"` bilan to'ldirilsin (`center()`).

**Misol 1:**

```Python
Kirish: s="Allamurod", n=15
Chiqarish: "***Allamurod***"
```

---

## String05

Ism va son `n` berilgan. Ismni chapga tekislab, o'ng tomonini `"."` bilan uzunlik `n` gacha to'ldiring (`ljust()`).

**Misol 1:**

```Python
Kirish: s="Allamurod", n=14
Chiqarish: "Allamurod....."
```

---

## String06

Son satr ko'rinishida berilgan. Uni o'ngga tekislab, chap tomonini `"0"` bilan uzunlik `n` gacha to'ldiring (`rjust()`).

**Misol 1:**

```Python
Kirish: s="26", n=5
Chiqarish: "00026"
```

---

## String07

Boshida va oxirida ortiqcha bo'sh joylari bor satr berilgan. Ikki tomondagi bo'sh joylarni olib tashlang (`strip()`).

**Misol 1:**

```Python
Kirish: s="   Allamurod Xakimov   "
Chiqarish: "Allamurod Xakimov"
```

---

## String08

Satr berilgan. Faqat chap tomonidagi bo'sh joylarni olib tashlang (`lstrip()`).

**Misol 1:**

```Python
Kirish: s="   Toshkent   "
Chiqarish: "Toshkent   "
```

---

## String09

Satr berilgan. Faqat o'ng tomonidagi bo'sh joylarni olib tashlang (`rstrip()`).

**Misol 1:**

```Python
Kirish: s="   Toshkent   "
Chiqarish: "   Toshkent"
```

---

## String10

Satr va belgi `k` berilgan. Satrning ikki tomonidagi `k` belgilarini olib tashlang (`strip()`).

**Misol 1:**

```Python
Kirish: s="###Allamurod###", k="#"
Chiqarish: "Allamurod"
```

**Misol 2:**

```Python
Kirish: s="!!Python!", k="!"
Chiqarish: "Python"
```

---

## String11

Allamurodning ismi ikki tomonida bo'sh joylar bilan, kichik harflarda kiritildi. Bo'sh joylarni olib tashlang, bosh harfini katta qiling va uzunligi 20 bo'lgan satr markaziga `"="` bilan joylashtiring (`strip()`, `capitalize()`, `center()`).

**Misol 1:**

```Python
Kirish: s="   allamurod  "
Chiqarish: "=====Allamurod======"
```

---

## String12

Telefon raqami bo'sh joy, chiziqcha va qavslar bilan yozilgan. Barcha `" "`, `"-"`, `"("` va `")"` belgilarini olib tashlab qaytaring (`replace()`).

**Misol 1:**

```Python
Kirish: tel="+998 (90) 123-45-67"
Chiqarish: "+998901234567"
```

---

## String13

Mahsulot nomi va narxi (satr) berilgan. Nomni 12 belgigacha `"."` bilan chapga, narxni 8 belgigacha bo'sh joy bilan o'ngga tekislab, birlashtirib qaytaring (`ljust()`, `rjust()`).

**Misol 1:**

```Python
Kirish: nom="Non", narx="5000"
Chiqarish: "Non.........    5000"
```

**Misol 2:**

```Python
Kirish: nom="Sut", narx="12000"
Chiqarish: "Sut.........   12000"
```

---

## String14

Fayl nomi berilgan, oxirida ortiqcha bo'sh joylar va `.txt` kengaytmasi bor. Avval o'ng tomondagi bo'sh joylarni, so'ng `.txt` ni olib tashlab, faqat nomni qaytaring (`rstrip()`, `replace()`).

**Misol 1:**

```Python
Kirish: fayl="allamurod_cv.txt   "
Chiqarish: "allamurod_cv"
```

---

## String15

Tartib raqami satr ko'rinishida berilgan, boshida ortiqcha nollar bor. Chap tomondagi `"0"` larni olib tashlab, natijani `"ID: "` so'zi bilan qaytaring (`lstrip()`).

**Misol 1:**

```Python
Kirish: s="000452"
Chiqarish: "ID: 452"
```

**Misol 2:**

```Python
Kirish: s="0070"
Chiqarish: "ID: 70"
```

---

## String16

Sana `"kun/oy/yil"` ko'rinishida berilgan. `"/"` belgilarini `"."` ga almashtiring va natijani uzunligi 16 bo'lgan satr markaziga `"-"` bilan joylashtiring (`replace()`, `center()`).

**Misol 1:**

```Python
Kirish: sana="15/03/2000"
Chiqarish: "---15.03.2000---"
```

---

## String17

Kichik harflarda yozilgan, ikki tomonida bo'sh joyi bor ism va familiya berilgan. Bo'sh joylarni olib tashlang, so'zlarni bosh harf bilan yozing va so'zlar orasidagi bo'sh joyni `"_"` ga almashtiring (`strip()`, `title()`, `replace()`).

**Misol 1:**

```Python
Kirish: s="  allamurod xakimov "
Chiqarish: "Allamurod_Xakimov"
```

---

## String18

Talaba ismi va bahosi (satr) berilgan. Ismni 10 belgigacha bo'sh joy bilan chapga, bahoni 3 belgigacha `"0"` bilan o'ngga tekislab, orasiga `" | "` qo'yib qaytaring (`ljust()`, `rjust()`).

**Misol 1:**

```Python
Kirish: ism="Allamurod", baho="95"
Chiqarish: "Allamurod  | 095"
```

**Misol 2:**

```Python
Kirish: ism="Ali", baho="7"
Chiqarish: "Ali        | 007"
```

---

## String19

Matn berilgan, boshida `"*"`, oxirida `"!"` belgilari bor. Chapdan `"*"` larni, o'ngdan `"!"` larni olib tashlang va natijani katta harflarda qaytaring (`lstrip()`, `rstrip()`, `upper()`).

**Misol 1:**

```Python
Kirish: s="***Salom Allamurod!!!"
Chiqarish: "SALOM ALLAMUROD"
```

---

## String20

Login berilgan, ikki tomonida bo'sh joylar bor. Bo'sh joylarni olib tashlang, nuqtani `"_"` ga almashtiring, kichik harfga o'tkazing va natijani uzunligi 20 bo'lguncha o'ng tomondan `"#"` bilan to'ldiring (`strip()`, `replace()`, `lower()`, `ljust()`).

**Misol 1:**

```Python
Kirish: s="  Allamurod.Xakimov "
Chiqarish: "allamurod_xakimov###"
```


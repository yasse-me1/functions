# 1.Uchta sonni qabul qilib, ularning o‘rtachasini hisoblovchi funksiya yozing. 
def sonlar(a, b, c):
    return (a + b + c) / 3
a= int(input("a sonni kiriting: "))
b=int(input("b sonni kiriting: "))
c=int(input("c sonni kiriting: "))
print(sonlar(a,b,c))
# 2.Berilgan matnni teskari tartibda qaytaruvchi funksiya yozing (def reverse_text(text: str) -> str).
def reverse_text(text: str)->str:
    return text[::-1]
matn = input("Matnni kiriting: ")
print(reverse_text(matn))
# 3.Ro‘yxatda eng katta sonni topuvchi funksiya yozing.
def kottasi(list1):
    eng_kottasi=list1[0]
    for qol in list1:
        if qol>eng_kottasi:
            eng_kottasi=qol

    return eng_kottasi
royxat=[-25,-9,34,-3,9,-29]
print(kottasi(royxat))
# 4.Foydalanuvchidan ism va yosh so‘rab, xabar qaytaruvchi funksiya yozing.
def malumot():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    return f"Salom, sizning ismingiz {ism}, yoshingiz {yosh} da."
print(malumot())
# 5.Son juft yoki toq ekanligini tekshiruvchi funksiya yozing (def is_even(n: int) -> bool).
def is_even(n: int) -> bool:
    return n % 2 == 0
print(is_even(2))
print(is_even(9))





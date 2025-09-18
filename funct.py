# 1.Uchta sonni qabul qilib, ularning o‘rtachasini hisoblovchi funksiya yozing. 
def sonlar(a, b, c):
    return (a + b + c) / 3
natija = sonlar(2,4,6)
print(natija)
# 2.Berilgan matnni teskari tartibda qaytaruvchi funksiya yozing (def reverse_text(text: str) -> str).
def reverse_text(text: str)->str:
    return text[::-1]
matn = input("Matnni kiriting: ")
print(reverse_text(matn))
# 3.Ro‘yxatda eng katta sonni topuvchi funksiya yozing.
def katta_son(royxat):
    return max(royxat)
sonlar = [3, 7, 2, 10, 5]
print(katta_son(sonlar))

# 4.Foydalanuvchidan ism va yosh so‘rab, xabar qaytaruvchi funksiya yozing.
def malumot(ism,yosh):
    return ism,yosh
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    print(f"Salom, sizning ismingiz {ism}, sizning yoshingiz {yosh} da.")
# 5.Son juft yoki toq ekanligini tekshiruvchi funksiya yozing (def is_even(n: int) -> bool).
def is_even(n: int) -> bool:
    return n % 2 == 0
print(is_even(2))
print(is_even(9))



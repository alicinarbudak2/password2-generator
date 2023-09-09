import random

cumle = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

uzunluk = int(input("Şifre Uzunluğu:"))

sifre = ""

for i in range(uzunluk):
    sifre += random.choice(cumle)  

    print("sifre")

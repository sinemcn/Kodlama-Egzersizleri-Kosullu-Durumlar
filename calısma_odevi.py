# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 # Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 # BKİ 18.5'un altındaysa -------> Zayıf

 # BKİ 18.5 ile 25 arasındaysa ------> Normal

 # BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 # BKİ 30'un üstündeyse -------------> Obez

boy = float(input("Boyunuz: "))
kilo = int(input("Kilonuz: "))
bki = kilo / boy ** 2
if bki < 18.5:
    print("Beden Kitle İndeksiniz: Zayıf")
elif bki >= 18.5 and bki < 25:
    print("Beden Kitle İndeksiniz: Normal")
elif bki >=25 and bki < 30:
    print("Beden Kitle İndeksiniz: Fazla Kilolu")
else:
    print("Obez")
# Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a>b) and (a>c):
    print("a en büyük sayıdır.")
elif (b>a) and (b>c):
    print("b en büyük sayıdır.")
elif (c>a) and (c>b):
    print("c en büyük sayıdır.")

# Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
#
#     Vize1 toplam notun %30'una etki edecek.
#
#     Vize2 toplam notun %30'una etki edecek.
#
#     Final toplam notun %40'ına etki edecek.
#
#
#     Toplam Not >=  90 -----> AA
#
#     Toplam Not >=  85 -----> BA
#
#     Toplam Not >=  80 -----> BB
#
#     Toplam Not >=  75 -----> CB
#
#     Toplam Not >=  70 -----> CC
#
#     Toplam Not >=  65 -----> DC
#
#     Toplam Not >=  60 -----> DD
#
#     Toplam Not >=  55 -----> FD
#
#     Toplam Not <  55 -----> FF
vize1 = float(input("Vize1: "))
vize2 = float(input("Vize2: "))
final = float(input("Final: "))
ortalama = vize1*0.3+ vize2*0.3 + final * 0.4

if ortalama >= 90:
    print(f"Ortalamanız {ortalama} ve notunuz AA")
elif ortalama >=85:
    print(f"Ortalamanız {ortalama} ve notunuz BA")
elif ortalama >= 80:
    print(f"Ortalamanız {ortalama} ve notunuz BB")
elif ortalama >= 75:
    print(f"Ortalamanız {ortalama} ve notunuz CB")
elif ortalama >= 70:
    print(f"Ortalamanız {ortalama} ve notunuz CC")
elif ortalama >= 65:
    print(f"Ortalamanız {ortalama} ve notunuz DC")
elif ortalama >= 60:
    print(f"Ortalamanız {ortalama} ve notunuz DD")
elif ortalama >= 55:
    print(f"Ortalamanız {ortalama} ve notunuz FD")
else:
    print(f"Ortalamanız {ortalama} ve notunuz FF. Dersten kaldınız.")




# Problem 4
# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
#
# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
#
# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
#
# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.
#
# Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
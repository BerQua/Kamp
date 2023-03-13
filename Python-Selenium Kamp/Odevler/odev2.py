mevcutogrenci = []
sonlandir = False

def ogrenciekle():
    ogrencisayisi = int(input("Kaç tane öğrenci eklemek istiyorsunuz : "))
    for i in range(ogrencisayisi):
        ogrenciler = input("Öğrenci isim ve soyismini yazınız : ")
        mevcutogrenci.append(ogrenciler)

def ogrencikayitsil():
    silinecekogrencisayisi = int(input("Kaç öğrenci silinecek? : "))
    silinecekogrencilistesi = []
    x = 0
    while silinecekogrencisayisi:
        x += 1
        ogrencikayitsilinecek = input(
            "Silinicek öğrencileri isim soyisim olarak giriniz : ")
        silinecekogrencilistesi.append(ogrencikayitsilinecek)

        for i in mevcutogrenci:
            if i in silinecekogrencilistesi:
                mevcutogrenci.remove(i)
            else:
                continue
        if silinecekogrencisayisi == x:
            break

    print(silinecekogrencilistesi)

    print("Yeni listedeki öğrenci saysı: " + str(len(mevcutogrenci)))
    for i in mevcutogrenci:
        print("Yeni listedeki öğrencilerin isim soyisimleri : " + str(i))

def ogrencigoster():
    ogrencinumarasi = 0
    for i in mevcutogrenci:
        ogrencinumarasi += 1
        print(str(ogrencinumarasi) + " : " + str(i))

def ogrencinumarasiniogren():
    numarasiogrenilecekogrenci = input("Hangi öğrencinin numarasını öğrenmek istiyorsunuz : ")
    x = 0
    for i in mevcutogrenci:
        if i == numarasiogrenilecekogrenci:
            print("Öğrenci bulundu aradığınız, Öğrenci; '" +
                  str(i) + " Numarası : " + str(x))
        x += 1

def close():
    print("Program sonlandırılıyor!")
    for i in mevcutogrenci:
        print(i)
    sonlandir = True
    return sonlandir

def menu():
    panel = int(input("Gerçekleştirmek istediğiniz işlemi seçiniz : \n 1 = > Yeni öğrenci kaydı ekle \n 2 = > Öğrenci kaydını sil \n 3 = > Panele eklenmiş olan öğrencileri göster \n 4 = > Panele kayıtlı öğrenci numarası öğren \n 5 = > Programı sonlandır \n Paneldeki komutları kullanmak için numaralardan birini tuşlayınız."))
    if panel == 1:
        ogrenciekle()
    elif panel == 2:
        ogrencikayitsil()
    elif panel == 3:
        ogrencigoster()
    elif panel == 4:
        ogrencinumarasiniogren()
    elif panel == 5:
        return close()
    else:
        print("Hatalı bir işlem gerçekleştirdiniz, tekrar deneyiniz!")

while True:
    if menu():
        break
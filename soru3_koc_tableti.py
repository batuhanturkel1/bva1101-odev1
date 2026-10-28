komut = input("Komut: ")

match komut:
    case "mola" | "m":
        hak = int(input("Kalan mola hakkı: "))
        if hak <= 0:
            print("Mola reddedildi: hakkınız kalmadı.")
        else:
            sure = int(input("Mola süresi (sn): "))
            if sure > 180:
                print("Mola reddedildi: en fazla 180 saniye.")
            else:
                kalan = hak - 1
                kalan_metin = "hiç" if kalan == 0 else str(kalan)
                print(f"Mola başladı. Kalan hakkınız: {kalan_metin}")
    case "yedek" | "y":
        yas = int(input("Yedek oyuncunun yaşı: "))
        if yas >= 16:
            print("Oyuncu değişikliği onaylandı.")
        else:
            print("Değişiklik reddedildi: lisans yaşı 16.")
    case "ping" | "p":
        gecikme = int(input("Gecikme (ms): "))
        if gecikme >= 85:
            print("Maç durduruldu, teknik ekip masaya.")
        else:
            print("Bağlantı normal sınırlarda, maç devam ediyor.")
    case "pes":
        print("Takım çekildi. Rakip galip ilan edildi.")
    case _:
        print(f"Tanınmayan komut: {komut}")

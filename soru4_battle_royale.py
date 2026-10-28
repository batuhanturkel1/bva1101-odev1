sira = int(input("Bitiş sırası (1-20): "))

if not (1 <= sira <= 20):
    print("Geçersiz sıra: lobide 20 takım var.")
else:
    oldurme = int(input("Öldürme sayısı: "))
    sure = int(input("Hayatta kalma süresi (sn): "))
    ceza = int(input("Ceza sayısı: "))

    if sira == 1:
        siralama_puan = 15
    elif sira == 2:
        siralama_puan = 12
    elif 3 <= sira <= 5:
        siralama_puan = 9
    elif 6 <= sira <= 10:
        siralama_puan = 5
    elif 11 <= sira <= 15:
        siralama_puan = 2
    else:
        siralama_puan = 0

    oldurme_puan = 18 if oldurme > 18 else oldurme

    hayatta_kalma_bonus = sure // 300 if oldurme > 0 else 0

    sans_bonus = 3 if sira == 8 else 0

    puan = siralama_puan + oldurme_puan + hayatta_kalma_bonus + sans_bonus - (ceza * 4)
    if puan < 0:
        puan = 0

    print(f"Hayatta kalma: {sure // 60} dk {sure % 60} sn")
    print(f"Toplam puan: {puan}")

    if sira == 8:
        print("Şanslı sekiz bonusu kazanıldı!")

    if puan >= 43:
        print("Büyük finale doğrudan yükseldiniz!")
    elif 30 <= puan <= 42:
        print("Son şans turuna kaldınız.")
    else:
        print("Elendiniz. İyi oyundu!")

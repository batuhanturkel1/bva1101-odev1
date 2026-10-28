galibiyet = int(input("Kazanılan maç (0-7): "))
averaj = int(input("Raund averajı: "))
uyari = int(input("Uyarı sayısı: "))

if not (0 <= galibiyet <= 7) or uyari < 0:
    print("Geçersiz giriş: kayıtları kontrol edin.")
elif uyari >= 3:
    print("Diskalifiye: disiplin kurulu kararı.")
elif galibiyet >= 6:
    print("Tebrikler! Doğrudan çeyrek finale yükseldiniz.")
elif 4 <= galibiyet <= 5 and averaj > 0:
    print("Play-off turuna kaldınız.")
elif (galibiyet == 4 and averaj <= 0) or (galibiyet == 3 and averaj >= 15):
    print("Tiebreaker maçı oynayacaksınız.")
elif uyari == 0:
    print("Elendiniz, ama Fair Play ödülü için teşekkürler.")
else:
    print("Elendiniz. Gelecek sezon görüşmek üzere.")

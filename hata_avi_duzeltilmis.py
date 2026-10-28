oldurme = int(input("Öldürme: "))
asist = int(input("Asist: "))
olum = int(input("Ölüm: "))
rol = input("Rol (1/2): ")
etki = (oldurme * 2 + asist) // (olum + 1)
print(f"Etki puanı: {etki}")
if etki >= 10 and oldurme >= 1:
    print("MVP adayı!")
else:
    print("Bu maç olmadı, sıradakine odaklan.")
if rol == "2":
    print("Takım oyuncusu rozeti kazandın.")
print("Değerlendirme tamamlandı.")

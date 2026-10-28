odul = int(input("Kazanılan ödül (TL): "))
seri = int(input("Galibiyet serisi: "))

bonus = 125 * (2 ** seri)
havuz = odul + bonus
kesinti = havuz * 8 // 100
havuz = havuz - kesinti

koc = havuz // 9
toplam_pay = havuz - koc

pay = toplam_pay // 5
kasa = toplam_pay % 5

bin = pay // 1000
tl = pay % 1000

print(f"Seri bonusu: {bonus} TL")
print(f"Kesinti sonrası havuz: {havuz} TL")
print(f"Koç payı: {koc} TL")
print(f"Oyuncu başına: {pay} TL", end="")
print(f" ({bin} bin {tl} TL)")
print("Takım kasasına", f"{kasa} TL", sep=": ")

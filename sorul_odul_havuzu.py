odul = int(input("Kazanılan ödül (TL): "))
seri = int(input("Galibiyet serisi: "))

bonus = 125 * (2 ** seri)
havuz = odul + bonus
print(f"Seri bonusu: {bonus} TL")

kesinti = havuz * 8 // 100
havuz -= kesinti
print(f"Kesinti sonrası havuz: {havuz} TL")

koc_payi = havuz // 9
toplam_oyuncu_payi = havuz - koc_payi
print(f"Koç payı: {koc_payi} TL")

oyuncu_payi = toplam_oyuncu_payi // 5
kasa = toplam_oyuncu_payi % 5

bin_kisim = oyuncu_payi // 1000
tl_kisim = oyuncu_payi % 1000

print(f"Oyuncu başına: {oyuncu_payi} TL", end="")
print(f" ({bin_kisim} bin {tl_kisim} TL)")
print("Takım kasasına", f"{kasa} TL", sep=": ")

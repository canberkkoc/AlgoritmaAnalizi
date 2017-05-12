from random import random

# Kümeler ve veriler
kume = [random() for i in range(10)]
veri = [random() for i in range(1000)]

parametre = 0.01  # Bu parametre mean değişim hızını etkiler arttıkça daha hızlı değişiz Min : 0 Max: 1 olmalıdır.

for x in veri:  # O(veri sayisi)
    enyakinK= 0;
    enkucukHata = 9999; # Sonuza gitmesi gerekli normal koşullarda
    for k in enumerate(kume):  # O(mean sayısı)
        hata = abs(x-k[1])
        if hata < enkucukHata:
            enkucukHata = hata
            enyakinK = k[0]
        kume[enyakinK] = kume[enyakinK]*(1-parametre) + x*(parametre)

print (kume)

# Son analiz durumunda -->O(data*means) yani Veri sayısı = K ve Küme Sayısı = J için // O(K.J) \\

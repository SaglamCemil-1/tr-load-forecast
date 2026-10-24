import os
import numpy as np
import csv

from unicodedata import decimal

aim_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "consumption.csv")
with open(aim_path,"r") as file:
    read = csv.reader(file)
    header = next(read)
    for i,rows in enumerate(read):
        pass
    i += 1
    if i%(24*7) != 0:
        i -= i%(24*7)
    day_count = i // 24
    week_count = day_count // 7

matris_365 = np.ones(i)
with open(aim_path, "r") as file:
    read = csv.reader(file)
    header = next(read)
    integer = 0
    for rows in read:
        if integer == i:
            break
        matris_365[integer] = rows[2]
        integer += 1

new_matris_dh = matris_365.reshape((day_count,24))
hourly_avg = np.mean(new_matris_dh,axis=0)
day_avg = np.mean(new_matris_dh,axis=1)
day_avg_f = day_avg.reshape((week_count,7))
weekdays_avg = np.mean(day_avg_f,axis=0)
week_avg = np.mean(day_avg_f,axis=1)

""" MAPE """
matris_365_forecast_real = matris_365[168:]
matris_365_forecast_weeklater = matris_365[:-168]

ape = abs(((matris_365_forecast_real - matris_365_forecast_weeklater) / matris_365_forecast_real) * 100)
mape_hourly = ape.reshape((i-168)//24,24)
mape_hourly_avg = np.mean(mape_hourly,axis =0) #aşşağı doğru toplar
mape_dayly_avg = np.mean(mape_hourly,axis =1)

print("n: Mape hourly ",mape_hourly_avg)
print("n: Mape dayly ",mape_dayly_avg)
print("Mape: ",np.mean(ape))
# <ne yaptığıma dair en ufak fikrim yok> #

   # print("new: ", matris_365_forecast_weeklater)
   # print("new: ", matris_365_forecast_real)
   # axis 1 - (right) """ axis 0 | (down)

print(f"day avg: \n{day_avg_f}")
print(f"hourly_avg: \n{hourly_avg}")
print(f"per days: \n\t\t{weekdays_avg}")
print(f"week_avg: \n{week_avg}")

"""                                 2. Basit tahminler ve MAPE (1–2 blok)
Ne: İki tahmin yap: “yarın = bugün” (matrisi 1 satır kaydır) ve “yarın = geçen haftanın aynı günü” (7 satır kaydır). İkisinin de MAPE değerini döngü kullanmadan hesapla.
Neden: Bu iki tahmin, kuracağın her modelin geçmesi gereken çizgi. Dikkat: İkisini aynı günler üzerinde karşılaştır. Haftalık tahmin ilk 7 gün için yapılamıyor; 
günlük tahmini farklı bir gün kümesinde ölçersen kıyas adil olmaz. Sonuçları bana gönder, kendi hesabımla karşılaştırırım.

                                    3. Resmî Yük Tahmin Planı’nın hatası (1–2 blok)
Ne: Veri çekme script’inde, aynı 294 gün için load-estimation-plan verisini CSV’ye kaydet. Bunu da (gün, 24) matrisine çevir ve gerçek tüketime göre MAPE’sini hesapla.
Neden: Projenin asıl kıyası bu. Sonunda üç sayın olacak: iki basit tahmin ve resmî tahmin. Modelin bu sayılarla değerlendirilecek.

                                    4. GitHub ve README (1 blok)
Ne: README’de şunlar olsun: günlük tüketim eğrisi, haftanın günleri ortalaması (doğru gün etiketleriyle), üç MAPE değeri ve 11. ile 20–21. haftalardaki düşüşlerin nedeni. 
Yüklemeden önce .env dosyasının .gitignore içinde olduğunu kontrol et. Neden: Bu README NumPy node’unun bitiş projesi. Bitince Pandas node’una geçersin."""

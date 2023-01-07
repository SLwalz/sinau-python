# library datetime

import datetime as dt #dt itu variabel, jd mengubah datetime jadi variabel dt

print('masukkan TTL anda')
tanggal = int(input("masukkan tanggal lahir = "))
bulan = int(input('masukkan bulan lahir   = '))
tahun = int(input('masukkan tahun lahir   = '))
print('========================')
hari_ini = dt.date.today()
print(f'hari ini tanggal {hari_ini}')
ttl = dt.date(tahun,bulan,tanggal)
print(f'anda lahir pada tanggal {ttl}')
umur = hari_ini - ttl
umur_final = int(umur.days / 365)
print(f"umur anda {umur_final} tahun")


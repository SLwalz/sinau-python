# print("Hello World")
# print("hello")
# a = "hello"
# b = "world"
# c = 100
# print(a,b,100)
# print(type(a),"\n",type(c))
# d = [1]
# e = 1
# hasil = d[0] is not e
# print(2*hasil,hex(id(d[0])),hex(id(e)))
# print(r'a\nb')

# PENTING PENTING!!!!!
# membuat multiline dengan 3 " (alternatif \n)
# print("""
# apa lu?
# lu gasuka ama gwe?
# sini gelut
# """)

# q='a'
# w='b'
# e='c'
# r=q+w+e+' '
# print(r[0:2])
# print(len(r))
# print(min(r))
# print(max(r),chr(117))
#bisa digunakan untuk memanipulasi string
#ord() dibuat untuk melihat berapa urutan suatu simboldi ASCII
#len() panjang string
#min() simbol dengan urutan ASCII terkecil
#max() simbol dengan urutan ASCII terbesar
#variabel.count(" x ") menghitung banyak karakter 'x' pada sebuah string
#variabel.upper/lower --> upper/lowercase
# isX bisa digunalan untuk melakukan pengecekan cari di gugel macam pengecekan is

# angka = input(':')
# cek = angka.isupper()
# print(str(cek))

# nama = input(':')
# a='sigit rendang'
# status= a not in nama
## in/ not in --> menyeleksi apa ada/ tidak nilai yang diinginkan dalam suatu string yang ada(bernilai T/F)
# print(status)
# jumlah =  nama.count("a")
# print(jumlah)


# #format string
# masukan = 400049
# print(f"{masukan:,}") #untuk memformat ke bilangan ribuan dgn ,
# angka = 12
# print(f"{angka:+d}") #untuk menampilkan tanda +/-, d adalah jenis bilangan bulat,, bisa diganti dgn f(float)
# angka = 5938.232
# print(f"{angka:.2f}") #untuk pembulatan angka di x dibelakang koma. 3f=3 angka diblkg koma, f adalah bilangan float
# print(f"{angka:.2%}") #menampilkan persen, 2 untuk menentukan berapa angka diblkg koma
# #bisa melakukan operasi didalam kurung format

# #konversi bilangan bin,dec,oct,hex
# decimal = 120
# biner = f"{bin(decimal)}"
# oktal = f"{oct(decimal)}"
# hexa = f"{hex(decimal)}"
# print(f"decimal = {decimal}\nbiner = {biner}\noktal = {oktal}\nhexadecimal = {hexa}")

#model if-else dan elif(else if) di python
# if syarat : statement
# elif syarat : statement
# else: statement
#
#     atau
#
# if syarat :
#     statement
# elif syarat:
#     statement
# else:
#     statement


# looping python
# for x in x atau range(): <-- syarat
#     aksi

#     atau

# while syarat:
#     aksi

# range --> range(a,b,c)
# a = awal
# b = sebelum akhir
# c = increment / decrement(pakai -)
# range(1,2,3)

# a = list(range(6,1,-2))
# b = [i for i in range(1,5) if i!=2]
# print(a)
# print(b)

# inputan = int(input('mau berapa kali'))
# for i in range(inputan):
#     print('gwe ganteng')
# while inputan>0:
    
#     inputan-=1
#     print('gwe raja iblis')
   
#     if inputan==3:
#         continue
# print('end')


## MANIPULASI DATA LIST
# data = ['re','ro','ra']
# data_baru = ['ri','ru']
# data.insert(posisi, data yang dimasukkan) <-- untuk memasukkan data baru pada posisi tertentu
# data.expand(data_baru)                    <-- untuk menggabungkan data lama dengan data data_baru
# data.append(data yang dimasukkan)         <-- untuk menambahkan data baru tapi hanya dimasukkan dibagian belakang
# data[2] = 'RA'                            <-- untuk malakukan perubahan data pada index tertentu
# data.remove('re')                           <-- menghapus data yang diinginkan, akan error apabila data yang ingin dihapus tidak ada
# data.pop()                                  <-- menghapus data paling belakang

cek = ['l','e','2']
cek.sort()
cek.reverse()
print(cek)

print('lolo',end=" ")

# DICTIONARY ATAU DICT
 
kerang = {
    'satu' : 'bjr',
    'dua' : 'hehe',
    'tiga' : cek[1],
}
print(kerang['satu'], kerang['tiga'])

# -pengecekan panjang = len(nama dict)
# -pengecekan key ada or not =>
#     key = "satu"
#     checkkey = key in kerang
#     print(f"apa {key} ada ? {checkkey} ") # hasilnya akan true or false
# -akses value dnegan 'get'=>
#      print(kerang.get["dua"]) # akan ditampilkan hasil
#      print(kerang.get("empat")) # akan ditampilkan none   
# -update dict
#       namaDict.update(key:value)
# sama meski ingin menambah data baru atau mengubah data lama
# -delete data pada dict
#      del namaDict[namaKey]
# - LOOPING 
# for variableName in dictName.keys(): untuk print key saja
#        print(variablName)
# for variableName in dictName.values(): untuk print value saja
#       print(variablName)
#       atau
#       print(dictName.get(varibleName on key module(line 157)))
# for variableName in dictName.items(): untuk print bemtuk item saja
#       print(variablName)
# tapi bentuk item (key, value)
# for key,value in dictName.items(): untuk print item saja
# (atau nama variabel lain boleh)
#       print(f"{key} {value}")
# 
#  COPY AND POP
# copy = mengkopi data
# newVariable = dictName.copy()
# pop = mentransfer data dan akan hilang di data awal
# newVariable = dictName.pop("namaVariabel yg ingin ditransfer")
# popitem = mentransfer data akhir
# newVariable = dictName.popitem()

saya = kerang.popitem()
print(kerang)
print(saya)






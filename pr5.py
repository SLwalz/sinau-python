# bikin belah ketupat * dengan looping



# GAGAL LANJUT NANTI
ulang = 1
while ulang==1:
    data = int(input('masukan ukuran belah ketupat: '))
    print('==========================')
    if (data%2)==1:
        ulangi_bintang = 1
        ulangi_spasi = data-1
        # while ulangi_spasi>0:
            
        for i in range(int(data/2)+1):
                print(' '*ulangi_spasi, end='')
                print('*'*ulangi_bintang)
                ulangi_bintang+=2
                ulangi_spasi-=1
        for i in range(int(data/2)):
                a = ulangi_bintang/2
                a = int(a) - 1
                ulangi_spasi+=2
                print(' '*ulangi_spasi, end='')
                print('*'*a)
                
        ulang=0
    else:
        print('harus masukkan angka ganjil')
        print('==========================')
print('==========================')
print('bintang anda sudah diprint')
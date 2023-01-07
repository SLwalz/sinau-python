# bikin kalkulator dari python dgn if sintaks

print(10*'=')
print('KALKULATOR')
print(10*'=')
angka1 = float(input("angka 1: "))
operasi = input('+ - x / : ')
angka2 = float(input('angka2: '))

if operasi=="+":
    print(f'hasil = {angka1+angka2}')
elif operasi=="-":
    print(f'hasil = {angka1-angka2}')
elif operasi=="x" or operasi=="*" or operasi=='X':
    print(f'hasil = {angka1*angka2}')
elif operasi=="/" or operasi==':':
    print(f'hasil = {angka1/angka2}')
print(10*'=')
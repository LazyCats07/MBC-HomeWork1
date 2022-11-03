def tambah(a, b):
    tambah = float(a) + float(b)
    return tambah

def kurang(a, b):
    tambah = float(a) - float(b)
    return kurang
    
def kali(a, b):
    tambah = float(a) * float(b)
    return kali

def bagi(a, b):
    tambah = float(a) / float(b)
    return bagi

while True:
    print('\n\n\t========== KALKULATOR SEDERHANA ==========\n\n')
    a = input('Masukan bilangan 1: ')
    b = input('Masukan bilangan 2: ')
    print('\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n 5. Batal')
    c = input('\npilih 1-5: ')
    if c == '1':
        print('hasilnya adalah: ', tambah(a, b))
    elif c == '2':
        print('hasilnya adalah: ',kurang(a, b))
    elif c == '3':
        print('hasilnya adalah: ',kali(a, b))
    elif c == '4':
        print('hasilnya adalah: ',bagi(a, b))
    elif c == '5':
        break
    else:
        print("operasi tidak dikenal.")






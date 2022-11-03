# Kalkulator Sederhana

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=","\n")

angka1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+,-,x,/) =  ")
angka2 = float(input("Masukkan angka 2 = "))

# Percabangan dan fungsi
def kalkulator():
    if operator == "+":
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} ")
        print(f"hasilnya adalah {hasil}")
    elif operator == "-":
        hasil = angka1 - angka2
        print(f"{angka1} - {angka2} ")
        print(f"Hasilnya adalah {hasil}")
    elif operator == "x":
        hasil = angka1 * angka2
        print(f"{angka1} x {angka2} ")
        print(f"Hasilnya adalah {hasil}")
    elif operator == "/":
        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} ")
        print(f"Hasilnya adalah {hasil}")
    print("\nAkhir dari sekian, Terima Gaji\n")
    
kalkulator()


    



    
    
    










# Note 
# 1. Data User = angka1, angka2, operator
# 2. Cabangnya = operator
# 3. Operator = +, -, *, /
# 4. Hasil & Tampilnya

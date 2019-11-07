# Menentukan Bilangan terbesar
# Masukkan angka 0 untuk berhenti, Untuk mendapatkan bilangan terbesar

print("**********Latihan 2**********")

max = 0 # Menentukan bilangan terbesar
while True :
    a = int(input("Masukkan bilangan = "))
    if max < a:
        max = a
    if a== 0:
       break # Mengakhiri perulangan

print ("Bilangan Terbesar adalah",max)

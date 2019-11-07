# Perulangan latihan1
# Menggunkan For 
print("Latihan 1")
print("Bilangan acak yang lebih kecil dari 0,5")
print("=========================================")


print ("Masukkan nilai N : 5 ")

import random # untuk menghasilkan variable acak berisi string atau data
jumlah = 5
a = 0

for data in range(jumlah):# untuk menampilkan list dengan jarak nilai urut
    i = random.uniform(.0,.5)# untuk menampilkan bil float
    a+=1

    print("Data bilangan acak ke",a,"==>", i) # Batas perulangan
    
print ("\\\\\Selesai/////")


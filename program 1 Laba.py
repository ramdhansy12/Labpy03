# Menghitung  total keuntungan selama 8 bulan berjalan usahanya.
# Menggunakan For dan if

a = 100000000 # awal modal usaha
print("Modal awal usaha",a)
for m in range (1,9):
    if(m>=1 and m<=2):
        b=a*0
        print("Laba bulan ke-",m," :",b)
        
    if(m>=3 and m<=4):
        c=a*0.1
        print("Laba bulan ke-",m," :",c)
    if(m>=5 and m<=7):
       d=a*0.5
       print ("Laba bulan ke-",m," :",d)
    if(m==8):
       e=a*0.2
       print ("Laba bulan ke-",m," :",e)
total = b+b+c+c+d+d+d+e # Total laba dari keseluruhan bulan
print("\nTotal : ", total)
       

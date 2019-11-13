#labpy03
### FlowChart
![FlowChart Latihan 1(Labpy 03)](https://user-images.githubusercontent.com/56957725/68741823-37ea2280-0621-11ea-941c-65817236e8c3.png)


#### Penjelasan Latihan 1

1. Mula -mula  input  nilai N bernilai 5,  dengan pernyataan print("Masukkan nilai N : 5"). **Hasil di layar 1**
2. Kemudian import random, import random ini untuk menghasilkan  variabel acak berisi string atau data yang akan di acak.
3. masukkan  jumlah = 5 dan a=0 nantinya ini untuk memberi data secara acak yang berjumlah 5 , dan *a* ini untuk memberi keterangan nomer pada bilangan float(Pecahan)
4. ketik perintah for data in range(jumlah) ini untuk menampilkan list nilai data dengan jarak nilai urut, maksudnya nanti di bilangan float antara nomer 1 sampai 5 itu berbeda.
5. masukkan i = random.uniform (.0,.5)igunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y. lalu masukkan a+ = 1 untuk memberi nomer pada bilangan float.
6. ketik perintah ("Data bilangan acak ke",a,"==>, i), nanti akan muncul seperti di **layar nomer 2**
7. SELESAI  :clap: . Hasil programnya ada dibawah :point_down:

![image](https://user-images.githubusercontent.com/56957725/68291979-89dcf680-00bd-11ea-94aa-dae22e9cb6ee.png)

------------------------------------------------------------------------------
#### FlowChart

![FLOWCHART BIL TERBESAR](https://user-images.githubusercontent.com/56957725/68741804-27d24300-0621-11ea-895c-7bec9465e8a4.jpg)
#### Penjelasan Latihan 2


1. **Mula mula input max = 0** . fungsi dari max untuk mencari nilai tertinggi. Fungsi ini dapat diberikan sebuah parameter berupa angka.  
2. **Ketik perintah while True**. _While disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya._
3. **pernyataan a = int(input("Masukkan bilangan = "))**. _fungsi dari int  berfungsi untuk  mengkonversi bilangan maupun string angka menjadi bilangan bulat (integer). input itu utuk masukan yang kita berikan ke program._
4. **pernyataan if max < a:**
                                **max = a**
                         **if a== 0:**
                            **break**
     _if itu bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu. Kenapa max = 0 nantinya 0 itu persamaan dari bilangan terbesar, nah if  a== 0 itu harus diakhiri dengan perintah break, break ini untuk memberhentikan perulangan_
5. **Pernyataan print ("Bilangan Terbesar adalah",max)**. _Nantinya ini akan menampilkan bilangan terbesar, dari nilai data yang anda masukkan_.
6. SELESAI :heavy_check_mark: :octocat:
.Hasil Programan ada di bawah :point_down:

![image](https://user-images.githubusercontent.com/56957725/68304546-8b67e800-00d8-11ea-9d41-fb84f6b54522.png)

----------------------------------------------------------------------------------------------------------------------------------------


#### Program 1

Soal :

**Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.**

Penyelesaian menggunakan For, if

1. Mula -mula masukkan modal usahanya yaitu a = 100000000

2. **Gunakan perintah for m in range (1,9):**, _for ini untuk perulangan dari 1 sampai 8, kenapa menggunakan for,karena for ini perulangan yang terhitung. Pada skirp in range(1, 9) akan mebentuk list perulangan yang berisi [1,2,3,4,5,6,7,8] nah dan bahwa iterasi 9 itu tidak termasuk, untuk membuktikan bawa perulangan ini hanya sampai 8 saja_.

3. **Lalu gunakan perintah _if(m>=1 and m<=2): b=a*0**. _if pertama ini untuk menentukan laba bulan ke 1 dan ke 2.masukan variable kalikan nilai (a) dengan data bulan 1 dan 2_. **lalu print("Laba bulan ke-",m," :",b) untuk menampilkan hasil laba**. _pada bulan pertama dan kedua belum mendapatkan laba jadinya 0_.

4. **if(m>=3 and m<=4): c=a*0.1**. _if yang kedua ini untuk menentukkan laba bulan ke 3 dan ke 4.masukan variable kalikan nilai (a) dengan data bulan 3 dan 4. pada bulan ke 3 itu baru mendapatkan laba sebesar 1%  berarti bulan ke 4 juga sama. lalu cetak (m) dan (c), dengan perintah_  **print("Laba bulan ke-",m," :",c)**.

5. **Kemudian if(m>5 and m<=7): d=a*0.5**._if ketiga untuk menentukan laba bulan ke 5 sampai ke 7.masukan variable lalu  kalikan nilai (a) dengan data bulan 5 sampai 7, pada bulan ke 5 laba naik sebesar 5% berarti pada bulan ke 6 dan 7 kenaikan labanya sama, lalu cetak (m) dan (d), dengan perintah_ **print ("Laba bulan ke-",m," :",d)**..

6. **if(m==8): e=a*0.2** if keempat atau yang terakhir  ini untuk menentukan laba bulan ke 8. lalu masukan variabel kalikan nilai (a) dengan data bulan 8. Pada laba bulan ke 8 ini menurun sebanyak 2%, lalu  cetak (m) dan (e) dengan perintah_ **print ("Laba bulan ke-",m," :",e)**.

7. **Kemudian yang terakhir totalkan keseluruhan laba yaitu total = b+b+c+c+d+d+d+e**
8. **lalu print("\nTotal : ", total)**, _untuk menampilkan hasil keseluruhan laba dari bulan pertama sampai bulan kedelapan._
9. SELESAI :+1: :thumbsup: Hasil programan ada di bawah:point_down:
   ![image](https://user-images.githubusercontent.com/56957725/68351955-8ede8c00-0137-11ea-8e40-89fab3ee41b5.png)




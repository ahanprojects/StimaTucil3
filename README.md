# Tugas Kecil 3 IF2211 Strategi Algoritma

7071 Pathfinding

## Deskripsi

7071 Pathfinding merupakan sebuah program pencarian jalur terpendek dari 2 tempat yang ada di map yang mengaplikasikan 2 materi yang berhubungan yaitu **Algoritma A\* (A star)** dan **Graf**.

## Requirement

**1. Python**

Python 3 or later

**2. Install requirements.txt**

1. Jalankan _command prompt_
2. Change directory ke folder `src`
3. Apabila pip belum terinstall, install pip terlebih dahulu
4. Masukkan command `pip install -r requirements.txt` pada directory src di _command prompt_. Contoh: `C:\Users\..\Tucil3Stima\src>pip install -r requirements.txt`

## How To Use

1. Buka _command crompt_
2. Change directory ke folder `src`
3. Jalankan perintah `python main.py'
4. Pada browser anda, buka laman `localhost:5000`
5. Pilih file yang akan divisualisasikan kedalam peta _Google Maps_, pastikan format file input sudah benar
6. Pilih simpul awal
7. Pilih simpul akhir

## Lain-Lain

### 1. Format file input

Format file input terdiri dari 4 bagian, yaitu <br/>

1. Baris pertama merupakan jumlah simpul berupa bilangan bulat
2. Koordinat dan nama simpul sebanyak jumlah simpul, ketiga elemen dipisahkan oleh spasi
3. Matriks ketetanggaan boolean antar simpul (1 apabila bertetangga, 0 apabila tidak)
4. Baris terakhir merupakan baris kosong **(PASTIKAN ADA)**

Contoh format file:


3<br/>
0.433 1.5677 A<br/>
-3.4322 0.9987 B<br/>
2.09 -1.001 C<br/>
0 1 0<br/>
1 0 0<br/>
0 0 0<br/>
<br/>
total line: 8

### 2. Error

* **Tidak menampilkan rute terpendek dan jarak antar 2 simpul**

Kemungkinan hal ini dapat terjadi karena program dibuka di `127.0.0.1:5000`, **PASTIKAN** dibuka pada `localhost:5000`

* **Google maps tidak menampilkan peta**  
Lakukan reload page pada browser beberapa kali.  

* **Clear Cache**

Apabila error masih terjadi setelah memastikan solusi dari error sebelumnya, lakukan _clear cache_ pada browser anda

## Identitas

13519070 - Mhd. Hiro Agayeff Muslion <br/>
13519071 - Farhan Nur Hidayat Denira <br/>

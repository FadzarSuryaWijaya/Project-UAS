# Project-UAS
## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Fadzar Surya Wijaya |
| **NIM** | 312310451 |
| **Kelas** | TI.23.A.5 |
| **Mata Kuliah** | Bahasa Pemrograman |

```python
print("=" * 50 + "\nSelamat Datang Di Kantin Universitas Pelita Bangsa \n" + "=" * 50)

menu = {
    1: {"nama": "Nasi Goreng", "harga": 10000, "stok": 10},
    2: {"nama": "Mie Kwetiaw", "harga": 10000, "stok": 8},
    3: {"nama": "Batagor", "harga": 10000, "stok": 5},
    4: {"nama": "Seblak", "harga": 13000, "stok": 7},
    5: {"nama": "Gorengan", "harga": 1000, "stok": 20},
}

keranjang = {menu[item]["nama"]: [0, 0] for item in menu}
tagihan = 0

while True:
    print("Menu")
    print("1. Pembelian")
    print("2. Struk")
    print("3. Keluar")
    pil = int(input("Masukkan pilihan: "))

    if pil == 1:
        for key, value in menu.items():
            print(f"{key}. {value['nama']} Harga: {value['harga']} Stok: {value['stok']}")

        pilihan = int(input("Masukkan nomor menu yang ingin dibeli: "))
        if pilihan in menu:
            if menu[pilihan]['stok'] > 0:   #jika stock lebih dari 0 maka
                jumlah = int(input(f"Masukkan jumlah {menu[pilihan]['nama']}: "))  #variable jumlah akan memanggil input baru
                if menu[pilihan]['stok'] >= jumlah:  #jika stock kurang dari jumlah yg otomatis mengacu pada jumlah nasi goreng
                    menu[pilihan]['stok'] -= jumlah  # jika iya maka jumlah tersebut akan dikurangi dari stock sebelumnya
                    tambah = keranjang[menu[pilihan]['nama']]
                    tambah[0] += jumlah
                    tambah[1] += menu[pilihan]['harga'] * jumlah
                    print(f"{jumlah} {menu[pilihan]['nama']}, Rp. {menu[pilihan]['harga'] * jumlah}")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Stok habis.")
        else:
            print("Nomor menu tidak valid.")

    elif pil == 2:
        print("=" * 20 + "\nBarang yang dibeli\n" + "=" * 20)
        for key, value in keranjang.items():
            if value[0] != 0:
                print(f"{value[0]} {key}, Rp. {value[1]}")
                tagihan += value[1]
        print(f"Total Tagihan : Rp. {tagihan}")

    elif pil == 3:
        print("Program dihentikan")
        break

    else:
        print("Pilihan tidak ada di menu. Silakan masukkan ulang.")
```

```python
print(".: Selamat Datang Di Toko :.\n")
```
* Mari kita mulai dari baris pertama. Kode ini hanya mencetak pesan selamat datang di toko. Pemformatan teks ini menambahkan sentuhan menyambut untuk pengguna yang menjalankan program.

```python
menu = {
    1: {"nama": "Nasi Goreng", "harga": 10000, "stok": 10},
    2: {"nama": "Mie Kwetiaw", "harga": 10000, "stok": 8},
    3: {"nama": "Batagor", "harga": 10000, "stok": 5},
    4: {"nama": "Seblak", "harga": 13000, "stok": 7},
    5: {"nama": "Gorengan", "harga": 1000, "stok": 20},
}
```
* Baris selanjutnya, kita mendefinisikan variabel `menu` sebagai kamus (dictionary) yang berisi informasi tentang beberapa item makanan. Setiap item memiliki nomor, nama, harga, dan stok. Ini mirip dengan daftar menu di toko makanan.

```python
keranjang = {menu[item]["nama"]: [0, 0] for item in menu}
```
* Berikutnya, kita membuat kamus `keranjang` yang awalnya kosong. Setiap item dalam `keranjang` akan memiliki nama item sebagai kunci dan nilai awal berupa jumlah dan total harga yang sama dengan 0.

```python
tagihan = 0
```
* Langkah selanjutnya, kita inisialisasi variabel `tagihan` sebagai 0. Variabel ini akan digunakan untuk menyimpan total tagihan pembelian.

```python
while True:
    print("Menu")
    print("1. Pembelian")
    print("2. Struk")
    print("3. Keluar")
    pil = int(input("Masukkan pilihan: "))
```
* Program selanjutnya memasuki loop tak terbatas (`while True`) untuk menampilkan menu kepada pengguna. Pengguna diminta memilih opsi dengan memasukkan angka.

```python
    if pil == 1:
        for key, value in menu.items():
            print(f"{key}. {value['nama']} Harga: {value['harga']} Stok: {value['stok']}")
```
* Jika pengguna memilih opsi 1 (Pembelian), program akan menampilkan menu makanan beserta harga dan stoknya. Ini memungkinkan pengguna untuk melihat item-item yang tersedia.

```python
        pilihan = int(input("Masukkan nomor menu yang ingin dibeli: "))
        if pilihan in menu:
            if menu[pilihan]['stok'] > 0:
                jumlah = int(input(f"Masukkan jumlah {menu[pilihan]['nama']}: "))
                if menu[pilihan]['stok'] >= jumlah:
                    menu[pilihan]['stok'] -= jumlah
                    tambah = keranjang[menu[pilihan]['nama']]
                    tambah[0] += jumlah
                    tambah[1] += menu[pilihan]['harga'] * jumlah
                    print(f"{jumlah} {menu[pilihan]['nama']}, Rp. {menu[pilihan]['harga'] * jumlah}")
                else:
                    print("Stok tidak mencukupi.")
            else:
                print("Stok habis.")
        else:
            print("Nomor menu tidak valid.")
```
* Setelah menampilkan menu, program meminta pengguna untuk memasukkan nomor menu yang ingin dibeli. Kemudian, program memeriksa apakah nomor menu tersebut valid dan apakah stoknya mencukupi untuk pembelian. Jika ya, maka program akan mengurangi stok dari menu, mencatat pembelian dalam `keranjang`, dan mencetak konfirmasi pembelian.
* `pilihan = int(input("Masukkan nomor menu yang ingin dibeli: "))`: Pengguna diminta untuk memasukkan nomor menu yang ingin dibeli. Nomor ini kemudian disimpan dalam variabel `pilihan`.
* `if pilihan in menu:`: Kondisi ini memeriksa apakah nomor menu yang dimasukkan pengguna ada dalam daftar menu (`menu`). Jika ya, maka program melanjutkan untuk memproses pembelian.
* `if menu[pilihan]['stok'] > 0:`: Kondisi ini memeriksa apakah stok dari item makanan yang dipilih tersedia (lebih dari 0). Jika stok tersedia, pengguna diminta untuk memasukkan jumlah item yang ingin dibeli.
* `jumlah = int(input(f"Masukkan jumlah {menu[pilihan]['nama']}: "))`: Pengguna diminta untuk memasukkan jumlah item makanan yang ingin dibeli. Jumlah ini kemudian disimpan dalam variabel `jumlah`.
* `if menu[pilihan]['stok'] >= jumlah:`: Kondisi ini memeriksa apakah stok yang tersedia cukup untuk memenuhi jumlah yang diminta oleh pengguna. Jika ya, maka pembelian dapat dilakukan.
* `menu[pilihan]['stok'] -= jumlah`: Jika kondisi terpenuhi, stok item makanan yang dipilih dikurangi sebanyak jumlah yang dibeli.
* `tambah = keranjang[menu[pilihan]['nama']]`: Variabel `tambah` diinisialisasi dengan mendapatkan nilai dari keranjang untuk item makanan yang dipilih, menggunakan nama item makanan sebagai kunci.
* `tambah[0] += jumlah`: Jumlah item makanan dalam keranjang (indeks 0) ditambah dengan jumlah yang dibeli.
* `tambah[1] += menu[pilihan]['harga'] * jumlah`: Total harga dalam keranjang (indeks 1) ditambah dengan harga per item makanan dikali dengan jumlah yang dibeli.
* `print(f"{jumlah} {menu[pilihan]['nama']}, Rp. {menu[pilihan]['harga'] * jumlah}")`: Program mencetak konfirmasi pembelian, mencantumkan jumlah dan nama item makanan yang dibeli, serta total harga untuk item tersebut.


```python
    elif pil == 2:
        print("=" * 20 + "\nBarang yang dibeli\n" + "=" * 20)
        for key, value in keranjang.items():
            if value[0] != 0:
                print(f"{value[0]} {key}, Rp. {value[1]}")
                tagihan += value[1]
        print(f"Total Tagihan : Rp. {tagihan}")
```

* Jika pengguna memilih opsi 2 (Struk), program akan mencetak struk pembelian. Ini termasuk barang yang dibeli beserta total tagihannya.
Tentu, mari kita bahas bagian ini dari program:
* `elif pil == 2:`: Ini adalah bagian dari blok kondisional yang menangani opsi kedua, yaitu ketika pengguna memilih untuk melihat struk pembelian.
* `print("=" * 20 + "\nBarang yang dibeli\n" + "=" * 20)`: Kode ini mencetak garis pemisah yang terdiri dari 20 karakter "=" untuk membentuk tampilan visual sebagai pemisah antara judul "Barang yang dibeli" dan item-item dalam struk.
* `for key, value in keranjang.items():`: Ini adalah loop yang digunakan untuk mengiterasi melalui setiap item dalam kamus `keranjang`. Kamus ini berisi item-item yang telah dibeli berserta informasi jumlah dan total harga.
* `if value[0] != 0:`: Kondisi ini memeriksa apakah jumlah item yang dibeli (indeks 0 dalam nilai `value`) tidak sama dengan 0. Ini bertujuan untuk memastikan bahwa hanya item yang benar-benar dibeli yang akan dicetak dalam struk.
* `print(f"{value[0]} {key}, Rp. {value[1]}")`: Baris ini mencetak informasi tentang item yang dibeli. `{value[0]}` menunjukkan jumlah item yang dibeli, `{key}` adalah nama item, dan `{value[1]}` adalah total harga untuk item tersebut. Ini memberikan tampilan struk yang terperinci.
* `tagihan += value[1]`: Ini menambahkan total harga dari setiap item yang dibeli ke dalam variabel `tagihan`. Hal ini membantu dalam menghitung total tagihan dari seluruh pembelian.
* `print(f"Total Tagihan : Rp. {tagihan}")`: Baris terakhir mencetak total tagihan keseluruhan setelah menampilkan detail setiap item yang dibeli.

```python
    elif pil == 3:
        print("Program dihentikan")
        break
```
* Jika pengguna memilih opsi 3 (Keluar), program akan memberikan pesan bahwa program dihentikan dan keluar dari loop tak terbatas.


```python
    else:
        print("Pilihan tidak ada di menu. Silakan masukkan ulang.")
```
* Jika pengguna memasukkan pilihan yang tidak valid, program memberikan pesan bahwa pilihan tidak ada di menu dan meminta pengguna untuk memasukkan ulang.

## Gambar Output
<p align="center">
* <img src="gambar/1.png">
</p>

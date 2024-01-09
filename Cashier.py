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



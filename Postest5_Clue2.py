#Program Menu Cafe dengan Menggunakan CRUD
def intro():
    print ("=======================================")
    print ("          Program Cafe ABC123          ")
    print ("=======================================")
    print ("          Silahkan Pilih Menu          ")
    print ("=======================================")
intro ()

menu_makanan = {
    "1" : "Kentang Goreng   : Rp. 20000",
    "2" : "Pisang Keju      : Rp. 15000",
    "3" : "Roti Bakar       : Rp. 15000", 
    "4" : "Batagor          : Rp. 20000",
    "5" : "Jasuke           : Rp. 10000",
    "6" : "Siomay           : Rp. 15000",
    "7" : "Cuanki           : Rp. 10000",
    "8" : "Cireng           : Rp. 10000"
}

menu_minuman = {
    "1" : "Hazzelnut Chocolate  : Rp. 10000",
    "2" : "Caramel Latte        : Rp. 15000",
    "3" : "Air Mineral          : Rp. 5000",
    "4" : "Cappucino            : Rp. 15000",
    "5" : "Es Jeruk             : Rp. 8000",
    "6" : "Es Teh               : Rp. 8000",
    "7" : "Sprite               : Rp. 5000",
    "8" : "Milo                 : Rp. 8000"
}

def pilihan_menu():
    print("[1] Menampilkan Menu")
    print("[2] Menambahkan Menu")
    print("[3] Mengedit Menu")
    print("[4] Menghapus Menu")
    print("[5] Menghitung Jumlah Menu")
    print("[6] Keluar")

def menu ():
    print ("[A] Menu Makanan")
    print ("[B] Menu Minuman")
    print ("\nMasukkan Menggunakan Huruf Kapital !")

def tampil_menu_makanan():
    for key, val in menu_makanan.items():
        print("%s" % (val))
    print ("=======================================")

def tampil_menu_minuman():
    for key, val in menu_minuman.items():
        print("%s" % (val))
    print ("=======================================")

def tambah_menu_makanan():
    print("[A] Tengah")
    print("[B] Belakang")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    letak = input("Letakkan Tambahan Menu di [A/B] : ")
    print ("=======================================")
    if letak == "A":
        print ("Masukkan Nomor yang akan ditempati oleh Menu Baru")
        kata_kunci = input("Letakkan Menu Baru pada urutan : ")
        print ("=======================================")
        print ("Masukkan Nama Menu yang ingin ditambahkan beserta harganya")
        print ("Bakso            : Rp. 15000 ============ Contoh")
        tambah_menu_makanan = input("")
        print ("=======================================")
        menu_makanan.update({kata_kunci : tambah_menu_makanan})
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("=======================================")
    elif letak == "B":
        print("Masukkan Angkanya saja !")
        jumlah_menu = int(input("Masukkan Jumlah Menu yang Ada : "))
        print ("=======================================")
        kata_kunci = jumlah_menu + 1
        print ("Masukkan Nama Menu yang ingin ditambahkan beserta harganya")
        print ("Bakso            : Rp. 15000 ============ Contoh")
        tambah_harga_makanan = input("")
        print ("=======================================")
        menu_makanan.update({kata_kunci : tambah_harga_makanan})
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("=======================================")
    else:
        print ("Maaf Pilihan yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

def tambah_menu_minuman():
    print("[A] Tengah")
    print("[B] Belakang")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    letak = input("Letakkan Tambahan Menu di [A/B] : ")
    print ("=======================================")
    if letak == "A":
        print ("Masukkan Nomor yang akan ditempati oleh Menu Baru")
        kata_kunci = input("Letakkan Menu Baru pada urutan : ")
        print ("=======================================")
        print ("Masukkan Nama Menu yang ingin ditambahkan beserta harganya")
        print ("Coca Cola            : Rp. 5000 ============ Contoh")
        tambah_menu_minuman = input("")
        print ("=======================================")
        menu_minuman.update({kata_kunci : tambah_menu_minuman})
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("=======================================")
    elif letak == "B":
        print("Masukkan Angkanya saja !")
        jumlah_menu = int(input("Masukkan Jumlah Menu yang Ada : "))
        kata_kunci = jumlah_menu + 1
        print ("=======================================")
        print ("Masukkan Nama Menu yang ingin ditambahkan beserta harganya")
        print ("Coca Cola            : Rp. 5000 ============ Contoh")
        tambah_menu_minuman = input("")
        print ("=======================================")
        menu_minuman.update({kata_kunci : tambah_menu_minuman})
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("=======================================")
    else:
        print ("Maaf Pilihan yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

def edit_menu_makanan():
    print("[A] Mengubah Harga Menu saja")
    print("[B] Mengubah Nama Menu beserta Harganya")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    edit = input("Masukkan Menu Edit yang dipilih [A/B] : ")
    print ("=======================================")
    if edit == "A":
        print("Masukkan Nomor Menu yang ingin diubah harganya")
        kata_kunci = input("")
        print ("=======================================")
        print("Masukkan Nama Menu serta harga pembaruannya")
        print("Bakso            : Rp. 15000 ============ Contoh")
        nama_menu = input("")
        print ("=======================================")
        menu_makanan[kata_kunci] = nama_menu
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("=======================================")
    elif edit == "B":
        print("Masukkan Nomor Menu yang ingin diubah seluruhnya")
        kata_kunci = input("")
        print ("=======================================")
        print("Masukkan Nama Menu Pembaruan beserta harga terbarunya")
        print("Bakso            : Rp. 15000 ============ Contoh")
        nama_menu = input("")
        print ("=======================================")
        menu_makanan[kata_kunci] = nama_menu
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("=======================================")
    else :
        print ("Maaf Metode yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

def edit_menu_minuman():
    print("[A] Mengubah Harga Menu saja")
    print("[B] Mengubah Nama Menu beserta Harganya")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    edit = input("Masukkan Menu Edit yang dipilih [A/B] : ")
    print ("=======================================")
    if edit == "A":
        print("Masukkan Nomor Menu yang ingin diubah harganya")
        kata_kunci = input("")
        print ("=======================================")
        print("Masukkan Nama Menu serta harga pembaruannya")
        print("Coca Cola            : Rp. 5000 ============ Contoh")
        nama_menu = input("")
        print ("=======================================")
        menu_minuman[kata_kunci] = nama_menu
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("=======================================")
    elif edit == "B":
        print("Masukkan Nomor Menu yang ingin diubah seluruhnya")
        kata_kunci = input("")
        print ("=======================================")
        print("Masukkan Nama Menu Pembaruan beserta harganya")
        print("Coca Cola            : Rp. 5000 ============ Contoh")
        nama_menu = input("")
        print ("=======================================")
        menu_minuman[kata_kunci] = nama_menu
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("=======================================")
    else :
        print ("Maaf Metode yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

def hapus_menu_makanan():
    print("[A] Satu-satu")
    print("[B] Keseluruhan")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    hapus = input("Ingin Menghapus Menggunakan Metode [A/B] : ")
    print ("=======================================")
    if hapus == "A":
        print("Masukkan Nomor Menu yang ingin dihapus")
        kata_kunci = input("")
        print ("=======================================")
        del menu_makanan [kata_kunci]
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("=======================================")
    elif hapus == "B":
        menu_makanan.clear()
        for key, val in menu_makanan.items():
            print("%s" % (val))
        print ("Sukses... Seluruh Menu Berhasil Terhapus")
        print ("=======================================")
    else:
        print ("Maaf Metode yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

def hapus_menu_minuman():
    print("[A] Satu-satu")
    print("[B] Keseluruhan")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    hapus = input("Ingin Menghapus Menggunakan Metode [A/B] : ")
    print ("=======================================")
    if hapus == "A":
        print("Masukkan Nomor Menu yang ingin dihapus")
        kata_kunci = input("")
        print ("=======================================")
        del menu_minuman [kata_kunci]
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("=======================================")
    elif hapus == "B":
        menu_minuman.clear()
        for key, val in menu_minuman.items():
            print("%s" % (val))
        print ("Sukses... Seluruh Menu Berhasil Terhapus")
        print ("=======================================")
    else:
        print ("Maaf Metode yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")

jawab = "y"
while jawab == "y":
    pilihan_menu()
    pilih = int(input("Masukkan Pilihan Menu [1, 2, 3, 4, 5, atau 6] : "))
    print ("=======================================")
    if pilih == 1:
        print ("Silahkan Pilih Menu yang ingin ditampilkan")
        menu()
        pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
        print ("=======================================")
        if pilihan == "A":
            tampil_menu_makanan()
        elif pilihan == "B":
            tampil_menu_minuman()
        else:
            print ("Maaf Pilihan Menu yang Anda Masukkan Tidak Tersedia")
            print ("=======================================")
    elif pilih == 2:
        print ("Silahkan Pilih Menu yang ingin ditambahkan")
        menu()
        pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
        print ("=======================================")
        if pilihan == "A":
            tampil_menu_makanan()
            print("Silahkan Pilih Letak untuk Menu Tambahan")
            tambah_menu_makanan()
        elif pilihan == "B":
            tampil_menu_minuman()
            print("Silahkan Pilih Letak Menu Tambahan")
            tambah_menu_minuman()
        else:
            print ("Maaf Pilihan Menu yang Anda Masukkan Tidak Tersedia")
            print ("=======================================")
    elif pilih == 3:
        print ("Silahkan Pilih Menu yang ingin diubah")
        menu()
        pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
        print ("=======================================")
        if pilihan == "A":
            tampil_menu_makanan()
            print("Silahkan Pilih Menu Edit yang diinginkan")
            edit_menu_makanan()
        elif pilihan == "B":
            tampil_menu_minuman()
            print("Silahkan Pilih Menu Edit yang diinginkan")
            edit_menu_minuman()
        else:
            print ("Maaf Pilihan Menu yang Anda Masukkan Tidak Tersedia")
            print ("=======================================")  
    elif pilih == 4:
        print ("Silahkan Pilih Menu yang ingin dihapus")
        menu()
        pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
        print ("=======================================")
        if pilihan == "A":
            tampil_menu_makanan()
            print("Silahkan Pilih Metode Penghapusan")
            hapus_menu_makanan()
        elif pilihan == "B":
            tampil_menu_minuman()
            print("Silahkan Pilih Metode Penghapusan")
            hapus_menu_minuman()
        else:
            print ("Maaf Pilihan yang Anda Masukkan Tidak Tersedia")
            print ("=======================================")
    elif pilih == 5:
        print ("Silahkan Pilih Menu yang ingin dihitung")
        menu()
        pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
        print ("=======================================")
        if pilihan == "A":
            tampil_menu_makanan()
            print ("Jumlah Menu Makanan yang tersedia sebanyak %d" % len(menu_makanan),"menu")
            print ("=======================================")
        elif pilihan == "B":
            tampil_menu_minuman()
            print ("Jumlah Menu Minuman yang tersedia sebanyak %d" % len(menu_makanan),"menu")
            print ("=======================================")
        else :
            print ("Maaf Pilihan yang Anda Masukkan Tidak Tersedia")
            print ("=======================================")
    elif pilih == 6:
        exit()
    else :
        print ("Maaf Pilihan yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")
    jawab = input("Apakah Anda Ingin Melihat Menu Kembali [y/t] ? ")
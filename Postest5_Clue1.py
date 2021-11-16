#Program Menu Cafe Sederhana
def intro():
    print ("=======================================")
    print ("          Program Cafe ABC123          ")
    print ("=======================================")
    print ("          Silahkan Pilih Menu          ")
    print ("=======================================")
intro ()

nama_menu_makanan = {
    "Kentang Goreng   :"  : "Rp. 20000",
    "Pisang Keju      :"  : "Rp. 15000",
    "Roti Bakar       :"  : "Rp. 15000", 
    "Batagor          :"  : "Rp. 20000",
    "Jasuke           :"  : "Rp. 10000",
    "Siomay           :"  : "Rp. 15000",
    "Cuanki           :"  : "Rp. 10000",
    "Cireng           :"  : "Rp. 10000"
}

nama_menu_minuman = {
    "Hazzelnut Chocolate  :" : "Rp. 10000",
    "Caramel Latte        :" : "Rp. 15000",
    "Air Mineral          :" : "Rp. 5000",
    "Cappucino            :" : "Rp. 15000",
    "Es Jeruk             :" : "Rp. 8000",
    "Es Teh               :" : "Rp. 8000",
    "Sprite               :" : "Rp. 5000",
    "Milo                 :" : "Rp. 8000"
}

def menu_makanan():
    for key, val in nama_menu_makanan.items():
        print("%s  %s" % (key, val))
    print ("=======================================")

def menu_minuman():
    for key, val in nama_menu_minuman.items():
        print("%s  %s" % (key,val))
    print ("=======================================")

jawab = "y"
while jawab == "y":
    print ("A. Menu Makanan")
    print ("B. Menu Minuman")
    print ("\nMasukkan Menggunakan Huruf Kapital !")
    pilihan = str(input("Masukkan Pilihan Menu [A/B] : "))
    print ("=======================================")
    if pilihan == "A":
        menu_makanan()
    elif pilihan == "B":
        menu_minuman()
    else :
        print ("Maaf Pilihan Menu yang Anda Masukkan Tidak Tersedia")
        print ("=======================================")
    jawab = input("Apakah Anda Ingin Melihat Menu Kembali [y/t] ? ")
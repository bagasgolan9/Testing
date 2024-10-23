
import os 

def hutanterlarang():
    print("Di dalam hutan terlarang kamu menemukan pohon besar")
    pohon = int(input("Masukan pilihan anda(1 atau 2) : "))
    if pohon == 1:
        print("Dekati pohon besar yang ada ditengah hutan")
        print("Saat mendekati pohon kamu akan bertemu dengan binatang buas dan kamu harus melawannya")
        binatangbuas=int(input("Masukan pilihan anda: "))
        if binatangbuas == 1:
            print("Kamu bertemu dengan hewan yang bisa berbicara dengan kamu")
        elif binatangbuas == 2:
            print("Kamu langsung keluar hutan tanpa menghiraukan binatang itu")

    elif pohon == 2:
        print("Jauhi pohon besar itu dan segera pergi")
    else:
        print("Input salah")

def lawanmonster():
    print("Kamu bertemu dengan monster berkepala 3, kepala 1 mengeluarkan api, kepala 2 mengeluarkan gas, kepala 3 mengeluarkan minyak")
    print("Kamu bertemu dengan monster berkepala 3, kepala 1 mengeluarkan api, kepala 2 mengeluarkan gas, kepala 3 mengeluarkan minyak")
    binatang3kepala=int(input("Masukan pilihan anda(1-3) : "))
    if binatang3kepala == 1:
        print("Kamu memenangkap permainan dan permainan selesai")
    elif binatang3kepala == 2:
        print("Binatang itu hanya luka dan kamu belum bisa mengalahkan binatang itu")
    elif binatang3kepala == 3:
        print("Game over")
    else:
        print("Input salah")
    

def desamagis():
    print("Kamu menjelajahi desa magis dan bertemu beberapa penduduk desa ayo berbicara dengan mereka")
    print("Kamu akan menjelajahi desa magis dan kamu harus bicara dengan mereka")
    orangdidesa=int(input("Masukan pilihan anda(1-5) : "))
    if orangdidesa == 1:
        print("Kamu bertemu dengan pak kades dan membicarakan tentang keadaan didesa")
    elif orangdidesa ==2:
        print("Kamu bertemu dengan pak samsul dan dia mengajari kamu melakukan sihir")
    elif orangdidesa ==3:
        print("Kamu bertemu dengan pak ronal yang jual ramuan sihir")
    elif orangdidesa ==4:
        print("Kamu bertemu bu dea yang sedang membutuhkan pertolongan")
    elif orangdidesa ==5:
        print("Kamu bertemu bu cia dan dia memberikan mu hadiah")
    else:
        print("Input salah")

def menu():
    while True:
        os.system('cls')
        print("Petualangan di Dunia Python")
        print("1. jelajahi hutan terlarang")
        print("2. bertarung melawan monster")
        print("3. Pergi ke desa magis")
        print("4. keluar dari petualangan")

        menu_utama = int(input("Masukkan pilihan anda(1-4) :"))
        
        if menu_utama == 1:
            hutanterlarang()
            
        elif menu_utama == 2:
            lawanmonster()
            
        elif menu_utama == 3: 
            desamagis()

        elif menu_utama == 4:
            break
        else:
            print("Input Salah")
        os.system('pause')
menu()

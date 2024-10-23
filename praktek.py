

# hujan = True

# if hujan:
#     print("Bani tidak berangkat ke kampus")
# else:
#     print("Bani berangkat ke kampus")
    
# huruf = 'kjdbfhja'
# angka = 1827812781

# def check_type(text):
#     if isinstance(text, int):
#         print(True)
#     else:
#         print(False)
    
    
# # check_type(angka)
# # check_type(huruf)

# # datang = 15.00

# # if datang > (14.40 + 0.15):
# #     print("Mahasiswa tidak boleh masuk")
# # else:
# #     print("Mahasiswa boleh masuk")

# nasi_goreng = False
# jenis_nasi_goreng = "Pedas" # Pedes, Sedang, dan Gurih
# mie_ayam = True
# nasi_padang = True

# if nasi_goreng:
#     if jenis_nasi_goreng == "Pedes":
#         print("Memesan nasi goreng pedas cabe 10")
#     elif jenis_nasi_goreng == "Sedang":
#         print("Memesan nasi goreng sedang")
#     else:
#         print("KAMU CUPU PESAN TIDAK PEDAS")
# elif mie_ayam:
#     print("Beli Mie Ayam")
# elif nasi_padang:
#     print("Beli Nasi Padang")
# else:
#     print("PULANG")
    
# username = "Jati"
# password = 1234

# username_input = str(input('Masukkan Username: '))
# password_input = str(input("Masukkan Password: "))

# if username_input == username:
#     if password_input == str(password):
#         print("LOGIN")
#     else:
#         print("Password Salah")
# else:
#     print("Username Salah")


# for angka in range(1, 5, 2):
#     print(angka) # 1, 3
    


# def count_while_loop(number):
#     while True:
#         if number > 5:
#             print(number)
#             number -= 10
#         else:
#             print(number*10)
#             return False
            
# count_while_loop(100)

import os

# 1. Deposito Uang
# 2. Withdraw Uang
# 3. Transfer

def deposito():
    print("Deposito Uang")
    

def menu():
    while True:
        os.system('cls')
        print("MASUKKAN ANGKA YANG ANDA PILIH")
        print("0. Keluar")
        print("1. Deposito Uang")
        print("2. Withdraw Uang")
        print("3. Transfer")
        
        menu_utama = int(input("Masukkan pilihan anda: ")) # 1, 2, 3
        
        if menu_utama == 1:
            deposito()
        elif menu_utama == 2:
            print("Withdraw Uang")
        elif menu_utama == 3: 
            os.system('cls')
            print('1. Transfer ke teman')
            print('2. Transfer ke bank lain')
            
            sub_menu_transfer = int(input("Masukkan pilihan anda: "))
            
        elif menu_utama == 0:
            break
        else:
            print("Input Salah")
        os.system('pause')
        
menu()

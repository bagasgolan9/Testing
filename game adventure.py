print("Selamat datang di petualangan hutan terlarang")
print("Lawan semua monster agar kamu bisa selamat")

import os


def menu_opening():
    while True:
        
        print("Apakah kamu siap untuk melawan semua monster?")
        print("Ya")
        print("Tidak")

menu_utama1=input(": ")
if menu_utama1 == "Ya":
    print("Siap-siap lah untuk melawan moster dan pergi ke desa magis")
else:
    print("Pengecut luu")
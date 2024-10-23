print("1. kali")
print("2. bagi")
print("3. jumlah")
print("4. kurang")
print("5. pangkat")
print("6. divisi")
print("7. modulus")
pilih=int(input("pilih operator aritmatika(1-7) : "))

if pilih >= 7:
    print("input salah")
    exit(1)

angka1=int(input("input number : "))
angka2=int(input("input number : "))

if pilih==1:
    print(angka1*angka2)
elif pilih==2:
    print(angka1/angka2)
elif pilih==3:
    print(angka1+angka2)
elif pilih==4:
    print(angka1-angka2)
elif pilih==5:
    print(angka1**angka2)
elif pilih==6:
    print(angka1//angka2)
elif pilih==7:
    print(angka1%angka2)

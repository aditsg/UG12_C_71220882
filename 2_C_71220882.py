angka = input("masukan angka : " )
hitung = input("masukan angka yang dihitung : ")

sum = 0
for each in angka:
    if each == hitung:
        sum = sum + 1
    
print ("angka",hitung,"muncul sebanyak",sum,"kali")

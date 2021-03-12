#Kalkulator Luas Persegi Panjang
print("*******Kalkulator Efa*******")
print("Menghitung Luas Persegi Panjang")
print("--------INPUT DATA--------")
Panjang = input("Panjang(m) : ")
Lebar = input("Lebar(m): ")
Luas_Persegi_panjang = float(Panjang)*float(Lebar)
print("----------HASIL----------")
print("Luas persegi panjang adalah", Luas_Persegi_panjang, 'm2', '\n')

#Kalkulator Luas Lingkaran
print("--------------------------")
print("Menghitung Luas Lingkaran")
print("--------INPUT DATA--------")
Jari_jari_Lingkaran = input("Panjang Jari jari(m): ")
phi = 22/7
Luas_Lingkaran = phi*(float(Jari_jari_Lingkaran)**2)
print("----------HASIL----------")
print("Luas lingkaran adalah", Luas_Lingkaran, "m2", '\n')

#Kalkulator Luas Permukaan Kubus
print("--------------------------")
print("Menghitung Luas Permukaan Kubus")
print("--------INPUT DATA--------")
Panjang_sisi = input("Panjang sisi kubus(m): ")
Luas_Kubus = 6*(float(Panjang_sisi)**2)
print("----------HASIL----------")
print("Luas permukaan kubus adalah", Luas_Kubus, 'm2', '\n')

#Konversi Suhu Celcius ke Fahrenheit
print("--------------------------")
print("Menghitung suhu celcius ke fahrenheit")
print("--------INPUT DATA--------")
Suhu_Celcius = input("Suhu dalam celcius: ")
Rumus_CkeF = ((9/5 * float(Suhu_Celcius)) + 32)
print("----------HASIL----------")
print("Suhunya adalah", Rumus_CkeF, "Fahrenheit", '\n')

#Konversi Suhu Reamur ke Kelvin
print("--------------------------")
print("Menghitung suhu reamur ke kelvin")
print("--------INPUT DATA--------")
Suhu_Reamur = input("Suhu dalam reamur: ")
Rumus_RkeK = ((5/4 * float(Suhu_Reamur)) + 273)
print("----------HASIL----------")
print("Suhunya adalah", Rumus_RkeK, "Kelvin")

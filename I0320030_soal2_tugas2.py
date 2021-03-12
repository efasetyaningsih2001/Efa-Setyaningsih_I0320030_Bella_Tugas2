#Biodata Pribadi
print("-----------BIODATA------------")
Nama = "Nama = Efa Setyaningsih"
NIM = "NIM = I0320030"
Prodi = "Prodi = Teknik Industri UNS"
Deskripsi_Diri = "Saya merupakan anak kedua dari tiga bersaudara. Biasanya saya dipanggil Efa oleh keluarga dan teman teman saya. Saya merupakan mahasiswa semester 2 Prodi Teknik Industri UNS.Saya orangnya cerewet dan suka panik. Makanan kesukaan saya adalah nasi goreng dan sate ayam. Minuman kesukaan saya adalah es teh dan es jeruk. Saya memiliki hobi menonton film dan drama korea. Genre film yang saya sukai adalah action,thriller,dan fantasy."
print('\n',Nama,'\n',NIM,'\n',Prodi,'\n',Deskripsi_Diri,'\n')

#Alamat Rumah
Dusun = "Ringinsari"
RT = '03'
RW = '02'
Desa = "Randusari"
Kecamatan = "Teras"
Kabupaten = "Boyolali"
print("Alamat rumah saya adalah",Dusun, 'RT',RT,'/RW',RW, str(Desa)+',', str(Kecamatan)+',', str(Kabupaten)+'.')
#Tinggi Badan
Tinggi = int((2*150)-(116.4+32))
print("Tinggi badan saya adalah",str(Tinggi)+ 'cm' )

#Berat Badan
Berat = float(2*(37.28 + 38.8)/4)
print("Berat badan saya adalah", str(Berat)+ 'kg')

#Ukuran Sepatu
Ukuran = float((151*0.13)+ 1.5)
print("Ukuran sepatu saya adalah", Ukuran,'cm')

#Tanggal Lahir
TanggalLahir = 29
BulanLahir = 9
TahunLahir = 2001
TanggalSekarang = 12
BulanSekarang = 3
TahunSekarang =2021

Umurdalamhari = (TanggalSekarang-TanggalLahir) + ((BulanSekarang-BulanLahir)*30) + ((TahunSekarang-TahunLahir)*365)
Bulan = int(((Umurdalamhari)%365)/30)
Tahun = int((Umurdalamhari)/365)
print("Umur saya adalah", Tahun, "tahun,", Bulan, "bulan.")









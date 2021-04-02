#Input nama dan nilai
nama = input('Masukkan Nama Anda :')
nilai = float(input('Masukkan nilai Anda :'))

#Ouput nilai
if nilai >= 85:
    print('Halo,', nama,'! Nilai Anda setelah dikonversi adalah A')
elif nilai >= 80:
    print('Halo,', nama, '! Nilai Anda setelah dikonversi adalah A-')
elif nilai >= 75:
    print('Halo,', nama, '! Nilai Anda setelah dikonversi adalah B+')
elif nilai >= 70:
    print('Halo,', nama, '! Nilai Anda setelah dikonversi adalah B')
elif nilai >= 65:
    print('Halo,', nama, '! Nilai Anda setelah dikonversi adalah C+')
elif nilai >= 60:
    print('Halo,', nama, '! Nilai Anda setelah dikonversi adalah C')
else:
    pass
print()

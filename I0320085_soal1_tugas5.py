#Input nama dan jenis kelamin
nama = input('Masukkan Nama Anda :')
jeniskelamin = input('Masukkan Jenis Kelamin Anda (L/P):')

#Output menyapa pengunjung
if jeniskelamin == 'L':
    print('Selama Datang, Tuan', nama,'!')
else:
    print('Selama Datang, Nyonya', nama,'!')
print()

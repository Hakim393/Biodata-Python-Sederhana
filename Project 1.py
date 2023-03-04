from ensurepip import version
from os import stat, system
d_nama = []
d_ttl = []
d_alamat = []
d_agama = []
d_kel = []

def judul():
    author()
    print('=' * 37)
    print('|          PROGRAM BIODATA          |')
    print('=' * 37)

def menu():
    system('cls')
    judul()
    print('| 1. Tambah Biodata                 |')
    print('| 2. Lihat Biodata                  |')
    print('| 3. Ubah Biodata                   |')
    print('| 4. Hapus Biodata                  |')
    print('| 5. Keluar                         |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')

    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        ubah()
    elif pilih2 == '4':
        hapus()
    elif pilih2 == '5':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu()

def tambah():
    system('cls')
    judul()
    print('Tambah Data'.center(40))
    print('=====================================')

    nama = input('Nama                  : ')
    d_nama.append(nama)
    ttl = input('Tempat/Tanggal lahir  : ')
    d_ttl.append(ttl)

    def kel():
        kelmn = input('Jenis Kelamin (L/P)   : ')
        if kelmn == 'L' or kelmn == 'l':
            k = 'Laki-Laki'
            d_kel.append(k)
        elif kelmn == 'P' or kelmn == 'p':
            k = 'Perempuan'
            d_kel.append(k)
        else : 
            print ('Input Salah')
            kel()
    kel()

    alamat = input('Alamat                : ')
    d_alamat.append(alamat)
    agama = input('Agama                 : ')
    d_agama.append(agama)
    print('=====================================')
    print ('Data Tersimpan'.center(40))
    print('=====================================')
    kembali = input('Kembali [enter]')
    menu()

def lihat():
    system('cls')
    judul()
    
    for i in range (len(d_nama)):

        print('%d.  Nama                 : %s'%(i+0, d_nama[i]))
        print('    Tempat/Tanggal Lahir : %s'%d_ttl[i])
        print('    Jenis Kelamin        : %s'%d_kel[i])
        print('    Alamat               : %s'%d_alamat[i])
        print('    Agama                : %s'%d_agama[i])
        print('-------------------------------------')
    kembali = input('Kembali Tekan [enter]')
    menu()

def ubah():
    system('cls')
    judul()
    def rubah():
        try:
            i = int (input('Inputkan ID : '))
            print('=====================================')
            
            if (i > len(d_nama[i])):
                print('')
            
            else:   
                namabaru = input('Nama                 : ')
                d_nama[i] = namabaru

                ttlbaru = input('Tempat/Tanggal Lahir : ')
                d_ttl[i] = ttlbaru

                def kelb():
                    kelmnb = input('Jenis Kelamin (L/P)  : ')
                    if kelmnb == 'L' or kelmnb == 'l':
                        kb = 'Laki-Laki'
                        d_kel[i] = kb
                    elif kelmnb == 'P' or kelmnb == 'p':
                        kb = 'Perempuan'
                        d_kel[i]= kb
                    else : 
                        print ('Input Salah')
                        kelb()
                kelb()
                alamatbaru = input('Alamat               : ')
                d_alamat[i] = alamatbaru

                agamabaru = input('Agama                : ')
                d_agama[i] = agamabaru
            print('=====================================')
            print ('Data Tersimpan'.center(40))
            print('=====================================')
            kembali = input ('Kembali Tekan [enter]')
            menu()  

        except (IndexError,ValueError):
            kembali = input("Input ID bukan angka/Data tidak ada [enter]") 
            ubah()
    rubah()

def hapus():
    system('cls')
    judul()
    def hapuss():
        try:
            print('Hapus Data'.center(40))
            print('=====================================')
            i = int(input('Masukkan ID : '))
            
            if (i > len(d_nama[i])):
                print('')
            else:

                d_nama.remove(d_nama[i])
                d_ttl.remove(d_ttl[i])
                d_kel.remove(d_kel[i])
                d_alamat.remove(d_alamat[i])
                d_agama.remove(d_agama[i])
            
            print('-------------------------------------')
            print ('Data Berhasil Dihapus'.center(40))
            print('-------------------------------------')
            input ('Kembali Tekan [enter]')
            menu()

        except (IndexError,ValueError):
            kembali = input("Input ID bukan angka/Data tidak ada [enter]") 
            hapus()

    hapuss()

def selesai():
    exit()

def author():
    print('Created by Hakim')

menu()
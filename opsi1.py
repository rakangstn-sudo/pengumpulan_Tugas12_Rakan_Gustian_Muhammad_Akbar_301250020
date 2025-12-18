import os

FILE_NAME = "nilai.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            f.write("Nama,Tugas,UTS,UAS,RataRata\n")

def hitung_rata(tugas, uts, uas):
    return (tugas + uts + uas) / 3

def tambah_data():
    nama = input("Nama Mahasiswa: ")

    try:
        tugas = float(input("Nilai Tugas: "))
        uts   = float(input("Nilai UTS: "))
        uas   = float(input("Nilai UAS: "))
    except ValueError:
        print("Nilai harus angka,Data batal disimpan")
        return

    rata = hitung_rata(tugas, uts, uas)

    with open(FILE_NAME, 'a') as f:
        f.write(f"{nama},{tugas},{uts},{uas},{rata:.2f}\n")

    print("Data berhasil disimpan")


def tampilkan_data():
    try:
        with open(FILE_NAME, 'r') as f:
            header = next(f)  # lewati header CSV

            print("\n=== DAFTAR NILAI MAHASISWA ===")
            for baris in f:
                data = baris.strip().split(",")

                print("------------------------------")
                print(f"Nama        : {data[0]}")
                print(f"Nilai Tugas : {data[1]}")
                print(f"Nilai UTS   : {data[2]}")
                print(f"Nilai UAS   : {data[3]}")
                print(f"Rata-rata   : {data[4]}")
            print("------------------------------")

    except FileNotFoundError:
        print("File data belum ada, silakan tambah data terlebih dahulu")

def cari_data():
    keyword = input("Masukkan nama yang dicari: ").lower()
    found = False

    with open(FILE_NAME, 'r') as f:
        next(f)  # lewati header
        for baris in f:
            data = baris.strip().split(",")

            if keyword == data[0].lower():
                print("\n=== DATA MAHASISWA ===")
                print(f"Nama        : {data[0]}")
                print(f"Nilai Tugas : {data[1]}")
                print(f"Nilai UTS   : {data[2]}")
                print(f"Nilai UAS   : {data[3]}")
                print(f"Rata-rata   : {data[4]}")
                found = True

    if not found:
        print("Data tidak ditemukan")


def menu():
    init_file()
    while True:
        print("\n=== SISTEM NILAI MAHASISWA ===")
        print("1. Tambah Data")
        print("2. Tampilkan Semua Data")
        print("3. Cari Data Mahasiswa")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

menu()
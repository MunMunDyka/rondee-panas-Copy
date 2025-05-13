def hitung_rata_rata(nilai_list):
    # Fungsi untuk menghitung rata-rata dari list nilai
    return sum(nilai_list) / len(nilai_list)

class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        # Inisialisasi atribut mahasiswa
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tampilkan_info(self):
        # Menampilkan informasi mahasiswa termasuk rata-rata nilai
        rata_rata = hitung_rata_rata(self.nilai)  # Menggunakan fungsi hitung_rata_rata
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Rata-rata nilai: {rata_rata:.2f}\n")

    def tambah_nilai(self, nilai_baru):
        # Menambah nilai baru ke list nilai mahasiswa btw ini perhitungannya Jumlah keselurahan rata rata bang
        self.nilai.append(nilai_baru)

if __name__ == "__main__":
    mhs1 = Mahasiswa("Andhika Laksmana", "220101", [80, 85, 90])
    mhs2 = Mahasiswa("Nabilah", "220104", [85, 80, 90])

    # Menampilkan daftar mahasiswa
    print("Daftar Mahasiswa:")
    print("1. Andhika Laksmana")
    print("2. Nabilah")

    pilih = int(input("\nPilih mahasiswa (1 atau 2): "))

    if pilih == 1:
        mahasiswa_terpilih = mhs1
    elif pilih == 2:
        mahasiswa_terpilih = mhs2
    else:
        print("Pilihan tidak valid!")
        exit()

    mahasiswa_terpilih.tampilkan_info()

    nilai_baru = float(input("Masukkan nilai baru yang ingin ditambahkan: "))
    mahasiswa_terpilih.tambah_nilai(nilai_baru)

    print("\nMenambahkan nilai baru...\n")
    mahasiswa_terpilih.tampilkan_info()

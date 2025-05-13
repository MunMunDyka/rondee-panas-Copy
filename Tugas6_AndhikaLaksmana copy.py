class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self._ipk = ipk  # Atribut privat IPK DONG

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"IPK     : {self._ipk:.2f}")

    def update_ipk(self, nilai_baru):
        if 0.0 <= nilai_baru <= 4.0:
            self._ipk = nilai_baru
        else:
            print("IPK tidak valid!")

    def status_lulus(self):
        if self._ipk >= 2.5:
            return "Lulus"
        else:
            return "Belum Lulus"


# Objek mahasiswa lagi ke 3x
mhs1 = Mahasiswa("Andhika Laksmana", "220101", "Teknik Informatika", 3.5)
mhs2 = Mahasiswa("Syahana", "220103", "Sistem Informasi", 2.8)

# Menampilkan informasi awal MAHASISWA KITA
print("Informasi Mahasiswa 1:")
mhs1.tampilkan_info()
print("\nInformasi Mahasiswa 2:")
mhs2.tampilkan_info()

# Update IPK SEMOGA LULUS
print("\nUpdate IPK Mahasiswa 2:")
mhs2.update_ipk(3.6)  # IPK yang valid
mhs2.tampilkan_info()

# Contoh input IPK tidak valid
print("\nContoh IPK tidak valid:")
mhs1.update_ipk(4.5)  # IPK yang tidak valid

# Menampilkan status lulus
print(f"\nStatus Lulus Mahasiswa 1: {mhs1.status_lulus()}")
print(f"Status Lulus Mahasiswa 2: {mhs2.status_lulus()}")

from prettytable import PrettyTable
import os


print("=== SISTEM DATA RUMAH SAKIT ===")
input("Tekan ENTER untuk mulai...")
os.system('cls')

#Data pasien
data_pasien = [
    {
        "id": "P001",
        "nama": "Ahmad Fauzi",
        "umur": "45",
        "jenis_kelamin": "Laki-laki",
        "diagnosa": "Demam Berdarah",
        "status": "Rawat Inap"
    },
    {
        "id": "P002",
        "nama": "Siti Aminah",
        "umur": "32",
        "jenis_kelamin": "Perempuan",
        "diagnosa": "Tipes",
        "status": "Rawat Jalan"
    }
]

#Melihat data pasien dalam tabel
def tabel_pasien():
    os.system('cls')
    if len(data_pasien) == 0:
        print("Data pasien sedang dalam kondisi kosong")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Status"]
        for pasien in data_pasien:
            tabel.add_row([
                pasien["id"],
                pasien["nama"],
                pasien["umur"],
                pasien["jenis_kelamin"],
                pasien["diagnosa"],
                pasien["status"]
            ])
            tabel.add_divider()
        print("\n=== Daftar Pasien ===")
        print(tabel)
        input("\nTekan ENTER untuk lanjut...")

#Sistem konfirmasi
def konfirmasi(pesan):
    while True:
        jawab = input(pesan + " (y/n): ").lower()
        if jawab in ["y", "n"]:
            return jawab == "y"
        print("Masukkan hanya 'y' atau 'n'!")

#Menambah data pasien
def tambah_pasien():
    os.system('cls')
    tabel_pasien()
    print("\n=== Tambah Data Pasien ===")

    #Loop sampai ID yang dimasukkan benar dan tidak duplikat
    while True:
        id = input("Masukkan ID Untuk Pasien: ").capitalize().strip()
        if not id:
            print("ID tidak boleh kosong.")
            continue
        id_sudah_ada = False
        for pasien in data_pasien:
            if pasien["id"] == id:
                print("ID tersebut sudah terdaftar. Silakan masukkan ID yang berbeda.")
                id_sudah_ada = True
                break
        if not id_sudah_ada:
            break  # keluar dari loop jika ID benar dan tidak ditemukan

    # Loop sampai nama tidak kosong
    while True:
        nama = input("Masukkan Nama Pasien: ").capitalize().strip()
        if nama:
            break
        else:
            print("Nama pasien tidak boleh kosong.")

    # Validasi umur dari input user (harus berupa angka) saya gunakan string bawaan python .isdigit untuk pastikan bahwa input berupa angka dan bilangan bulat
    while True:
        umur = input("Masukkan Umur Pasien: ").strip() #saya berikan strip in input supaya tidak ada sepasi kosong yang bisa ganggu kerja .isdigit nya
        if umur.isdigit():
            break
        else:
            print("Umur yang diinput harus berupa angka.")

    # Validasi jenis kelamin
    while True:
        print("\nPilih Jenis Kelamin:")
        print("1. Laki-laki")
        print("2. Perempuan")
        jk_pilihan = input("Masukkan pilihan (1/2): ").strip()
        if jk_pilihan == "1":
            jenis_kelamin = "Laki-laki"
            break
        elif jk_pilihan == "2":
            jenis_kelamin = "Perempuan"
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

    # Validasi diagnosa
    while True:
        diagnosa = input("Masukkan Diagnosa dari Pasien: ").capitalize().strip()
        if diagnosa:
            break
        else:
            print("Diagnosa tidak boleh kosong.")

    # Validasi status pasien
    while True:
        print("\nPilih Status Pasien:")
        print("1. Rawat Inap")
        print("2. Rawat Jalan")
        print("3. Sembuh")
        print("4. Meninggal")
        status_pilihan = input("Masukkan pilihan (1-4): ").strip()
        if status_pilihan == "1":
            status = "Rawat Inap"
            break
        elif status_pilihan == "2":
            status = "Rawat Jalan"
            break
        elif status_pilihan == "3":
            status = "Sembuh"
            break
        elif status_pilihan == "4":
            status = "Meninggal"
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

    # Konfirmasi
    if konfirmasi("Apakah data sudah benar dan ingin disimpan?"):
        data_baru = {
            "id": id,
            "nama": nama,
            "umur": umur,
            "jenis_kelamin": jenis_kelamin,
            "diagnosa": diagnosa,
            "status": status
        }
        data_pasien.append(data_baru)
        print("Pasien baru berhasil didaftarkan")
        input("Tekan ENTER untuk melihat daftar pasien...")
        tabel_pasien()
    else:
        print("Penambahan dibatalkan")

#Menghapus data pasien
def hapus_pasien():
    os.system('cls')
    tabel_pasien()
    print("\n=== Hapus Data Pasien ===")
    while True:
        id = input("Masukkan ID Pasien yang ingin dihapus: ").capitalize().strip()

        if not id:
            print("ID tidak boleh kosong. Silakan coba lagi.")
            continue

        pasien_ditemukan = None
        for pasien in data_pasien:
            if pasien["id"] == id:
                pasien_ditemukan = pasien
                break

        if pasien_ditemukan:
            nama_pasien = pasien_ditemukan["nama"]
            if konfirmasi(f"Yakin ingin menghapus data pasien '{nama_pasien}'?"):
                data_pasien.remove(pasien_ditemukan)
                print(f"Data Pasien {nama_pasien} berhasil dihapus.")
                input("Tekan ENTER untuk melihat daftar pasien...")
                tabel_pasien()
            else:
                print("Penghapusan pasien dibatalkan.")
                input("Tekan ENTER untuk kembali...")
            break  
        else:
            print("ID pasien tidak ditemukan. Silakan coba lagi.")

#Mengubah data pasien
def ubah_data():
    while True:
        tabel_pasien()
        print("\n=== Ubah Data Pasien ===")

        #Cari pasien berdasarkan ID
        while True:
            id = input("Masukkan ID Pasien yang ingin diubah (atau ketik 'x' untuk batal): ").capitalize().strip()
            if id.lower() == 'x':
                return  

            pasien_ditemukan = None
            for pasien in data_pasien:
                if pasien["id"] == id:
                    pasien_ditemukan = pasien
                    break

            if pasien_ditemukan:
                break
            else:
                print("ID tidak ditemukan. Silakan coba lagi.")

        #tampilan tabel dari data yang akan di ubah saja
        while True:
            os.system('cls')
            print("\n=== Data Saat Ini ===")
            table = PrettyTable()
            table.field_names = ["ID", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Status"]
            table.add_row([
                pasien_ditemukan["id"],
                pasien_ditemukan["nama"],
                pasien_ditemukan["umur"],
                pasien_ditemukan["jenis_kelamin"],
                pasien_ditemukan["diagnosa"],
                pasien_ditemukan["status"]
            ])
            print(table)

            print("\n=== Pilih Data yang Ingin Diubah ===")
            print("1. Nama")
            print("2. Umur")
            print("3. Jenis Kelamin")
            print("4. Diagnosa")
            print("5. Status")
            print("6. Kembali")

            pilihan = input("Masukkan pilihan (1-6): ")

            if pilihan == "1":
                while True:
                    nama_baru = input("Masukkan Nama Baru: ").capitalize().strip()
                    if nama_baru:
                        pasien_ditemukan["nama"] = nama_baru
                        break
                    else:
                        print("Nama tidak boleh kosong.")
            elif pilihan == "2":
                while True:
                    umur_baru = input("Masukkan Umur Baru: ").strip()
                    if umur_baru.isdigit():
                        pasien_ditemukan["umur"] = umur_baru
                        break
                    else:
                        print("Umur harus berupa angka.")
            elif pilihan == "3":
                while True:
                    print("\nPilih Jenis Kelamin:")
                    print("1. Laki-laki")
                    print("2. Perempuan")
                    jk_pilihan = input("Masukkan pilihan (1/2): ")
                    if jk_pilihan == "1":
                        pasien_ditemukan["jenis_kelamin"] = "Laki-laki"
                        break
                    elif jk_pilihan == "2":
                        pasien_ditemukan["jenis_kelamin"] = "Perempuan"
                        break
                    else:
                        print("Pilihan tidak valid. Coba lagi.")
            elif pilihan == "4":
                while True:
                    diagnosa_baru = input("Masukkan Diagnosa Baru: ").capitalize().strip()
                    if diagnosa_baru:
                        pasien_ditemukan["diagnosa"] = diagnosa_baru
                        break
                    else:
                        print("Diagnosa tidak boleh kosong.")
            elif pilihan == "5":
                while True:
                    print("\nPilih Status Pasien:")
                    print("1. Rawat Inap")
                    print("2. Rawat Jalan")
                    print("3. Sembuh")
                    print("4. Meninggal")
                    status_pilihan = input("Masukkan pilihan (1-4): ")
                    if status_pilihan == "1":
                        pasien_ditemukan["status"] = "Rawat Inap"
                        break
                    elif status_pilihan == "2":
                        pasien_ditemukan["status"] = "Rawat Jalan"
                        break
                    elif status_pilihan == "3":
                        pasien_ditemukan["status"] = "Sembuh"
                        break
                    elif status_pilihan == "4":
                        pasien_ditemukan["status"] = "Meninggal"
                        break
                    else:
                        print("Pilihan tidak valid.")
            elif pilihan == "6":
                return
            else:
                print("Pilihan tidak valid.")
                continue

            print("\nData berhasil diperbarui. Berikut data terbaru:")
            tabel = PrettyTable()
            tabel.field_names = ["ID", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Status"]
            tabel.add_row([
                pasien_ditemukan["id"],
                pasien_ditemukan["nama"],
                pasien_ditemukan["umur"],
                pasien_ditemukan["jenis_kelamin"],
                pasien_ditemukan["diagnosa"],
                pasien_ditemukan["status"]
            ])
            print(tabel)

            #Menu konfirmasi setelah update
            while True:
                print("\nApakah ingin mengubah data lagi?")
                print("1. Ya, ID yang sama")
                print("2. Ya, ID berbeda")
                print("3. Tidak, kembali ke menu")
                ulang = input("Masukkan pilihan (1/2/3): ")

                if ulang == "1":
                    break
                elif ulang == "2":
                    return ubah_data()
                elif ulang == "3":
                    return
                else:
                    print("Pilihan tidak valid. Coba lagi.")

#Mencari Pasien Berdasarkan ID hanya tampikan 1 pasien aja
def pasien_id():
    os.system('cls')
    while True:
        id_pasien = input("Masukkan ID Pasien (atau ketik 'x' untuk kembali): ").capitalize().strip()
        if id_pasien.lower() == 'x':
            return
        if not id_pasien:
            print("ID tidak boleh kosong.")
            continue

        # Cek apakah ada pasien dengan ID tsb
        for pasien in data_pasien:
            if pasien["id"] == id_pasien:
                tabel = PrettyTable()
                tabel.field_names = ["ID", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Status"]
                tabel.add_row([
                    pasien["id"],
                    pasien["nama"],
                    pasien["umur"],
                    pasien["jenis_kelamin"],
                    pasien["diagnosa"],
                    pasien["status"]
                ])
                print(tabel)
                input("\nTekan ENTER untuk kembali...")
                return

        print("Data pasien dengan ID tersebut tidak ditemukan.")
        input("Tekan ENTER untuk coba lagi...")

#Mencari pasien berdasarkan status
def pasien_status():
            os.system('cls')
            print("\n=== Cari Pasien Berdasarkan Status ===")
            print("1. Rawat Inap")
            print("2. Rawat Jalan")
            print("3. Sembuh")
            print("4. Meninggal")
            print("5. Kembali")

            pilihan = input("Pilih status (1-5): ")

            if pilihan == "1":
                status_input = "Rawat Inap"
            elif pilihan == "2":
                status_input = "Rawat Jalan"
            elif pilihan == "3":
                status_input = "Sembuh"
            elif pilihan == "4":
                status_input = "Meninggal"
            elif pilihan == "5":
                sub_menu()
            else:
                print("Pilihan tidak valid.")
                return

            #menampilkan tabel dari status yang di pilih
            tabel = PrettyTable()
            tabel.field_names = ["ID", "Nama", "Umur", "Jenis Kelamin", "Diagnosa", "Status"]

            ditemukan = False
            for pasien in data_pasien:
                if pasien["status"] == status_input:
                    tabel.add_row([
                        pasien["id"],
                        pasien["nama"],
                        pasien["umur"],
                        pasien["jenis_kelamin"],
                        pasien["diagnosa"],
                        pasien["status"]
                    ])
                    tabel.add_divider()
                    ditemukan = True

            if ditemukan:
                print(f"\n=== Hasil Pencarian Status: {status_input} ===")
                print(tabel)
            else:
                print(f"Tidak ada pasien dengan status '{status_input}'.")

            input("\nTekan ENTER untuk lanjut...")

#Menu utama
def main_menu():
    while True:
        os.system('cls')
        print("\n=== Menu Utama ===")
        print("1. Lihat Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Ubah Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            sub_menu()
        elif pilihan == "2":
            login_1()
            tambah_pasien()
        elif pilihan == "3":
            login_1()
            ubah_data()
        elif pilihan == "4":
            login_1()
            hapus_pasien()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan ENTER untuk lanjut...")

#Sub menu ketika pilih opsi 1
def sub_menu():
    while True:
        os.system('cls')
        print("\n=== Lihat Data Pasien ===")
        print("1. Lihat Semua Data Pasien")
        print("2. Cari Pasien Berdasarkan ID")
        print("3. Cari Pasien Berdasarkan Status")
        print("4. Kembali ke Menu Utama")

        sub_pilihan = input("Masukkan pilihan (1-4): ")

        if sub_pilihan == "1":
            tabel_pasien()
        elif sub_pilihan == "2":
            pasien_id()
        elif sub_pilihan == "3":
            pasien_status()
        elif sub_pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan ENTER untuk lanjut...")

#Bagian login dari sistem rumah sakit
def login():
    while True:
        print("=== LOGIN SISTEM DATA RUMAH SAKIT ===")
        password = input("Masukkan password: ")
        if password == "admin123":
            print("Login berhasil!\n")
            os.system('cls')
            break
        else:
            print("Password salah, coba lagi.\n")
            input("\nTekan ENTER untuk lanjut...")
            os.system('cls')

#Bagian untuk Login menu 2-4 pada menu utama
def login_1():
    while True:
        print("=== LOGIN SISTEM DATA RUMAH SAKIT ===")
        password = input("Masukkan password: ")
        if password == "123admin":
            print("Login berhasil!\n")
            os.system('cls')
            break
        else:
            print("Password salah, coba lagi.\n")
            input("\nTekan ENTER untuk lanjut...")
            os.system('cls')

# berfungsi agar program selalu kembali ke awal kecuali di matikan langsung dari terminal
def run_program():  
    while True:
        os.system('cls')
        login()
        main_menu()

run_program()
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# Fungsi Interpolasi Lagrange
def interpolasi_lagrange(x, y, x_query):
    n = len(x)
    hasil = 0
    for i in range(n):
        suku = y[i]
        for j in range(n):
            if j != i:
                suku *= (x_query - x[j]) / (x[i] - x[j])
        hasil += suku
    return hasil

# Fungsi Diferensiasi Numerik
def diferensi_maju(f, x, h):
    return (f(x + h) - f(x)) / h

def diferensi_mundur(f, x, h):
    return (f(x) - f(x - h)) / h

def diferensi_sentral(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Fungsi Aturan Trapesium
def aturan_trapesium(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Fungsi Plotting
def buat_grafik(x, y, label_x, label_y, judul, nama_file):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'o', label='Titik data')
    plt.plot(x, y, '-', label='Garis interpolasi')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(judul)
    plt.legend()
    plt.savefig(nama_file)
    plt.show()

# Fungsi I/O dan Menu
def ambil_data():
    while True:
        try:
            print("Pilih jenis data:")
            print("1. Posisi")
            print("2. Kecepatan")
            print("3. Percepatan")
            print("4. Kembali ke menu utama")
            pilihan_jenis_data = int(input("Masukkan pilihan (1/2/3/4): "))
            if pilihan_jenis_data == 4:
                return None, None, None
            if pilihan_jenis_data == 1:
                jenis_data = 'posisi'
            elif pilihan_jenis_data == 2:
                jenis_data = 'kecepatan'
            elif pilihan_jenis_data == 3:
                jenis_data = 'percepatan'
            else:
                raise ValueError("Pilihan tidak valid.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    while True:
        try:
            n = int(input("Masukkan jumlah data: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    waktu = []
    data = []
    for i in range(n):
        while True:
            try:
                t = float(input(f"Masukkan waktu ke-{i + 1}: "))
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
        while True:
            try:
                d = float(input(f"Masukkan data ke-{i + 1}: "))
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
        waktu.append(t)
        data.append(d)
    return jenis_data, np.array(waktu), np.array(data)

def simpan_ke_csv(data):
    with open('data_simpan.csv', mode='w', newline='') as file:
        penulis = csv.writer(file)
        penulis.writerow(["slot", "jenis_data", "waktu", "data"])
        for slot, (jenis_data, waktu, data) in data.items():
            waktu_str = ' '.join(map(str, waktu))
            data_str = ' '.join(map(str, data))
            penulis.writerow([slot, jenis_data, waktu_str, data_str])

def muat_dari_csv():
    data = {}
    if os.path.exists('data_simpan.csv'):
        with open('data_simpan.csv', mode='r') as file:
            pembaca = csv.reader(file)
            next(pembaca)  # Lewati header
            for row in pembaca:
                slot = int(row[0])
                jenis_data = row[1]
                waktu = np.array(list(map(float, row[2].split())))
                nilai_data = np.array(list(map(float, row[3].split())))
                data[slot] = (jenis_data, waktu, nilai_data)
    return data

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_utama():
    global data_simpan
    data_simpan = muat_dari_csv()
    while True:
        bersihkan_layar()
        print("Menu Utama:")
        print("1. Input Data")
        print("2. Output Data")
        print("3. Hapus Data")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            input_data()
        elif pilihan == '2':
            output_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            simpan_ke_csv(data_simpan)
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def input_data():
    global data_simpan
    while True:
        bersihkan_layar()
        print("Input Data:")
        for slot in range(1, 6):
            status = "kosong" if slot not in data_simpan else "terisi"
            print(f"Slot {slot}: {status}")
        print("6. Kembali ke menu utama")
        try:
            pilihan_slot = int(input("Pilih slot untuk menyimpan data (1-5/6): "))
            if pilihan_slot == 6:
                return
            if pilihan_slot < 1 or pilihan_slot > 5:
                raise ValueError("Nomor slot harus antara 1 dan 5.")
            if pilihan_slot in data_simpan:
                print(f"Slot {pilihan_slot} sudah terisi. Data pada slot ini akan diganti.")
                konfirmasi = input("Apakah Anda yakin? (y/n): ").lower()
                if konfirmasi != 'y':
                    continue
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    jenis_data, waktu, data = ambil_data()
    if jenis_data is None:
        return
    data_simpan[pilihan_slot] = (jenis_data, waktu, data)
    print(f"Data berhasil disimpan di slot {pilihan_slot}")
    input("Tekan Enter untuk kembali ke menu utama...")

def output_data():
    global data_simpan
    while True:
        bersihkan_layar()
        print("Output Data:")
        for slot in range(1, 6):
            status = "kosong" if slot not in data_simpan else "terisi"
            print(f"Slot {slot}: {status}")
        print("6. Kembali ke menu utama")
        try:
            pilihan_slot = int(input("Pilih slot data yang ingin digunakan (1-5/6): "))
            if pilihan_slot == 6:
                return
            if pilihan_slot not in data_simpan:
                raise ValueError("Slot data tidak ditemukan.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    jenis_data, waktu, data = data_simpan[pilihan_slot]
    while True:
        try:
            t_query = float(input(f"Masukkan waktu untuk query (rentang {min(waktu)} hingga {max(waktu)}): "))
            if t_query < min(waktu) or t_query > max(waktu):
                raise ValueError(f"Waktu harus dalam rentang {min(waktu)} hingga {max(waktu)}.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    while True:
        try:
            print("Pilih jenis output data:")
            print("1. Posisi")
            print("2. Kecepatan")
            print("3. Percepatan")
            pilihan_jenis_output = int(input("Masukkan pilihan (1/2/3): "))
            if pilihan_jenis_output < 1 or pilihan_jenis_output > 3:
                raise ValueError("Pilihan tidak valid.")
            if pilihan_jenis_output == 1:
                jenis_output = 'posisi'
            elif pilihan_jenis_output == 2:
                jenis_output = 'kecepatan'
            elif pilihan_jenis_output == 3:
                jenis_output = 'percepatan'
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    h = (max(waktu) - min(waktu)) / (len(waktu) - 1)

    if jenis_output == 'posisi':
        hasil = interpolasi_lagrange(waktu, data, t_query)
        print(f"Posisi pada waktu {t_query} adalah {hasil}")
    elif jenis_output == 'kecepatan':
        f_interpolasi = lambda t: interpolasi_lagrange(waktu, data, t)
        hasil = diferensi_sentral(f_interpolasi, t_query, h)
        print(f"Kecepatan pada waktu {t_query} adalah {hasil}")
    elif jenis_output == 'percepatan':
        f_interpolasi = lambda t: interpolasi_lagrange(waktu, data, t)
        hasil = diferensi_sentral(lambda t: diferensi_sentral(f_interpolasi, t, h), t_query, h)
        print(f"Percepatan pada waktu {t_query} adalah {hasil}")

    print("\nPilih opsi berikut:")
    print("1. Buat grafik")
    print("2. Simpan hasil ke file teks")
    print("3. Kembali ke menu utama")
    pilihan_output = input("Pilih opsi: ")

    if pilihan_output == '1':
        nama_file_grafik = input("Masukkan nama file untuk grafik (misal: grafik.png): ")
        buat_grafik(waktu, data, 'Waktu', jenis_output.capitalize(), f"{jenis_output.capitalize()} vs Waktu", nama_file_grafik)
    elif pilihan_output == '2':
        nama_file_teks = input("Masukkan nama file untuk hasil (misal: hasil.txt): ")
        with open(nama_file_teks, 'w') as file:
            file.write(f"Jenis data: {jenis_data}\n")
            file.write(f"Waktu query: {t_query}\n")
            file.write(f"Hasil {jenis_output}: {hasil}\n")
        print(f"Hasil berhasil disimpan ke {nama_file_teks}")

    input("Tekan Enter untuk kembali ke menu utama...")

def hapus_data():
    global data_simpan
    while True:
        bersihkan_layar()
        print("Hapus Data:")
        for slot in range(1, 6):
            status = "kosong" if slot not in data_simpan else "terisi"
            print(f"Slot {slot}: {status}")
        print("6. Kembali ke menu utama")
        try:
            pilihan_slot = int(input("Pilih slot data yang ingin dihapus (1-5/6): "))
            if pilihan_slot == 6:
                return
            if pilihan_slot not in data_simpan:
                raise ValueError("Slot data tidak ditemukan.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    konfirmasi = input(f"Apakah Anda yakin ingin menghapus data di slot {pilihan_slot}? (y/n): ").lower()
    if konfirmasi == 'y':
        del data_simpan[pilihan_slot]
        print(f"Data di slot {pilihan_slot} berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
    input("Tekan Enter untuk kembali ke menu utama...")

if __name__ == '__main__':
    menu_utama()
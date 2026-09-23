# ============================================================
# TUPLE
# ============================================================

# --- Cara membuat tuple ---
tuple_jenis_kelamin = ('laki-laki', 'perempuan')        # cara standar
tuple_status_perkawinan = 'menikah', 'lajang'            # tanpa kurung
tuple_lulus = tuple(['lulus', 'tidak lulus'])            # fungsi tuple()

# tuple kosong
tuple_kosong = ()

# tuple yang hanya berisi satu item (wajib pakai tanda koma)
tuple_tunggal = (10,)
print(type((10)))    # yang ini dianggap integer biasa
print(type((10,)))   # yang ini dianggap tuple

# --- Cara mengakses nilai tuple ---
tuple_jenis_kelamin = ('laki-laki', 'perempuan')
print(tuple_jenis_kelamin[1])   # indeks satu
print(tuple_jenis_kelamin[0])   # indeks nol

print(tuple_jenis_kelamin[-2])
print(tuple_jenis_kelamin[-1])

# --- Slicing tuple ---
tuple_buah = ('Pisang', 'Nanas', 'Melon', 'Durian')
print(tuple_buah[0:1])
print(tuple_buah[0:2])
print(tuple_buah[1:3])
print(tuple_buah[0:-1])
print(tuple_buah[-1:-3])
print(tuple_buah[-1:3])
print(tuple_buah[-3:-1])

# --- Sequence unpacking ---
siswa = ('Nurul Huda', 'Bangkalan', 24)
nama, asal, usia = siswa   # ekstrak isi tuple ke variabel-variabel
print('Nama:', nama)
print('Asal:', asal)
print('Usia:', usia)

# --- Menggabungkan dua buah tuple atau lebih ---
a = (1, 2, 3)
b = (50, 60, 70)
c = a + b
print(c)

# --- Fungsi-fungsi bawaan tuple ---
nilai_semester_1 = (80, 90, 100, 88, 60)
print(max(nilai_semester_1))
print(min(nilai_semester_1))
print(len(nilai_semester_1))

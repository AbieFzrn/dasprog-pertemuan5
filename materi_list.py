# ============================================================
# LIST
# ============================================================

# --- Membuat list ---
list_kosong = []                                          # list kosong
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']         # list berisi string
list_nilai = [80, 70, 90, 60]                              # list berisi integer
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]     # list campuran

# --- Menampilkan list ---
print('list_kosong:', list_kosong)
print('list_buah:', list_buah)
print('list_nilai:', list_nilai)
print('list_jawaban:', list_jawaban)

# menampilkan dengan indeks
print(list_buah[0])
print(list_buah[2])
print(list_buah[1])
print(list_buah[3])

# menampilkan dengan indeks negatif
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

# --- Slicing list ---
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])

# --- Slicing tanpa batas ---
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
print(list_buah[0:])
print(list_buah[1:])
print(list_buah[2:])
print(list_buah[3:])
print(list_buah[:0])
print(list_buah[:1])
print(list_buah[:2])
print(list_buah[:3])
print(list_buah[:4])

# --- Mengubah data di dalam list ---
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
print(list_buah)
list_buah[0] = 'Jeruk'          # ubah data pertama
print(list_buah)
list_buah[-1] = 'Mangga'        # ubah data terakhir
print(list_buah)

# ubah data dalam range
list_buah[1:3] = ['Naga', 'Pepaya']
print(list_buah)

# --- Menambah item ke dalam list ---
list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
print(list_buah)
list_buah.append('Sirsak')      # tambah data di belakang list
print(list_buah)
list_buah.insert(0, 'Jambu')    # tambah data di awal list
print(list_buah)
list_buah.insert(2, 'Manggis')  # tambah data di index mana pun
print(list_buah)

# --- Menghapus item dari list ---
# menggunakan fungsi pop()
list_angka = [1, 2, 3, 4, 5]
print(list_angka)
angka_yang_terhapus = list_angka.pop()   # hapus satu angka di belakang
print('angka yang terhapus:', angka_yang_terhapus)
print(list_angka)

# menggunakan fungsi remove()
list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)
list_buah.remove('Jambu')   # hapus item pertama dengan nilai 'Jambu'
print(list_buah)

# menggunakan statement del
print('' * 2)
list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)
del list_buah[1]
print(list_buah)
del list_buah[0:2]
print(list_buah)

# --- Menggabungkan dua buah list atau lebih ---
a = [1, 2, 3]
b = ['a']
c = [True, 'b', False]
listBaru = a + b + c
print(listBaru)

# --- Mengurutkan data ---
list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print(list_buah)
list_buah.sort()      # urutkan secara ascending
print(list_buah)
list_buah.reverse()   # membalikkan posisi item list
print(list_buah)

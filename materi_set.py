# ============================================================
# SET
# ============================================================

# --- Cara membuat set ---
himpunan_siswa = {'Huda', 'Lendis', 'Wahid', 'Basith'}   # kurung kurawal
print(himpunan_siswa)
himpunan_buah = set(['mangga', 'apel'])                   # dari list
print(himpunan_buah)
set_campuran = {'manusia', 'hewan', 5, True, ('A', 'B')}  # tipe data campuran
print(set_campuran)

# --- Set bersifat unordered ---
set_ku = {'a'}
# baris berikut sengaja dikomentari karena set tidak bisa diakses pakai indeks
# (akan muncul: TypeError: 'set' object is not subscriptable)
# print(set_ku[0])

himpunan_siswa = {'Huda', 'Lendis', 'Wahid', 'Basith'}
print(himpunan_siswa)

# --- Set bersifat unchangable ---
# anggota set harus dari tipe data yang immutable
set_buah = {'mangga', 'lemon', 'alpukat', True, 1, 2, 3}
# tuple boleh jadi anggota set karena bersifat immutable
papan_ketik = {
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (0)
}

# list tidak boleh jadi anggota set karena list bersifat mutable
# baris berikut sengaja dikomentari
# (akan muncul: TypeError: unhashable type: 'list')
# x = {35, 100, ['a', 'b']}

# --- Tidak bisa menerima nilai duplikat ---
list_kata = [
    'pagi', 'ini', 'adalah', 'pagi', 'yang',
    'sangat', 'cerah'
]
print(list_kata)

kata_unik = {
    'pagi', 'ini', 'adalah', 'pagi', 'yang',
    'sangat', 'cerah'
}
# atau bisa langsung konversi list_kata menjadi set:
# kata_unik = set(list_kata)
print(kata_unik)

# --- Menambah anggota baru ---
himpunan_abjad = {'a', 'b', 'c'}
print(himpunan_abjad)
himpunan_abjad.add('d')            # menambah satu-satu
himpunan_abjad.add('e')
himpunan_abjad.update({'f', 'g'})  # menambah lebih dari satu sekaligus
himpunan_abjad.update(['h', 'i'])  # bisa juga pakai list
print(himpunan_abjad)

# --- Menghapus anggota ---
himpunan = {'maya', 'budi', 100, ('a', 'b'), False, True}
print(himpunan)
himpunan.remove(100)                  # error jika nilai tidak ada
print(himpunan)
himpunan.discard(('a', 'b'))          # tidak error jika nilai tidak ada
print(himpunan)
nilaiYangDihapus = himpunan.pop()     # ambil & hapus nilai di sebelah kiri
print('nilaiYangDihapus =', nilaiYangDihapus)
print(himpunan)
himpunan.clear()                      # hapus semua nilai
print(himpunan)

# --- Fungsi keanggotaan pada set ---
grup_smp = {'andi', 'budi', 'ratna', 'sari'}
grup_sma = {'putri', 'ratna', 'andi', 'agus'}

# union (gabungan)
print(grup_smp | grup_sma)
print(grup_smp.union(grup_sma))

# intersection (irisan)
print(grup_smp & grup_sma)
print(grup_smp.intersection(grup_sma))

# difference (selisih)
print('
anggota grup smp yang bukan anggota grup sma')
print(grup_smp - grup_sma)
print(grup_smp.difference(grup_sma))

print('
dibalik, anggota grup sma yang bukan anggota grup smp:')
print(grup_sma - grup_smp)
print(grup_sma.difference(grup_smp))

# symmetric_difference (hanya anggota satu grup saja)
print('
anggota yang hanya ikut satu grup saja:')
print(grup_sma.symmetric_difference(grup_smp))

# --- Menampilkan anggota set dengan perulangan ---
himpunan_buah = {'pepaya', 'apel', 'jagung', 'rambutan'}
for buah in himpunan_buah:
    print(buah)

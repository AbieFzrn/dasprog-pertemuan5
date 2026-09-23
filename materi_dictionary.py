# ============================================================
# DICTIONARY
# ============================================================

pertemuan_hari_ini = {
    "judul": "Belajar Dictionary Pada Python 3",
    "tanggal": "01 Februari 2021",
    "kategori": ["Python", "Python Dasar"],
    "page_views": 10,
    "published": True,
    "share_count": {
        "facebook": 0,
        "twitter": 2
    }
}

# --- Sifat unique: key yang sama akan menimpa nilai sebelumnya ---
artikel = {
    "judul": "Menu Masakan Enak",
    "judul": "Menu Masakan Enak Tradisional"
}
print(artikel.get("judul"))

# --- Cara membuat dictionary ---
buku = {                                    # cara pertama
    "judul": "Daun Yang Jatuh Tidak Pernah Membenci Angin",
    "penulis": "Tere Liye"
}
buku = dict(                                # cara kedua
    judul="Daun Yang Jatuh Tidak Pernah Membenci Angin",
    penulis="Tere Liye"
)

# --- Cara mengakses item pada dictionary ---
pertemuan_hari_ini = {
    "judul": "Belajar Dictionary Pada Python 3",
    "tanggal": "01 Februari 2021",
    "kategori": ["Python", "Python Dasar"],
    "page_views": 10,
    "published": True,
    "share_count": {
        "facebook": 0,
        "twitter": 2
    }
}

print('Judul:', pertemuan_hari_ini.get('judul'))
print('Tanggal:', pertemuan_hari_ini['tanggal'])
print('Facebook share:', pertemuan_hari_ini.get('share_count').get('facebook'))
print('Twitter share:', pertemuan_hari_ini['share_count']['twitter'])

# get() dengan nilai default
share_count = pertemuan_hari_ini.get('share_count')
# baris berikut sengaja dikomentari karena key 'instagram' tidak ada
# (akan muncul: KeyError: 'instagram')
# print('Instagram share:', share_count['instagram'])
print('Instagram share:', share_count.get('instagram', 0))   # ini tidak error

# --- Perulangan untuk dictionary ---
buku = {
    'judul': 'Hafalan Sholat Delisa',
    'penulis': 'Tere Liye'
}
for key in buku:
    print(key, '->', buku[key])

for nama_atribut, nilai in buku.items():
    print(nama_atribut, '->', nilai)

# --- Mengubah nilai item ---
mahasiswa = {
    'nama': 'Lendis Fabri',
    'asal': 'Indonesia'
}
print('Nama awal:', mahasiswa.get('nama'))
mahasiswa['nama'] = 'Andi Mukhlish'
print('Setelah diubah:', mahasiswa.get('nama'))

# --- Menambahkan item ---
mahasiswa = {
    'nama': 'Lendis Fabri',
    'asal': 'Indonesia',
}
print('Hobi:', mahasiswa.get('hobi'))     # output None
mahasiswa['hobi'] = 'Memancing'
print('Hobi dari {} adalah {}'.format(
    mahasiswa.get('nama'),
    mahasiswa.get('hobi')
))

# --- Menghapus item ---
mahasiswa = {
    'nama': 'Wahid Abdullah',
    'usia': 18,
    'asal': 'Indonesia'
}
del mahasiswa['nama']
mahasiswa.pop('usia')
mahasiswa.pop('asal')

# pop() mengembalikan nilai yang dihapus
pesan_singkat = {
    "isi": "ISI PESAN INI HANYA BISA DIBACA SEKALI SAJA!! 😱"
}
isi_pesan = pesan_singkat.pop('isi')
print('isi pesan:', pesan_singkat.get('isi'))   # output: None
print('isi pesan:', isi_pesan)

# --- Operator keanggotaan ---
siswa = {'nama': 'Renza Ilhami'}
print('Apakah variabel siswa memiliki key nama?')
print('nama' in siswa)
print('
Apakah variabel siswa TIDAK memiliki key usia?')
print('usia' not in siswa)

# --- Panjang atau banyak key pada dictionary ---
sekolah = {
    'nama': 'Sekolah Dasar Negeri Surabaya 1',
    'jenjang': 'Sekolah Dasar',
    'akreditasi': 'A'
}
print("Jumlah atribut variabel sekolah adalah:", len(sekolah))

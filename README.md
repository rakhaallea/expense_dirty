# Expense Cleaner & Tracker (OOP Python)

## 📌 Deskripsi Project

Project ini merupakan program sederhana berbasis Python untuk membaca dan mengolah data pengeluaran (expense) dari file CSV yang masih memiliki data kotor (dirty data).

Program dibuat menggunakan konsep **Object-Oriented Programming (OOP)** dan struktur **modular programming** agar code lebih rapih, mudah dikembangkan, dan mudah dipahami.

---

# 🎯 Tujuan Program

Program ini dibuat untuk:

- Membaca data dari file CSV
- Membersihkan data yang tidak valid
- Menandai data error tanpa membuat program crash
- Mengelompokkan total pengeluaran berdasarkan kategori
- Menampilkan summary data valid dan error

---

# 📂 Struktur Folder

```text
expense_project/
│
├── main.py
│
├── models/
│   ├── expense_record.py
│   └── expense_tracker.py
│
├── services/
│   └── cleaner.py
│
├── data/
│   └── expense_dirty.csv
│
└── README.md
```

---

# 🧩 Penjelasan Class

## 1. ExpenseRecord

Class ini digunakan untuk merepresentasikan satu data pengeluaran.

### Attribute:

| Attribute | Fungsi                             |
| --------- | ---------------------------------- |
| tanggal   | Menyimpan tanggal transaksi        |
| amount    | Menyimpan nominal pengeluaran      |
| kategori  | Menyimpan kategori pengeluaran     |
| status    | Menyimpan status data (OK / ERROR) |

### Method:

| Method       | Fungsi                     |
| ------------ | -------------------------- |
| is_valid()   | Mengecek apakah data valid |
| is_invalid() | Mengecek apakah data error |

---

## 2. ExpenseTracker

Class ini digunakan untuk mengelola seluruh data pengeluaran.

### Fungsi utama:

- Membaca file CSV
- Melakukan cleaning data
- Menghitung total pengeluaran per kategori
- Menampilkan summary data
- Menampilkan data error

---

# 🧹 Strategi Data Cleaning

Program menggunakan strategi:

## ✅ Mark as Error

Jika ditemukan data:

- kosong
- invalid
- tidak dapat dikonversi ke angka

maka data:

- tetap disimpan
- diberi status `"ERROR"`

Contoh:

```python
ExpenseRecord(..., status="ERROR")
```

---

# 🔄 Alur Program

## 1. Read

Program membaca file CSV menggunakan:

```python
csv.DictReader()
```

---

## 2. Clean & Validate

Data dibersihkan menggunakan function:

```python
clean_row()
```

Validasi dilakukan pada kolom:

- amount

---

## 3. Store

Data yang sudah diproses disimpan ke dalam:

```python
self.expenses
```

---

## 4. Process

Program menghitung total pengeluaran per kategori.

Contoh:

- makan
- transport
- belanja

---

## 5. Output

Program menampilkan:

- data error
- jumlah data valid & error
- total pengeluaran per kategori

---

# 🛡️ Error Handling

Program menggunakan:

```python
try-except
```

Tujuannya agar:

- program tidak crash
- data invalid tetap bisa diproses

---

# 📊 Contoh Output

```text
======================================================================
                            DATA ERROR
======================================================================

1. Tanggal  : 2024-01-02
   Kategori : transport
   Amount   : Rp 0
   Status   : ERROR
----------------------------------------------------------------------

======================================================================
                 TOTAL DATA OK DAN ERROR
======================================================================
Jumlah Data Error     : 2
Jumlah Data Valid     : 118
Total Data            : 120
======================================================================

======================================================================
            TOTAL PENGELUARAN PER KATEGORI
======================================================================
makan               Rp          70.000
transport           Rp          15.000
======================================================================
```

---

# ✅ Keunggulan Program

- Menggunakan OOP
- Menggunakan modular programming
- Memiliki error handling
- Tidak crash saat data kotor ditemukan
- Struktur code lebih rapih dan scalable

---

# ⚠️ Kekurangan Program

- Validasi tanggal masih sederhana
- Belum export hasil cleaning ke CSV baru
- Tampilan output masih console text
- Belum menggunakan database

---

# 🚀 Pengembangan Selanjutnya

Program masih dapat dikembangkan menjadi:

- GUI/Desktop App
- Dashboard visualisasi
- Export Excel/CSV
- Database integration
- Web application

---

# 👨‍💻 Teknologi yang Digunakan

- Python 3
- CSV Module
- Object-Oriented Programming (OOP)

---

# 📌 Kesimpulan

Program berhasil membaca dan membersihkan data expense yang kotor menggunakan pendekatan OOP dan modular programming. Program juga mampu menangani error tanpa menyebabkan crash serta menghasilkan rekap pengeluaran berdasarkan kategori.

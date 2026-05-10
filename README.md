# Expense Cleaner & Tracker (OOP Python)

## 📌 Deskripsi Project

Project ini merupakan program sederhana berbasis Python untuk membaca dan mengolah data pengeluaran (expense) dari file CSV yang masih memiliki data kotor (dirty data).

Program dibuat menggunakan konsep:
- Object-Oriented Programming (OOP)
- Modular Programming

Tujuan utama project ini adalah agar code:
- lebih rapih
- mudah dipahami
- mudah dikembangkan
- memiliki pemisahan tanggung jawab yang jelas

---

# 🎯 Tujuan Program

Program ini dibuat untuk:
- Membaca data dari file CSV
- Membersihkan data yang tidak valid
- Menandai data error tanpa membuat program crash
- Mengelompokkan total pengeluaran berdasarkan kategori
- Menampilkan summary data valid dan error
- Menyimpan log data error

---

# 📂 Struktur Folder

```text
expense_project/
│
├── main.py
│
├── models/
│   ├── expenseRecord.py
│   └── expenseTracker.py
│
├── services/
│   ├── cleaner.py
│   ├── reader.py
│   └── processor.py
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

---

### Attribute

| Attribute | Fungsi |
| --- | --- |
| tanggal | Menyimpan tanggal transaksi |
| amount | Menyimpan nominal pengeluaran |
| kategori | Menyimpan kategori pengeluaran |
| status | Menyimpan status data (OK / ERROR) |

---

### Method

| Method | Fungsi |
| --- | --- |
| is_valid() | Mengecek apakah data valid |
| is_invalid() | Mengecek apakah data error |

---

## 2. ExpenseTracker

Class ini digunakan sebagai manager utama dataset pengeluaran.

Class ini bertanggung jawab untuk:
- membaca data CSV
- menyimpan seluruh object expense
- menyimpan log error
- mengelola proses data
- menampilkan output program

---

### Attribute

| Attribute | Fungsi |
| --- | --- |
| self.records | Menyimpan list object ExpenseRecord |
| self.error_logs | Menyimpan list data error |

---

### Method

| Method | Fungsi |
| --- | --- |
| load_csv() | Membaca file CSV |
| get_total() | Menghitung total seluruh pengeluaran |
| get_by_category() | Mengambil total pengeluaran per kategori |
| show_error_data() | Menampilkan data error |
| show_summary() | Menampilkan summary data |
| show_total_per_kategori() | Menampilkan total kategori |

---

# 🧹 Penjelasan Services

Folder `services/` digunakan untuk memisahkan business logic program agar code lebih modular dan mudah dikelola.

---

## 1. cleaner.py

Digunakan untuk:
- membersihkan data
- validasi amount
- menangani data invalid

Function utama:

```python
clean_row()
```

---

## 2. reader.py

Digunakan untuk:
- membaca file CSV
- mengubah data CSV menjadi list dictionary

Function utama:

```python
read_csv()
```

Menggunakan library:

```python
csv.DictReader()
```

---

## 3. processor.py

Digunakan untuk:
- menghitung total pengeluaran per kategori

Function utama:

```python
process_total_per_kategori()
```

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

Program membaca file CSV melalui:

```python
reader.py
```

Function:

```python
read_csv()
```

---

## 2. Clean & Validate

Data dibersihkan menggunakan:

```python
clean_row()
```

Validasi dilakukan pada:
- amount kosong
- amount invalid
- format angka

---

## 3. Store

Data yang sudah diproses disimpan ke:

```python
self.records
```

Sedangkan data error disimpan ke:

```python
self.error_logs
```

---

## 4. Process

Program melakukan:
- menghitung total pengeluaran
- menghitung total per kategori
- menghitung jumlah data valid dan error

Proses kategori dilakukan melalui:

```python
processor.py
```

---

## 5. Output

Program menampilkan:
- data error
- summary data
- total pengeluaran per kategori
- total keseluruhan pengeluaran

---

# 🛡️ Error Handling

Program menggunakan:

```python
try-except
```

Tujuannya agar:
- program tidak crash
- data invalid tetap bisa diproses
- error dapat dicatat ke dalam `error_logs`

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

TOTAL SELURUH PENGELUARAN:
Rp 85.000
```

---

# ✅ Keunggulan Program

- Menggunakan OOP
- Menggunakan modular programming
- Memiliki error handling
- Tidak crash saat data kotor ditemukan
- Memiliki pemisahan responsibility per module
- Memiliki error log system
- Struktur code lebih rapih dan scalable

---

# ⚠️ Kekurangan Program

- Validasi tanggal masih sederhana
- Belum export hasil cleaning ke CSV baru
- Tampilan output masih console text
- Belum menggunakan database
- Error message masih sederhana

---

# 🚀 Pengembangan Selanjutnya

Program masih dapat dikembangkan menjadi:
- GUI/Desktop Application
- Dashboard visualisasi data
- Export Excel/CSV hasil cleaning
- Database integration
- Web application
- Filtering dan sorting data
- Statistik pengeluaran bulanan

---

# 👨‍💻 Teknologi yang Digunakan

- Python 3
- CSV Module
- Object-Oriented Programming (OOP)
- Modular Programming

---

# 📌 Kesimpulan

Program berhasil membaca dan membersihkan data expense yang kotor menggunakan pendekatan OOP dan modular programming.

Program mampu:
- menangani data invalid tanpa crash
- menyimpan log error
- menghitung total pengeluaran
- mengelompokkan data berdasarkan kategori

Pemisahan logic ke dalam folder `services/` membuat program lebih modular, rapih, scalable, dan mudah dikembangkan untuk kebutuhan yang lebih kompleks di masa depan.
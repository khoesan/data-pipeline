# 🏛 Submission Pemda - Data Pipeline ke Google Sheets

Proyek ini membangun sebuah *data pipeline* sederhana untuk mengolah data dari file CSV (`products.csv`) dan mengunggahnya ke Google Sheets secara otomatis menggunakan Google Sheets API. 

Pipeline terdiri dari tiga tahap utama: **extract**, **transform**, dan **load** (ETL). Proyek ini juga dilengkapi dengan **unit testing** dan **test coverage**.

---

## 📁 Struktur Direktori

```

submission-pemda/
│
├── main.py                        # Script utama untuk menjalankan pipeline ETL
├── products.csv                   # File CSV sebagai sumber data
├── google-sheets-api.json        # Kredensial Google Sheets API (service account)
├── requirements.txt              # File dependency
│
├── utils/                         # Modul ETL
│   ├── extract.py                 # Fungsi untuk membaca file CSV
│   ├── transform.py               # Fungsi untuk membersihkan & memformat data
│   └── load.py                    # Fungsi untuk mengunggah data ke Google Sheets
│
├── tests/                         # Unit test untuk masing-masing modul
│   ├── test\_extract.py
│   ├── test\_transform.py
│   └── test\_load.py
│
├── submission.txt                 # Instruksi teknis (cara menjalankan skrip)
└── .coverage                      # Hasil pengukuran test coverage

````

---

## ⚙️ Instalasi

1. **Clone repo ini** (jika belum):
   ```bash
   git clone <url-repo>
   cd submission-pemda
    ````

2. **Buat virtual environment & aktifkan**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # Untuk Linux/macOS
   venv\Scripts\activate           # Untuk Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Menjalankan Pipeline

Jalankan pipeline lengkap (Extract → Transform → Load):

```bash
python main.py
```

Pastikan file `products.csv` dan `google-sheets-api.json` sudah tersedia di direktori proyek.

---

## 🧪 Menjalankan Unit Test

Proyek ini menggunakan `unittest` untuk pengujian fungsionalitas:

```bash
python -m unittest discover tests
```

Untuk mengukur **test coverage**:

```bash
coverage run -m unittest discover tests
coverage report -m
```

---

## 🔗 Integrasi Google Sheets

Hasil akhir dari data akan diunggah ke Google Sheets melalui service account. Link Google Sheet tujuan:
[🔗 Google Spreadsheet](https://docs.google.com/spreadsheets/d/14BctMkMRHxLgnYDMkaDFx9ccGVFI92pbeKbBu34kpCw/edit?gid=0)

> ⚠️ Pastikan spreadsheet tersebut telah dibagikan ke email dari service account Anda (yang terdapat di file `google-sheets-api.json`).

---

## 🛠 Penjelasan Modul

* `extract.py`: Membaca data mentah dari file CSV ke dalam struktur dataframe.
* `transform.py`: Membersihkan, memfilter, atau memformat data sesuai kebutuhan (misal: menghapus kolom kosong, konversi tipe data).
* `load.py`: Mengunggah data hasil transformasi ke Google Sheets menggunakan `gspread`.

---

## 📝 Catatan

* Untuk menggunakan service account Google Sheets, ikuti panduan resmi [di sini](https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account).

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan submission internal. Tidak untuk penggunaan komersial tanpa izin.

```

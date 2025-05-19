# 🏛 ETL Pipeline Sederhana dari Web Scraping ke Repositori Data

Proyek ini membangun sebuah *data pipeline* sederhana yang dimulai dari proses **web scraping** data produk dari sebuah website, dilanjutkan dengan tahap pembersihan data, dan akhirnya memuat data ke dua repositori: file **CSV** (`products.csv`) dan **Google Sheets** menggunakan Google Sheets API.

Pipeline mengikuti tiga tahap utama dalam proses **ETL (Extract - Transform - Load)**. Proyek ini juga dilengkapi dengan **unit testing** serta **test coverage** untuk memastikan setiap komponen berjalan dengan baik.

---

## 📁 Struktur Direktori

```
submission-pemda/
│
├── main.py                        # Script utama untuk menjalankan pipeline ETL
├── products.csv                   # File output CSV hasil akhir data
├── google-sheets-api.json        # Kredensial Google Sheets API (service account)
├── requirements.txt              # Daftar dependensi Python
│
├── utils/                         # Modul ETL
│   ├── extract.py                 # Scraping data dari website
│   ├── transform.py              # Membersihkan & memformat data hasil scraping
│   └── load.py                   # Menyimpan data ke CSV & mengunggah ke Google Sheets
│
├── tests/                         # Unit test untuk masing-masing modul
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── submission.txt                 # Instruksi teknis (cara menjalankan skrip)
└── .coverage                      # File hasil test coverage

```

---

## ⚙️ Instalasi

1. **Clone repo ini**:

   ```bash
   git clone <url-repo>
   cd submission-pemda
   ```

2. **Buat dan aktifkan virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Menjalankan Pipeline

Jalankan pipeline ETL lengkap (Web Scraping → Data Cleaning → Load ke CSV & Google Sheets):

```bash
python main.py
```

Pastikan kredensial `google-sheets-api.json` tersedia di direktori root proyek.

---

## 🧪 Menjalankan Unit Test

Proyek menggunakan `unittest` untuk pengujian fungsi:

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

Hasil data akhir akan diunggah secara otomatis ke Google Sheets melalui service account. Link spreadsheet tujuan:

[🔗 Google Spreadsheet](https://docs.google.com/spreadsheets/d/14BctMkMRHxLgnYDMkaDFx9ccGVFI92pbeKbBu34kpCw/edit?gid=0)

---

## 🛠 Penjelasan Modul

* `extract.py`: Scrapes data dari website dan mengubahnya menjadi dataframe.
* `transform.py`: Membersihkan, memfilter, atau memformat data sesuai kebutuhan (misal: normalisasi nama kolom, konversi tipe data, penghapusan entri kosong).
* `load.py`: Menyimpan hasil transformasi ke `products.csv` dan mengunggahnya ke Google Sheets menggunakan `gspread`.

---

## 📝 Catatan

* Untuk menggunakan service account Google Sheets, ikuti panduan resmi [di sini](https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account).
* Beberapa situs dapat memiliki mekanisme anti-scraping. Pastikan penggunaan data tetap sesuai dengan kebijakan mereka.

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan submission internal. Tidak untuk penggunaan komersial tanpa izin.

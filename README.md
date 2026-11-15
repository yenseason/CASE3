# Dashboard Visualisasi Data Cuaca — CASE3

## Identitas Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama | Neysalva Calista Firlin |
| NPM | 241051005 |
| Mata Kuliah | Visualisasi Data |
| Program Studi | Sistem Informasi |

## 1. Deskripsi Proyek

CASE3 merupakan proyek visualisasi data yang berfokus pada pengolahan dan penyajian data cuaca menggunakan Python. Proyek ini dikembangkan dengan memanfaatkan Streamlit sebagai framework untuk membangun dashboard interaktif.

Dashboard ini bertujuan untuk menyajikan informasi cuaca dalam bentuk visualisasi yang lebih informatif dan mudah dipahami. Melalui pengolahan dataset cuaca, pengguna dapat mengamati informasi serta pola yang terdapat dalam data melalui tampilan dashboard.

## 2. Latar Belakang

Data cuaca merupakan salah satu jenis data yang dapat memberikan informasi mengenai kondisi lingkungan dalam periode tertentu. Data tersebut dapat digunakan untuk memahami perubahan dan pola kondisi cuaca berdasarkan informasi yang tersedia.

Namun, data yang disajikan hanya dalam bentuk tabel terkadang sulit dipahami, terutama ketika jumlah data cukup banyak. Oleh karena itu, diperlukan visualisasi data untuk menyajikan informasi secara lebih terstruktur dan menarik.

Melalui proyek CASE3, data cuaca diolah dan disajikan dalam dashboard interaktif sehingga informasi di dalam dataset dapat diamati dengan lebih mudah melalui berbagai bentuk visualisasi.

## 3. Tujuan Proyek

- Melakukan pengolahan dan analisis terhadap dataset cuaca.
- Menyajikan informasi cuaca dalam bentuk visualisasi data.
- Mempermudah pemahaman terhadap informasi yang terdapat dalam dataset.
- Mengamati pola dan perubahan data cuaca berdasarkan informasi yang tersedia.
- Mengembangkan dashboard interaktif sebagai media penyajian hasil analisis.
- Menerapkan penggunaan Python dan berbagai library untuk pengolahan serta visualisasi data.

## 4. Visualisasi yang Digunakan

Visualisasi dalam dashboard CASE3 digunakan untuk membantu pengguna memahami informasi cuaca melalui penyajian grafis.

Bentuk visualisasi yang digunakan mengikuti variabel dan pengolahan data pada aplikasi, dengan tujuan untuk:

1. **Visualisasi Data Cuaca**  
   Menampilkan informasi variabel cuaca dalam bentuk grafik agar data lebih mudah diamati.

2. **Perbandingan Data Cuaca**  
   Membantu melihat perbedaan nilai antarvariabel atau kelompok data yang tersedia.

3. **Pola Perubahan Data**  
   Menyajikan perubahan informasi cuaca berdasarkan urutan atau periode data apabila tersedia.

4. **Ringkasan Statistik**  
   Menampilkan gambaran umum dataset sebagai informasi pendukung proses analisis.

## 5. Fitur Dashboard

Dashboard CASE3 dikembangkan untuk menyajikan informasi cuaca melalui beberapa fitur utama, yaitu:

- **Tampilan Data Cuaca:** Menyajikan informasi dari dataset cuaca yang digunakan.
- **Ringkasan Data:** Memberikan gambaran umum mengenai data yang dianalisis.
- **Visualisasi Grafis:** Menampilkan data dalam bentuk grafik agar informasi lebih mudah dipahami.
- **Analisis Data:** Membantu pengguna mengamati pola dan karakteristik data cuaca.
- **Dashboard Interaktif:** Menyediakan tampilan visualisasi yang dapat digunakan untuk mengeksplorasi informasi pada dataset.

## 6. Hasil Analisis Awal

Analisis awal pada proyek CASE3 dilakukan menggunakan dataset `dataset_cuaca.csv` sebagai sumber utama pengolahan data.

Dataset tersebut digunakan untuk mengamati informasi dan karakteristik data cuaca melalui proses analisis menggunakan Python dan Pandas.

Hasil pengolahan kemudian disajikan melalui visualisasi pada dashboard Streamlit agar informasi yang terdapat dalam dataset dapat dipahami secara lebih terstruktur.

Analisis lebih lanjut dilakukan dengan mengamati pola, perbandingan, serta perubahan nilai pada variabel cuaca yang tersedia dalam dataset.

## 7. Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman untuk pengolahan data dan pengembangan aplikasi |
| Jupyter Notebook | Lingkungan untuk melakukan analisis data |
| Pandas | Mengolah dan memanipulasi dataset |
| Streamlit | Membangun dashboard interaktif |
| Plotly | Membuat visualisasi data interaktif |
| Git | Mengelola versi proyek |
| GitHub | Menyimpan dan membagikan source code proyek |

## 8. Live Dashboard

Dashboard CASE3 dikembangkan menggunakan Streamlit Community Cloud agar dapat diakses secara online.

**Link Dashboard:** https://case3-dashboard-cuaca-yenseason.streamlit.app/

## 9. Struktur Folder

```text
CASE3/
│
├── analisis_data.ipynb
├── app.py
├── dataset_cuaca.csv
├── requirements.txt
└── README.md
```

Keterangan:
- `analisis_data.ipynb` : File notebook untuk proses analisis dan pengolahan data cuaca.
- `app.py` : File utama untuk menjalankan aplikasi dashboard Streamlit.
- `dataset_cuaca.csv` : Dataset yang digunakan dalam analisis data cuaca.
- `requirements.txt` : Daftar library Python yang diperlukan.
- `README.md` : Dokumentasi proyek.

## 10. Cara Menjalankan Secara Lokal

Untuk menjalankan dashboard CASE3 pada komputer lokal, ikuti langkah berikut:

**1. Clone repository GitHub**

```bash
git clone https://github.com/yenseason/CASE3.git
```

**2. Masuk ke direktori proyek**

```bash
cd CASE3
```

**3. Install seluruh library yang dibutuhkan**

```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi Streamlit**

```bash
streamlit run app.py
```

**5. Buka dashboard**

Setelah aplikasi berjalan, buka alamat lokal yang ditampilkan pada terminal, biasanya:

```text
http://localhost:8501
```

## 11. Repository GitHub

Source code dan seluruh file proyek CASE3 dapat diakses melalui repository berikut:

https://github.com/yenseason/CASE3

# Kumpulan Proyek Coding Camp

Repositori ini berisi kumpulan proyek dan submission yang diselesaikan sebagai bagian dari program Coding Camp oleh **Hussain Tamam Gucci Al Fauzan**. Setiap folder mewakili submission untuk kelas atau kursus yang berbeda, yang mencakup berbagai topik mulai dari analisis data hingga machine learning.

## Daftar Isi
1.  [Belajar Analisis Data dengan Python](#1-belajar-analisis-data-dengan-python)
2.  [Belajar Fundamental Pemrosesan Data](#2-belajar-fundamental-pemrosesan-data)
3.  [Belajar Machine Learning untuk Pemula](#3-belajar-machine-learning-untuk-pemula)
4.  [Belajar Machine Learning Terapan](#4-belajar-machine-learning-terapan)
5.  [Belajar Machine Learning Lanjutan](#5-belajar-machine-learning-lanjutan)
6.  [Capstone Project](#6-capstone-project)

---

### 1. Belajar Analisis Data dengan Python

Proyek ini berfokus pada analisis data set *Bike Sharing*. Tujuannya adalah untuk melakukan eksplorasi data, menjawab pertanyaan bisnis, dan membuat visualisasi data interaktif menggunakan Streamlit.

-   **Lokasi:** `Belajar Analisis Data dengan Python/`
-   **Notebook Analisis:** `notebook.ipynb`
-   **Dashboard:** `dashboard/dashboard.py`
-   **Data:** `data/day.csv`, `data/hour.csv`

### 2. Belajar Fundamental Pemrosesan Data

Submission ini menunjukkan pemahaman tentang proses Extract, Transform, Load (ETL) fundamental.

-   **Lokasi:** `Belajar Fundamental Pemrosesan Data/`
-   **Logika Utama:** `main.py`
-   **Fungsi ETL:**
    -   `utils/extract.py`
    -   `utils/transform.py`
    -   `utils/load.py`

### 3. Belajar Machine Learning untuk Pemula

Folder ini berisi dua proyek machine learning tingkat pemula.

-   **Lokasi:** `Belajar Machine Learning untuk Pemula/`
-   **Proyek 1: Klasifikasi**
    -   **Notebook:** `[Klasifikasi]_Submission_Akhir_BMLP_Hussain_Tamam_Guci_Al_Fauzan.ipynb`
-   **Proyek 2: Clustering**
    -   **Notebook:** `[Clustering]_Submission_Akhir_BMLP_Hussain_Tamam_Gucci_Al_Fauzan.ipynb`

### 4. Belajar Machine Learning Terapan

Berisi dua proyek machine learning terapan, lengkap dengan laporan proyek.

-   **Lokasi:** `Belajar Machine Learning Terapan/`
-   **Submission 1:**
    -   **Notebook:** `submisi-satu/notebook.ipynb`
    -   **Laporan:** `submisi-satu/laporan_proyek-satu_Hussain.md`
-   **Submission 2 (Akhir):**
    -   **Notebook:** `submisi-akhir/submisi_akhir.ipynb`
    -   **Laporan:** `submisi-akhir/laporan_submission_2_hussain.md`

### 5. Belajar Machine Learning Lanjutan

Submission untuk kelas machine learning lanjutan yang mencakup analisis sentimen dan proyek akhir dengan model yang diekspor.

-   **Lokasi:** `Belajar Machine Learning Lanjutan/`
-   **Submission 1: Analisis Sentimen**
    -   **Deskripsi:** Melakukan scraping dan analisis sentimen pada ulasan game *Kingdom Two Crowns*.
    -   **Notebook:** `submisi-pertama/[Analisis Sentimen]Pelatihan_Proyek_Hussain Tamam Gucci Al Fauzan.ipynb`
-   **Submission Final:**
    -   **Deskripsi:** Proyek akhir dengan model yang disimpan dalam format TFLite dan TFJS.
    -   **Notebook:** `submisi-final/notebook.ipynb`
    -   **Model:** `submisi-final/tflite/` dan `submisi-final/tfjs_model/`

### 6. Capstone Project

Proyek puncak dari program ini, yang berfokus pada pemodelan untuk prediksi stunting.

-   **Lokasi:** `Capstone Project/`
-   **Notebook:** `modelstunting.ipynb`

---

## Cara Menjalankan Proyek

Setiap folder proyek bersifat mandiri. Untuk menjalankan salah satu proyek:
1.  Masuk ke direktori proyek yang diinginkan.
    ```bash
    cd "Belajar Analisis Data dengan Python"
    ```
2.  Jika tersedia, instal dependensi yang diperlukan menggunakan file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
3.  Buka file notebook (`.ipynb`) menggunakan Jupyter Notebook/Lab atau jalankan skrip Python yang relevan. Untuk dashboard Streamlit, gunakan perintah:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

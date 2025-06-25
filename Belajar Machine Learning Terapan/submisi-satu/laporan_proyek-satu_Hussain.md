# Laporan Proyek Machine Learning - Prediksi Penjualan Global Game

## Domain Proyek

Industri video game merupakan sektor hiburan yang berkembang pesat secara global. Penjualan game dipengaruhi banyak faktor seperti platform, genre, publisher, hingga preferensi regional. Dengan meningkatnya biaya produksi dan kompetisi yang ketat, prediksi penjualan menjadi sangat penting untuk perencanaan strategi bisnis.

Melalui pendekatan machine learning, kita dapat membangun model prediktif berbasis data historis yang membantu publisher mengestimasi potensi penjualan sebelum game dirilis.

## Business Understanding

### Problem Statements

1. Bagaimana memprediksi penjualan global (`Global_Sales`) game berdasarkan fitur historis seperti genre, platform, publisher, dan penjualan wilayah?
2. Fitur apa yang paling mempengaruhi `Global_Sales`?

### Goals

1. Membangun model prediktif untuk memperkirakan `Global_Sales`.
2. Mengidentifikasi fitur-fitur penting yang mempengaruhi penjualan global.

### Solution Statements

- Tiga algoritma digunakan:
  - **Linear Regression** (baseline)
  - **Random Forest Regressor**
  - **XGBoost Regressor**
- Hyperparameter tuning dengan **GridSearchCV**
- Metrik evaluasi: **MAE**, **RMSE**, dan **R²**

## Data Understanding

**Sumber Data:**

- [https://www.kaggle.com/datasets/gregorut/videogamesales](https://www.kaggle.com/datasets/gregorut/videogamesales)

### Informasi Dataset:

- **Jumlah Data**: 16.598 baris, 11 kolom
- **Jumlah Setelah Pembersihan Missing Values**: 16.269 baris (271 baris tanpa `Year`, 58 baris tanpa `Publisher` dihapus)
- **Fitur:**
  - `Rank`: Peringkat berdasarkan penjualan (tidak digunakan dalam model)
  - `Name`: Nama game (tidak digunakan dalam model)
  - `Platform`: Platform rilis (PS4, Xbox, dll.)
  - `Year`: Tahun rilis
  - `Genre`: Jenis game
  - `Publisher`: Penerbit
  - `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`: Penjualan regional (dalam juta unit)
  - `Global_Sales`: Penjualan global (target)

### Kondisi Data:

- **Missing Values**:
  - `Year`: 271 baris hilang
  - `Publisher`: 58 baris hilang
  - Solusi: baris-baris tersebut dihapus
- **Duplikat**: Tidak ditemukan setelah dicek dengan `df.duplicated().sum()`
- **Outlier**:
  - Ditemukan outlier signifikan pada kolom `Global_Sales` dan penjualan regional yakni `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`
  - Distribusi sangat skewed → ditangani dengan **log-transformasi (`log1p`)**

## Data Preparation

### Tahapan yang dilakukan:

1. **Handling Missing Values**:

- Kolom `Year` memiliki 271 nilai kosong, dan `Publisher` memiliki 58 nilai kosong.
- Karena kedua kolom ini penting untuk fitur prediktif dan datanya bersifat kategorikal/numerik, baris yang memiliki nilai kosong dihapus.
- **Jumlah data setelah penghapusan missing values**: 16.269 baris.

2. **Encoding**:
   - `Genre` dan `Platform` diencoding menggunakan **One-Hot Encoding** karena jumlah kategorinya masih relatif sedikit dan tidak ordinal.

- `Publisher` memiliki jumlah kategori sangat banyak. Untuk menghindari high-dimensionality:
  - `Publisher` dengan jumlah game < 150 digabung ke kategori `'Other'`.
  - Menghasilkan 23 Pubsliher tersisa
  - Setelah itu, dilakukan One-Hot Encoding terhadap `Publisher`

3. **Drop Kolom Tak Relevan**:

- Kolom `Name` dan `Rank` tidak memberikan informasi prediktif yang berguna untuk model regresi.
- Kedua kolom tersebut dihapus dari dataset. **setelah proses encoding selesai**.

4. **Log Transformasi**:

- Fitur `Global_Sales`, `NA_Sales`, `EU_Sales`, `JP_Sales`, dan `Other_Sales` memiliki distribusi sangat skewed dengan banyak outlier.
- Untuk menormalkan distribusi dan meningkatkan performa model regresi, dilakukan **log-transformasi** menggunakan `np.log1p`.
- Hasil log-transformasi **tidak menimpa data asli**, tetapi disimpan dalam kolom baru: `Log_Global_Sales`, `Log_NA_Sales`, `Log_EU_Sales`, `Log_JP_Sales`, dan `Log_Other_Sales`.
- Target variabel `Global_Sales` juga ditransformasi dan disimpan dalam `Log_Global_Sales` sebagai target model.

5. **Scaling**:

- Fitur numerik seperti `Year` dan kolom penjualan hasil log-transformasi (selain target) distandarisasi menggunakan **StandardScaler**.
- Ini penting terutama untuk algoritma seperti Linear Regression yang sensitif terhadap skala fitur.

6. **Train-Test Split**:

- Data dibagi menjadi **training set dan test set** dengan rasio **70:30**.
- **Alasan pemilihan rasio**:
  - Dataset memiliki ukuran cukup besar (>16.000 baris), sehingga 30% untuk test set masih merepresentasikan populasi dengan baik.
  - Rasio ini juga umum digunakan untuk mencapai keseimbangan antara pelatihan dan evaluasi model.

## Model Development

### Penjelasan Model dan Alasan Pemilihan

#### 1. **Linear Regression**

- **Definisi**: Linear Regression adalah algoritma regresi yang mencoba memodelkan hubungan antara satu atau lebih fitur independen dengan target dependen menggunakan garis lurus.
- **Cara Kerja**:

  - Model mencari kombinasi koefisien (bobot) terbaik yang meminimalkan _residual sum of squares_ (selisih antara nilai prediksi dan nilai aktual).
  - Rumus dasar: `y = β0 + β1x1 + β2x2 + ... + βnxn`
  - Estimasi koefisien dilakukan dengan metode OLS (Ordinary Least Squares).

- **Alasan Pemilihan**:

  - Digunakan sebagai baseline sederhana.
  - Mudah diinterpretasi dan dilatih dengan cepat.
  - Dapat menjadi pembanding awal sebelum menggunakan model kompleks.

- **Parameter**:
  - Tidak dilakukan tuning karena model ini digunakan sebagai baseline.
  - Default parameter dari `sklearn.linear_model.LinearRegression` digunakan.

#### 2. **Random Forest Regressor**

- **Definisi**: Random Forest adalah algoritma ensemble learning yang membangun banyak pohon keputusan (decision trees) dan menggabungkan prediksi mereka untuk meningkatkan akurasi.
- **Cara Kerja**:
  - Model membuat banyak decision tree dari subset data berbeda.
  - Untuk regresi, hasil prediksi adalah **rata-rata** dari semua pohon.
  - Mengurangi overfitting dengan mengacak fitur dan sampel.
  - Tahan terhadap noise dan outlier karena penggabungan banyak model.
- **Alasan Pemilihan**:

  - Cocok untuk data non-linear dan dengan interaksi fitur kompleks.
  - Tidak memerlukan scaling dan relatif robust terhadap outlier.
  - Bias rendah dan varians dikendalikan oleh averaging.

- **Parameter Awal**: Default dari `RandomForestRegressor` (sklearn)
- **Tuning**: Dilakukan menggunakan `GridSearchCV` dengan ruang pencarian terbatas
- **Best Parameters (hasil tuning)**:
  ```python
  {'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 200}
  ```
  - `max_depth = 20`: Membatasi kedalaman setiap pohon untuk mencegah overfitting dan menjaga keseimbangan antara kompleksitas dan generalisasi.
  - `min_samples_split = 2`: Jumlah minimum sampel untuk membagi sebuah node. Nilai kecil memperbolehkan lebih banyak pembelahan dan menangkap kompleksitas data.
  - `n_estimators = 200`: Jumlah pohon dalam hutan. Semakin banyak pohon, hasil prediksi semakin stabil. 200 dipilih sebagai jumlah optimal berdasarkan uji coba.

#### 3. **XGBoost Regressor**

- **Definisi**: XGBoost (Extreme Gradient Boosting) adalah algoritma boosting yang dioptimalkan untuk efisiensi, kecepatan, dan performa, serta mendukung regularisasi untuk mencegah overfitting.
- **Cara Kerja**:

  - Model pertama membuat prediksi sederhana terhadap target.
  - Model berikutnya dilatih untuk memprediksi _residuals_ (selisih prediksi sebelumnya dengan nilai aktual).
  - Proses diulang hingga jumlah pohon terpenuhi atau error minimal tercapai.
  - XGBoost juga mendukung teknik pruning, early stopping, dan regularisasi L1/L2 untuk menghindari overfitting.

- **Alasan Pemilihan**:

  - Memberikan performa tinggi, efisien, dan telah terbukti unggul di banyak kompetisi machine learning.
  - Dapat menangani data dengan fitur non-linear dan missing values ringan.
  - Dilengkapi regularisasi untuk mengontrol kompleksitas model.

- **Parameter Awal**: Default dari `XGBRegressor` (xgboost)
- **Tuning**: Dilakukan menggunakan `GridSearchCV` dengan ruang pencarian terbatas
- **Best Params (hasil tuning)**:
  ```python
  {'learning_rate': 0.2, 'max_depth': 3, 'n_estimators': 200}
  ```
  - `learning_rate = 0.2`: Mengontrol seberapa besar kontribusi tiap pohon baru terhadap model akhir. Nilai ini lebih cepat dari default (0.1) dan masih stabil.
  - `max_depth = 3`: Membatasi kedalaman setiap pohon. Nilai kecil seperti 3 membantu menghindari overfitting.
  - `n_estimators = 200`: Jumlah pohon yang dibangun secara berurutan. Jumlah ini dinilai cukup untuk mencapai konvergensi tanpa terlalu lama waktu komputasi.

## Evaluation

### Hasil Evaluasi:

| Model             | MAE    | RMSE   | R²     |
| ----------------- | ------ | ------ | ------ |
| XGBoost           | 0.0431 | 0.5344 | 0.8404 |
| Random Forest     | 0.0397 | 0.5653 | 0.8311 |
| Linear Regression | 0.0994 | 1.5952 | 0.5234 |

### Interpretasi Bisnis:

Model yang dibangun telah mampu menjawab problem statements yang diajukan. Model berhasil memprediksi `Global_Sales` dengan tingkat akurasi yang tinggi, seperti tercermin dari nilai R² yang mencapai 0.84 pada model XGBoost. Ini menunjukkan bahwa model dapat menangkap pola dari data historis dengan baik, menjawab pertanyaan bagaimana cara memprediksi penjualan berdasarkan atribut seperti genre, platform, dan publisher.

Dari sisi goals, model tidak hanya memberikan prediksi yang akurat, tetapi juga mampu mengidentifikasi fitur-fitur yang paling berpengaruh terhadap total penjualan sebuah game. Ini selaras dengan tujuan awal proyek untuk memahami faktor-faktor penting yang berdampak besar terhadap performa game secara global.

Secara bisnis, keberadaan model ini memberikan dampak signifikan. Publisher atau developer dapat menggunakannya untuk merancang strategi pengembangan dan pemasaran game secara lebih terarah. Dalam skala besar, model ini dapat menjadi alat bantu pengambilan keputusan, seperti menentukan genre atau platform yang potensial, memilih wilayah pasar dengan potensi penjualan tinggi, hingga mengoptimalkan anggaran marketing. Singkatnya, model ini bisa menjadi gambaran menyeluruh bagi pengembang dalam merancang game dengan memperhatikan berbagai faktor penting, serta dalam menentukan wilayah rilis dan strategi promosi yang tepat.

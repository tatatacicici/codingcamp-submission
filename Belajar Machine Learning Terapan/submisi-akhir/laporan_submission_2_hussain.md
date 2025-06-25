# Laporan Proyek Machine Learning - Sistem Rekomendasi Anime - Hussain Tamam Gucci Al Fauzan

## Project Overview

Industri anime global terus menunjukkan pertumbuhan yang signifikan, dengan peningkatan jumlah produksi dan platform distribusi digital yang semakin memudahkan akses bagi penggemar di seluruh dunia. Data dari Association of Japanese Animations (AJA) menunjukkan bahwa pasar anime global mencapai nilai triliunan yen dan terus berekspansi (AJA, 2023). Dengan ribuan judul anime yang tersedia, mulai dari serial TV, film, OVA (Original Video Animation), hingga ONA (Original Net Animation), pengguna seringkali dihadapkan pada tantangan untuk menemukan konten baru yang benar-benar sesuai dengan preferensi individual mereka. Fenomena ini dikenal sebagai _information overload_, di mana banyaknya pilihan justru dapat mengurangi kepuasan pengguna jika tidak ada mekanisme penyaringan yang efektif (Park et al., 2012).

Proyek ini bertujuan untuk mengatasi masalah tersebut dengan mengembangkan sistem rekomendasi anime. Sistem rekomendasi yang baik tidak hanya membantu pengguna menemukan anime yang relevan dengan lebih efisien, tetapi juga dapat meningkatkan _engagement_ pengguna pada platform, mendorong eksplorasi konten yang lebih luas, dan pada akhirnya memberikan nilai tambah bagi penyedia layanan. Dengan menerapkan dua pendekatan utama, yaitu _content-based filtering_ dan _collaborative filtering_, diharapkan sistem ini dapat memberikan rekomendasi yang beragam dan akurat.

Pentingnya penyelesaian masalah ini didasari oleh kebutuhan pengguna akan pengalaman menonton yang lebih personal dan efisien. Dalam konteks bisnis, sistem rekomendasi yang efektif dapat menjadi pembeda kompetitif yang signifikan bagi platform streaming atau basis data anime, meningkatkan retensi pengguna, dan mendorong konsumsi konten (Gomez-Uribe & Hunt, 2016).

**Referensi:**

- Association of Japanese Animations (AJA). (2023). _Anime Industry Report_.
- Park, D. H., Kim, H. K., Choi, I. Y., & Kim, J. K. (2012). A literature review and classification of recommender systems research. _Expert Systems with Applications, 39_(11), 10059-10072.
- Gomez-Uribe, C. A., & Hunt, N. (2016). The Netflix Recommender System: Algorithms, Business Value, and Innovation. _ACM Transactions on Management Information Systems (TMIS), 6_(4), 1-19.
- Aggarwal, C. C. (2016). _Recommender Systems: The Textbook_. Springer.
- Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: Introduction and challenges. In _Recommender Systems Handbook_ (pp. 1-34). Springer.

---

## Business Understanding

Proses klarifikasi masalah dalam pengembangan sistem rekomendasi anime ini melibatkan identifikasi tantangan yang dihadapi pengguna dan tujuan yang ingin dicapai melalui solusi yang diajukan.

### Problem Statements

1.  **Kesulitan Penemuan Konten:** Pengguna seringkali merasa kewalahan dengan banyaknya pilihan anime dan kesulitan menemukan judul baru yang sesuai dengan selera spesifik mereka, terutama di luar judul-judul yang sudah sangat populer.
2.  **Rekomendasi Kurang Personal:** Rekomendasi yang bersifat umum atau hanya berdasarkan popularitas seringkali kurang relevan bagi preferensi unik setiap individu.
3.  **Masalah _Cold Start_:** Bagaimana memberikan rekomendasi yang berarti bagi pengguna baru yang belum memiliki riwayat tontonan atau rating, dan bagaimana merekomendasikan anime baru yang belum banyak mendapatkan interaksi dari pengguna?

### Goals

1.  **Meningkatkan Kepuasan Pengguna:** Menyediakan rekomendasi anime yang lebih personal dan relevan sehingga meningkatkan kepuasan pengguna dalam menemukan konten baru.
2.  **Meningkatkan _Engagement_ Pengguna:** Mendorong pengguna untuk mengeksplorasi lebih banyak anime dan menghabiskan lebih banyak waktu pada platform melalui saran yang menarik.
3.  **Menyediakan Solusi Rekomendasi Komprehensif:** Mengimplementasikan dua pendekatan rekomendasi (Content-Based dan Collaborative Filtering) untuk mencakup berbagai skenario, termasuk penanganan masalah _cold start_ secara parsial.
4.  **Mengevaluasi Efektivitas Model:** Mengukur kinerja model rekomendasi yang dibangun menggunakan metrik evaluasi yang sesuai untuk memastikan kualitas dan relevansi rekomendasi yang diberikan.

### Solution Approach

Untuk mencapai tujuan-tujuan tersebut, dua pendekatan utama dalam sistem rekomendasi akan diimplementasikan:

1.  **Content-Based Filtering:**

    - **Alasan Pemilihan:** Pendekatan ini dipilih karena kemampuannya untuk merekomendasikan item berdasarkan atribut intrinsiknya (misalnya, genre, tipe). Ini sangat berguna untuk mengatasi masalah _cold start_ pada item baru (anime baru bisa direkomendasikan selama fiturnya diketahui) dan dapat memberikan rekomendasi yang transparan (mudah dijelaskan mengapa suatu item direkomendasikan). Selain itu, pendekatan ini tidak bergantung pada data rating dari pengguna lain.
    - **Cara Kerja:** Sistem akan menganalisis fitur-fitur konten dari setiap anime, terutama genre. Anime akan direpresentasikan sebagai vektor fitur menggunakan teknik TF-IDF (_Term Frequency-Inverse Document Frequency_). Kemiripan antara dua anime kemudian dihitung menggunakan metrik _cosine similarity_ berdasarkan vektor fitur genre mereka. Anime yang memiliki profil genre paling mirip dengan anime yang disukai pengguna akan direkomendasikan.

2.  **Collaborative Filtering:**
    - **Alasan Pemilihan:** Pendekatan ini dipilih karena kemampuannya untuk menangkap preferensi implisit dan pola perilaku pengguna yang kompleks, yang mungkin tidak dapat ditangkap hanya dari fitur konten. _Collaborative filtering_ dapat menghasilkan rekomendasi yang lebih _serendipitous_ (mengejutkan namun relevan) dengan menemukan kesamaan antar pengguna atau antar item berdasarkan histori interaksi mereka.
    - **Cara Kerja (menggunakan LightFM):**
      - **LightFM (Light Factorization Machines)** adalah sebuah library Python untuk membuat model rekomendasi. LightFM sangat efisien dan dapat digunakan untuk data _feedback_ eksplisit (seperti rating 1-10) maupun implisit (seperti jumlah tontonan). Library ini mengimplementasikan beberapa model, termasuk model faktorisasi matriks yang dimodifikasi untuk menangani _sparsity_ data dan dapat dengan mudah diperluas menjadi model _hybrid_.
      - Pada intinya, LightFM (dalam konfigurasi yang digunakan di proyek ini) bekerja dengan mempelajari representasi vektor laten (embeddings) untuk setiap pengguna dan setiap item (anime) dari matriks interaksi pengguna-item. Matriks interaksi $R$ (dimana $R_{ui}$ adalah rating pengguna $u$ untuk item $i$) difaktorisasi menjadi dua matriks berdimensi lebih rendah: $P$ (matriks fitur laten pengguna) dan $Q$ (matriks fitur laten item), sehingga $R \approx P \times Q^T$.
      - Prediksi rating $\hat{r}_{ui}$ untuk pengguna $u$ dan item $i$ adalah hasil _dot product_ dari vektor laten mereka: $\hat{r}_{ui} = p_u \cdot q_i + b_u + b_i + b_{global}$, di mana $b_u$ dan $b_i$ adalah bias pengguna dan item, dan $b_{global}$ adalah bias global.
      - Model dilatih dengan mengoptimalkan _loss function_. Dalam proyek ini, digunakan _loss function_ **WARP (Weighted Approximate-Rank Pairwise)**. WARP loss bertujuan untuk membuat item positif (yang dirating tinggi/berinteraksi) mendapatkan ranking lebih tinggi daripada item negatif (yang belum dirating/dirating rendah). Loss function ini secara iteratif mengambil sampel pengguna $u$, item positif $i$ yang diketahui, dan item negatif $j$ (yang belum dirating oleh $u$). Jika item $j$ diprediksi memiliki skor lebih tinggi dari $i$ (ranking salah), model akan di-update. Loss-nya dapat dirumuskan secara konseptual sebagai:
        $L_{WARP} = \sum_{(u,i,j) \in D_S} f(rank_{ui}) \cdot \max(0, 1 - (\hat{x}_{ui} - \hat{x}_{uj}))$
        dimana $f(rank_{ui})$ adalah fungsi bobot yang menurun seiring dengan meningkatnya rank dari item positif $i$ (memberikan bobot lebih pada kesalahan ranking di posisi atas), dan $(\hat{x}_{ui} - \hat{x}_{uj})$ adalah perbedaan skor prediksi antara item positif dan item negatif. Tujuannya adalah untuk membuat $\hat{x}_{ui} > \hat{x}_{uj}$.
      - **Alasan Pemilihan Hyperparameter untuk LightFM:**
        - `no_components=50`: Jumlah dimensi laten. Nilai 50 dipilih sebagai titik awal yang umum, memberikan keseimbangan antara kemampuan model untuk menangkap pola dan risiko _overfitting_ serta waktu komputasi.
        - `loss='warp'`: WARP loss dipilih karena efektif untuk data rating eksplisit dan fokus pada optimasi ranking, yang relevan untuk rekomendasi top-N.
        - `learning_schedule='adagrad'`: Adagrad adalah optimizer adaptif yang menyesuaikan laju pembelajaran untuk setiap parameter, seringkali memberikan hasil yang baik tanpa perlu _tuning_ manual laju pembelajaran awal secara ekstensif.
        - `random_state=42`: Digunakan untuk memastikan hasil pelatihan model dapat direproduksi.
        - `epochs=20`: Jumlah iterasi pelatihan. Dipilih sebagai nilai awal yang cukup untuk model belajar pola tanpa memakan waktu terlalu lama.
        - `num_threads=10`: Digunakan untuk paralelisasi pada CPU, disesuaikan dengan ketersediaan core pada lingkungan eksekusi untuk mempercepat pelatihan.

Dengan mengimplementasikan kedua pendekatan ini, diharapkan sistem dapat memberikan rekomendasi yang lebih kaya dan relevan, mengatasi keterbatasan masing-masing metode jika digunakan secara terpisah.

---

## Data Understanding

Dataset yang digunakan adalah "Anime Recommendations Database" dari Kaggle ([https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)), yang merupakan hasil _scraping_ dari MyAnimeList ([https://myanimelist.net/topanime.php](https://myanimelist.net/topanime.php)).

### 1. `anime.csv`

Dataset ini berisi informasi detail mengenai setiap judul anime.

- **Variabel/Fitur:**
  - `anime_id`: ID unik anime (int).
  - `name`: Judul lengkap anime (object/string).
  - `genre`: Daftar genre, dipisahkan koma (object/string).
  - `type`: Tipe penayangan (Movie, TV, OVA, dll.) (object/string).
  - `episodes`: Jumlah episode (object/string, 1 jika Movie).
  - `rating`: Rata-rata rating (skala 1-10) (float).
  - `members`: Jumlah anggota komunitas (int).
- **Karakteristik Awal:**
  - Jumlah baris: 12.294.
  - Tidak ada data duplikat.
  - Nilai kosong ditemukan pada: `genre` (62 baris), `type` (25 baris), `rating` (230 baris).
  - Rating anime berkisar antara 1.67 hingga 10.0.

### 2. `rating.csv`

Dataset ini berisi rating yang diberikan oleh pengguna.

- **Variabel/Fitur:**
  - `user_id`: ID pengguna acak (int).
  - `anime_id`: ID anime yang dirating (int).
  - `rating`: Rating yang diberikan (skala 1-10, atau -1 jika hanya ditonton tanpa skor) (int).
- **Karakteristik Awal:**
  - Jumlah baris: 7.813.737.
  - Terdapat satu baris data duplikat.
  - Tidak ada nilai kosong (NaN).
  - Rating -1 mengindikasikan anime dalam _watchlist_ atau belum diberi skor.

### Exploratory Data Analysis (EDA)

**Insight dari `anime_df`:**

- Terdapat 3.265 genre unik.
- Tipe penayangan yang paling umum adalah TV.
- Anime dengan _voters_ terbanyak adalah "Death Note", "Shingeki no Kyojin", dan "Sword Art Online".
- Anime dengan episode terbanyak adalah "Oyako Club" (1818 episode).
- Penggunaan _Weighted Rating_ (mempertimbangkan jumlah _voters_) memberikan peringkat anime populer yang lebih reliabel dibandingkan rating mentah. Berdasarkan _Weighted Rating_, "Fullmetal Alchemist: Brotherhood" (TV), "Kimi no Na wa." (Movie), dan "Ginga Eiyuu Densetsu" (OVA) menjadi yang teratas di kategorinya masing-masing.
- Genre "Shounen", "Drama", dan "Action" paling sering muncul di 20 anime teratas. Pasangan genre "Action & Shounen" juga umum.

**Insight dari `rating_df`:**

- Sekitar 18.90% dari total rating adalah -1 (kemungkinan _watchlist_).
- Setelah filtering, terdapat 55.118 pengguna unik.
- Distribusi rating (tanpa -1) menunjukkan bahwa pengguna cenderung memberikan rating tinggi (7, 8, 9 paling umum).
- Anime populer seperti "Death Note" sering masuk _watchlist_, menunjukkan korelasi antara popularitas umum dan minat tontonan masa depan.
- Matriks rating pengguna-anime memiliki _sparsity_ sebesar 99.23%, yang umum untuk dataset rekomendasi.

---

## Data Preparation

Langkah-langkah pra-pemrosesan data dilakukan untuk meningkatkan kualitas dan kesesuaian data untuk pemodelan.

**1. Pembersihan `anime_df`:**

- Baris dengan nilai _null_ pada kolom `genre`, `type`, dan `rating` dihapus. Jumlah baris menjadi 12.017.
- Kolom `episodes` dikonversi menjadi tipe numerik (integer), dengan nilai "Unknown" atau NaN diimputasi menjadi 0.
- Normalisasi teks:
  - `type`: Menghilangkan spasi berlebih dan diubah ke _title case_.
  - `genre`: Menghilangkan spasi berlebih.
- Kolom `genre` (string genre dipisah koma) ditransformasi menjadi `genre_list` (list string genre).

**2. Pembersihan `rating_df` (menghasilkan `cf_df`):**

- Baris dengan `rating == -1` dihapus.
- Pengguna dengan kurang dari 10 rating dihapus.
- Duplikasi baris berdasarkan `user_id` dan `anime_id` dihapus, dengan mempertahankan entri terakhir.
- Anime yang dirating oleh kurang dari 5 pengguna dihapus.
- Setelah pembersihan, `cf_df` memiliki 6.274.555 baris.

**3. Feature Engineering untuk Content-Based Filtering (pada `content_df` turunan `anime_df`):**

- Kolom `genre_list` diproses lebih lanjut:
  - Setiap item genre diubah menjadi huruf kecil.
  - Karakter non-alfanumerik (spasi, tanda hubung) diganti dengan underscore (`_`).
  - Underscore berlebih dihilangkan. (Contoh: "Sci-Fi" menjadi "sci_fi").
- List token genre yang telah diproses (`genre_tokens`) digabungkan menjadi satu string (`genre_str`) per anime.
- `TfidfVectorizer` diterapkan pada `genre_str` untuk membuat `tfidf_matrix` dengan bentuk (12017, 43).

**4. Data Preparation untuk Collaborative Filtering (LightFM):**

- Objek `lightfm.data.Dataset` diinisialisasi dan di-_fit_ dengan `user_id` dan `anime_id` unik dari `cf_df`.
- Jumlah pengguna yang dikenali adalah 55.118 dan item (anime) adalah 8.025.
- Matriks interaksi (`interactions_matrix`) dan matriks bobot (`weights_matrix`) dibangun dari `cf_df` (rating sebagai bobot). Keduanya berformat COO dan berbentuk (55118, 8025).
- Pemetaan ID asli ke ID internal LightFM (dan sebaliknya) dibuat.
- Data interaksi dan bobot dibagi menjadi 80% data latih dan 20% data uji menggunakan `random_train_test_split`.

---

## Modeling and Result

Dua pendekatan sistem rekomendasi diimplementasikan dan diuji.

### Model 1: Content-Based Filtering

Model ini merekomendasikan anime berdasarkan kemiripan genre.

- **Perhitungan Kemiripan:** Matriks kemiripan kosinus (`cosine_sim_matrix_revised`) berukuran (12017, 12017) dihitung dari `tfidf_matrix_revised` (matriks TF-IDF genre yang telah diproses).
- **Fungsi Rekomendasi:** Fungsi `get_content_based_recommendations` dibuat untuk mengambil judul anime sebagai input, mencari kemiripannya dengan anime lain berdasarkan skor kosinus, dan mengembalikan 10 anime teratas yang paling mirip. Penanganan _case-insensitivity_ untuk judul input juga diterapkan.
- **Contoh Hasil (Top-N Recommendation):**
  Untuk anime input "Shigatsu wa Kimi no Uso", berikut adalah beberapa rekomendasi teratas:
  ```
                                                     name                                           genre_list
  5312                       D.C.III: Da Capo III Special                     [Drama, Music, Romance, School]
  2191               Kimi no Iru Machi: Tasogare Kousaten                   [Drama, Romance, School, Shounen]
  2211             Shinkyoku Soukai Polyphonica Crimson S            [Drama, Fantasy, Music, Romance, School]
  3507                     Shinkyoku Soukai Polyphonica 2                              [Drama, Fantasy, Music, Romance, School]
  256                                 Hibike! Euphonium 2                              [Drama, Music, School]
  ```
  Rekomendasi ini menunjukkan anime dengan genre yang serupa seperti Drama, Music, Romance, dan School.

### Model 2: Collaborative Filtering (LightFM)

Model ini merekomendasikan anime berdasarkan pola rating pengguna.

- **Definisi dan Pelatihan Model:**
  - Model LightFM diinisialisasi dengan `no_components=50`, `loss='warp'`, `learning_schedule='adagrad'`, dan `random_state=42`.
  - Model dilatih menggunakan `train_interactions` dan `train_weights` selama 20 epoch dengan `num_threads=10` (disesuaikan dengan jumlah core CPU yang tersedia, yaitu 12).
- **Fungsi Rekomendasi:** Fungsi `get_lightfm_recommendations` menghasilkan rekomendasi untuk `user_id` tertentu dengan memprediksi skor untuk item yang belum ditonton, menyaring yang sudah ditonton, dan mengembalikan 10 item teratas.
- **Contoh Hasil (Top-N Recommendation):**
  Untuk `user_id 32755`, yang diketahui menyukai "Noragami Aragoto" (rating 10) dan "Sakurasou no Pet na Kanojo" (rating 10), berikut adalah beberapa rekomendasi teratas:
  ```
                                                   name                                              genre  predicted_score
  0                                              Nisekoi                Comedy, Harem, Romance, School, Shounen         0.912856
  1                               Gekkan Shoujo Nozaki-kun                              Comedy, Romance, School         0.774158
  2                         Love Live! School Idol Project                       Music, School, Slice of Life         0.358599
  3                                     Kuroko no Basket                      Comedy, School, Shounen, Sports         0.184254
  4                            Kuroko no Basket 2nd Season                      Comedy, School, Shounen, Sports         0.169067
  ```

### Kelebihan dan Kekurangan Pendekatan yang Dipilih

- **Content-Based Filtering:**
  - **Kelebihan:** Transparan, tidak memerlukan banyak data rating pengguna lain, dapat menangani _cold start_ untuk item baru.
  - **Kekurangan:** Cenderung _over-specialized_, kualitas sangat bergantung pada fitur konten.
- **Collaborative Filtering (LightFM):**
  - **Kelebihan:** Mampu menemukan preferensi tersembunyi (_serendipity_), tidak bergantung pada fitur konten item secara eksplisit.
  - **Kekurangan:** Mengalami masalah _cold start_ untuk pengguna baru dan item baru, rentan terhadap _popularity bias_, dipengaruhi oleh _sparsity_ data.

---

## Evaluation

Evaluasi dilakukan untuk kedua model rekomendasi untuk mengukur kinerjanya.

### Metrik Evaluasi Content-Based Filtering

Evaluasi untuk model _content-based filtering_ yang murni berdasarkan kemiripan genre seringkali bersifat kualitatif. Namun, untuk memberikan gambaran kuantitatif mengenai seberapa sering rekomendasi berbasis genre selaras dengan preferensi rating historis pengguna, digunakan pendekatan simulasi dengan metrik berikut:

- **Precision@k**: Mengukur proporsi item yang relevan di antara K item teratas yang direkomendasikan. Dalam simulasi ini, "relevan" diartikan sebagai item yang juga dirating tinggi (misalnya, rating >= 7) oleh pengguna yang sama di masa lalu, setelah satu item yang disukainya digunakan sebagai input untuk rekomendasi berbasis konten.

- **MAP@k (Mean Average Precision)**: Merupakan rata-rata dari Average Precision (AP) untuk setiap pengguna sampel. AP memperhitungkan urutan item relevan dalam daftar rekomendasi, memberikan nilai lebih tinggi jika item relevan muncul di posisi awal.
- **NDCG@k (Normalized Discounted Cumulative Gain)**: Mengukur kualitas urutan rekomendasi dengan memberikan bobot lebih pada item relevan di posisi atas dan menggunakan skor relevansi aktual (dalam simulasi ini, rating pengguna digunakan sebagai skor relevansi).

**Alasan Penggunaan Data Pengguna (Rating) sebagai Ground Truth untuk Evaluasi Content-Based:**
Meskipun model _content-based_ tidak menggunakan data rating untuk membuat rekomendasi (ia menggunakan kemiripan genre), evaluasi performanya tetap memerlukan cara untuk mengukur apakah rekomendasi yang dihasilkan "baik" atau "relevan" dari perspektif pengguna. Data rating pengguna (khususnya item yang dirating tinggi) berfungsi sebagai _ground truth_ atau proksi untuk preferensi pengguna. Dengan menyimulasikan skenario di mana satu item yang disukai pengguna digunakan untuk menghasilkan rekomendasi konten, kemudian dibandingkan dengan item lain yang juga disukai pengguna tersebut, dapat diperoleh gambaran seberapa sering kesamaan genre berkorelasi dengan preferensi rating pengguna.

**Hasil Evaluasi Content-Based Filtering (Simulasi pada 100 Pengguna):**

- Mean Precision@10: **0.0770**
- MAP@10: **0.0422**
- Mean NDCG@10: **0.4375**

**Interpretasi Hasil Evaluasi Content-Based:**
Skor Precision@10 dan MAP@10 yang relatif rendah menunjukkan bahwa keselarasan antara kemiripan genre murni dengan preferensi rating historis pengguna untuk item lain tidak terlalu tinggi dalam simulasi ini. Skor NDCG@10 sebesar 0.4375 mengindikasikan kualitas ranking yang sedang. Hasil ini wajar karena model tidak dilatih pada preferensi rating pengguna, melainkan hanya pada fitur konten. Evaluasi kualitatif (seperti pada contoh "Shigatsu wa Kimi no Uso") yang menunjukkan relevansi genre tetap penting untuk model ini.

### Metrik Evaluasi LightFM

- **Precision@k**: Mengukur proporsi item yang direkomendasikan dalam k item teratas yang relevan.
  Metrik ini penting untuk mengetahui seberapa akurat rekomendasi yang diberikan dalam sejumlah kecil item yang ditampilkan ke pengguna.
- **Recall@k**: Mengukur proporsi item relevan yang berhasil ditemukan dan direkomendasikan dalam k item teratas.
  Metrik ini penting untuk mengetahui seberapa banyak item yang disukai pengguna yang berhasil ditangkap oleh sistem.
- **AUC (Area Under the ROC Curve)**: Mengukur kemampuan model untuk membedakan antara pasangan item positif dan negatif secara acak. Nilai mendekati 1 menunjukkan performa yang lebih baik dalam ranking.

### Hasil Evaluasi LightFM

- **Pada Data Pelatihan**:
  - Training Precision@10: 0.6152
  - Training Recall@10: 0.1515
  - Training AUC: 0.9857
- **Pada Data Pengujian**:
  - Test Precision@10: 0.3146
  - Test Recall@10: 0.2080
  - Test AUC: 0.9763

### Interpretasi Hasil Evaluasi Keseluruhan

Model _collaborative filtering_ (LightFM) menunjukkan performa kuantitatif yang lebih baik dalam mencocokkan preferensi rating pengguna (AUC 0.9763 pada data uji) dibandingkan dengan evaluasi simulasi pada model _content-based_. Penurunan Precision@10 dari data latih ke data uji pada LightFM mengindikasikan adanya sedikit _overfitting_, namun presisi 0.3146 pada data uji masih menunjukkan bahwa sekitar 3 dari 10 rekomendasi teratas adalah relevan. Recall@10 sebesar 0.2080 menunjukkan kemampuan model untuk menemukan sebagian item relevan.

Model _content-based_, meskipun skor metrik kuantitatif simulasinya lebih rendah, tetap memiliki nilai dalam skenario _cold start_ item dan memberikan rekomendasi yang transparan berdasarkan genre.

---

### Interpretasi Bisnis

Hasil evaluasi model, khususnya model _collaborative filtering_ dengan LightFM, memberikan implikasi bisnis yang positif. Skor AUC yang tinggi (0.9763 pada data uji) menunjukkan bahwa sistem memiliki kemampuan yang kuat untuk membedakan anime yang mungkin disukai pengguna dari yang tidak. Dari perspektif bisnis, ini berarti sistem dapat diandalkan untuk menyajikan konten yang lebih relevan, yang berpotensi meningkatkan kepuasan dan retensi pengguna.

Nilai Precision@10 sebesar 0.3146 pada data uji untuk LightFM, meskipun menunjukkan adanya ruang untuk peningkatan akibat _overfitting_, tetap memberikan nilai bisnis. Ini berarti bahwa dari 10 anime yang direkomendasikan, rata-rata sekitar 3 anime akan benar-benar relevan bagi pengguna. Dalam konteks platform dengan ribuan judul, kemampuan untuk menyajikan 3 judul yang kemungkinan besar disukai dari 10 saran pertama adalah langkah signifikan dalam mengurangi _information overload_ dan membantu pengguna menemukan konten baru.

Evaluasi _content-based filtering_, meskipun dengan metrik simulasi yang lebih rendah (Mean Precision@10: 0.0770), tetap menunjukkan bahwa ada kalanya kesamaan genre dapat mengarah pada item yang juga disukai pengguna. Kekuatan utamanya adalah dalam transparansi dan penanganan _cold-start_ item.

Kombinasi kedua model menawarkan fleksibilitas. _Content-based filtering_ dapat digunakan untuk pengguna baru (mengatasi _cold start_ pengguna) atau untuk merekomendasikan anime baru yang belum memiliki banyak rating (_cold start_ item). Sementara itu, _collaborative filtering_ dapat memberikan rekomendasi yang lebih personal dan _serendipitous_ bagi pengguna dengan riwayat interaksi yang cukup. Strategi _hybrid_ yang menggabungkan output kedua model ini bisa menjadi langkah pengembangan selanjutnya untuk memaksimalkan nilai bisnis, seperti meningkatkan jumlah anime yang ditonton per sesi, durasi kunjungan pengguna, dan loyalitas terhadap platform.

---

🍎 Fruit Classification using CNN (Fruit-360 Dataset)

Proyek ini bertujuan untuk membangun model klasifikasi gambar menggunakan Convolutional Neural Network (CNN) untuk mengidentifikasi berbagai jenis buah berdasarkan gambar. Dataset yang digunakan adalah **Fruit-360**, yang berisi gambar buah dari berbagai sudut, ukuran, dan tingkat kematangan (matang dan busuk).

## 📂 Dataset

Dataset yang digunakan adalah [Fruit-360 Dataset](https://www.kaggle.com/datasets/moltean/fruits), yang terdiri dari:

- Gambar buah-buahan dari berbagai jenis
- Diambil dari berbagai sudut pandang
- Terdiri dari buah yang masih segar dan busuk
- Ukuran gambar: 100x100 piksel

## 🧠 Model Arsitektur

Model CNN dibangun menggunakan TensorFlow dan terdiri dari beberapa layer:

- `Conv2D` + `BatchNormalization` + `ReLU`
- `MaxPooling2D`
- `Dropout` untuk regularisasi
- `Dense` (fully connected layer) dengan softmax di output layer

Optimasi dilakukan menggunakan:

- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Output**: One-hot encoding dari label buah

## 📊 Hasil

Model mencapai akurasi:

- Training: **86%**
- Testing: **97%**

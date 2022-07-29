[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8039826&assignment_repo_type=AssignmentRepo)
# Graded Challenge 2

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Classification terutama Logistic Regression dan SVM._

---

## Assignment Instructions

Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=census_adult_income&page=table) untuk langsung menuju ke dataset.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan dataset `ml_datasets` dari database bernama `census_adult_income`.
2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `age, workclass, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country, dan income_bracket`.
   - Kolom diatas hanya digunakan sebagai dataset awal. Silakan lakukan Feature Selection di-notebook setelah dataset dibuat.
   - Pilih semua `workclass`, kecuali `?`.
   - Pilih `hours_per_week` kurang dari 100.
   - Limit jumlah data menjadi sebanyak `nomor batch dikali dengan tahun lahir kalian`. ex: Batch 10 dan lahir tahun 1995, 10 x 1995 = 19950.
3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P1G2_<nama-students>.csv`.
4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!
5. Tampilkan `head` dan `tail` dari dataset pada notebook!

_Graded Challenge 2_ dikerjakan dalam format _notebook_ dengen beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah _Scikit-Learn_.

2. Ada penggunaan library visualisasi, seperti _matplotlib_, _seaborn_, atau yang lain.

3. Isi _notebook_ harus mengikuti _outline_ di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, **query yang telah kalian buat pada Google Cloud Platform!**, dan _objective_ yang ingin dicapai.

   2. Import Libraries
      > _Cell_ pertama pada _notebook_ **harus berisi dan hanya berisi** semua _library_ yang digunakan dalam _project_.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Data Preprocessing
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-dev-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.

   10. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan _objective_ yang sudah ditulis di bagian pengenalan.

4. Notebook harus diupload dalam akun GitHub Classroom masing-masing siswa untuk selanjutnya dinilai. Jika dalam sebuah tugas terdapat dua atau lebih soal, maka gabungkan jawaban ke dalam satu file notebook.

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1W1LGSVM_<nama-student>.ipynb` misal `h8dsft_P1W1LGSVM_raka_ardhi.ipynb`.
- Push Assigment yang telah kalian buat ke akun Github Classroom kalian masing-masing.

## Problems

Buatlah model Classification menggunakan Logistic Regression dan SVM untuk memprediksi `income bracket` menggunakan dataset yang sudah kalian simpan.

## Conceptual Problems

_Jawab pertanyaan berikut:_

1. Apakah yang dimaksud dengan `coeficient` pada logistic regression?
2. Apakah yang dimaksud dengan `Support Vector` pada SVM?
3. Apakah fungsi parameter `kernel` pada SVM? Jelaskan salah satu kernel yang kalian pahami!

## Assignment Objectives

_Graded Challenge 2_ ini dibuat guna mengevaluasi konsep Logistic Regression dan SVM sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu memahami konsep Classification dengan Logistic Regression dan SVM
- Mampu mempersiapkan data untuk digunakan dalam model Logistic Regression dan SVM
- Mampu mengimplementasikan Logistic Regression dan SVM untuk membuat prediksi

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan | 30 pts |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts |
| Logistic Regression | Mengimplementasikan Logistic Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| SVM | Mengimplementasikan SVM dan menentukan hyperparameter yang tepat dengan dengan Scikit-Learn | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Classifications | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (10 each number) | 30 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 20 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 30 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan kelemahan/kekurangan dan kelebihan dari model yang dibuat.
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Sebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

`Total Points : 190`

---

## Notes

- **Deadline : P1W2D5 pukul 23:59 WIB.**

- **Keterlambatan pengumpulan tugas mengakibatkan skor GC 2 menjadi 0.**

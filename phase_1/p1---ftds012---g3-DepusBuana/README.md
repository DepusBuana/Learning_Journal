[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8061530&assignment_repo_type=AssignmentRepo)
# Graded Challenge 3

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Ensemble Learning._

---

## Assignment Objectives

*Graded Challenge 3* ini dibuat guna mengevaluasi konsep Ensemble Learning sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery
- Mampu memahami konsep Classification dengan Ensemble Learning.
- Mampu mengimplementasikan Ensemble Learning untuk membuat prediksi.
- Mampu memahami konsep salah satu algoritma boosting dan mengimplementasikannya dalam kasus Supervised Learning

---

## Problems

Buatlah model Classification menggunakan Random Forest dan salah satu algoritma boosting untuk memprediksi apakah seorang pasien akan meninggal atau tidak menggunakan dataset yang sudah Anda dapatkan.

---

## Conceptual Problems

*Jawab pertanyaan berikut:*

1. Apakah yang dimaksud dengan Bagging?

2. Jelaskan perbedaan algoritma Random Forest dengan algoritma boosting yang Anda pilih?

---

## Dataset

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Pada tugas kali ini, dataset yang digunakan **tidak akan menggunakan `bigquery-public-data`**. 

2. Masuk ke dalam Google BigQuery. Gunakan informasi dibawah ini sebagai tempat untuk mengambil data (gunakan sebagai informasi untuk klausa `FROM`).
   * Project ID : `ftds-hacktiv8-project`
   * Dataset Name : `phase1_assignments`
   * Table Name : `heart-failure`

3. Ambil semua data dari table nomor 2.

4. Berikut ini adalah informasi dari setiap column. 
   <img src='https://i.ibb.co/YBGwMXm/P1-G3-Dataset-Information.png'>

5. Simpan dataset dalam bentuk `.csv` dengan nama `h8dsft_P1G3_<nama-students>.csv` misal `h8dsft_P1G3_raka_ardhi.csv`.

6. Salin query yang telah dibuat di Google Cloud Platform. Tulislah pada bagian atas notebook!

7. Tampilkan `head` dan `tail` dari dataset pada notebook!

---

## Assignment Instructions

*Graded Challenge 3* dikerjakan dalam format ***notebook*** dengen beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   
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
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
5. *Notebook* harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P1G3_<nama-student>.ipynb` misal `h8dsft_P1G3_raka_ardhi.ipynb`.

- Push assignment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan | 15 pts |
| Preprocessing | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 20 pts |
| Random Forest | Mengimplementasikan Random Forest dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Boosting | Mengimplementasikan Boosting dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Apakah Kode Berjalan Tanpa Ada Error? | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Classifications | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (Soal 1 : 10 pts. Soal 2 : 20 pts) | 30 pts |

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

```
Total Points : 175
```

---

## Notes

* **Deadline : P1W3D4 pukul 23:59 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor GC 3 menjadi 0.**

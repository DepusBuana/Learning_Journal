[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7974528&assignment_repo_type=AssignmentRepo)
# Live Code 3

```{attention}
This page is still on development.
```

## Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas
2. **Judul/Penanda Soal**\
    Sediakan *Cell* Markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan di tiap soalnya. Tiap soal mengikuti format nomor 2-6.
3. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
4. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana.
5. *Data Processing*\
   Bagian ini berisi proses pengolahan data hingga siap dianalisa.
6. *Mathematical Calculation and Analysis*\
    Bagian ini berisi perhitungan matematis dan analisa yang diperlukan seperti membuat grafik, dsb.
6. Hasil\
   Pada bab terakhir ini berisi jawaban dari pertanyaan soal/kesimpulan analisa.

---

## Problems

Kamu adalah seorang data scientist di salah satu perusahaan penjual Liquor. Ada terdapat 5000 transaksi yang terjadi di satu hari untuk suatu produk. Tim marketing menduga ada suatu keanehan pada data transaksi. Bantu tim marketing untuk memvalidasi dugaan mereka apakah betul ada anomali pada data transaksi.

## Dataset Description

* Pada graded challenge ini, data diakses menggunakan `bigquery-public-data` pada Google Cloud Big Query.
* Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=iowa_liquor_sales&t=sales&page=table) untuk langsung menuju ke tabel.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan tabel `sales` pada dataset `iowa_liquor_sales.
2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `sale_dollars`

   - Batasi jumlah data maksimal 5000
3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P0LC3_<nama-students>.csv`.
4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!
5. Tampilkan `head` dan `tail` dari dataset pada notebook!

**Clue**
Untuk mengetahui adanya anomali, kamu bisa menggunakan metode extreme value analysis. Untuk melakukan pengecekan anomali/outlier, lakukan langkah-langkah di bawah ini:
1. Lakukan perhitungan central tendency (mean, median, modus) terhadap data sebelum dideteksi adanya anomali. ***[Menjawab Rubrik 1b]***
2. Cek skewness data untuk mengetahui apakah data terdistribusi normal atau tidak. ***[Menjawab Rubrik 1c]***
3. Lakukan pengolahan data dengan menggunakan extreme value analysis. ***[Menjawab Rubrik 1d]***
4. Buat variabel baru yang menyimpan data yang sudah dibuang data anomalinya.
5. Analisis signifikansi perbedaan data sebelum dibuang outliernya dengan sesudah menggunakan hipotesis testing single sample. (Anggap data awal merupakan data populasi dan data baru merupakan sample). Definisikan pula hipotesis null dan alternatifnya. ***[Menjawab Rubrik 1e]***

**PERTANYAAN**

**Silahkan jawab pertanyaan-pertanyaan di bawah ini berdasarkan hasil yang kamu peroleh dan tulis pada bagian hasil:**
1. Berapa rata-rata, median, dan modus dari data tersebut sebelum dihilangkan outliernya? Bagaimana kecerendungan pemusatan datanya? jelaskan jawabanmu!***[Menjawab Rubrik 2a]***
2. Sebelum melakukan extreme value analysis, kamu harus melakukan pengecekan skewness dari distribusi datanya. Apakah datanya skew atau normal? jelaskan jawabanmu!***[Menjawab Rubrik 2b]***
3. Ada dua teknik untuk melakukan extreme value analysis, teknik yang mana yang kamu pakai? berikan alasanmu berdasarkan data!***[Menjawab Rubrik 2c]***
4. Ada berapa banyak data yang merupakan outlier? apakah cukup signifikan jumlahnya? (anggap bahwa jumlah signifikan lebih dari 50%). Jelaskan jawabanmu!***[Menjawab Rubrik 2d]***
5. Setelah kamu menyingkirkan outlier dari data dan melakukan uji hipotesis, apakah ada perbedaan yang signifikan? jelaskan jawabanmu!***[Menjawab Rubrik 2e]***

**POIN ANALISIS**
1. Apa kesimpulan yang akan kamu bagikan kepada tim marketing berkaitan dugaan mereka?
---

## Assignment Rubrics

### 1. Code Review
**Impementasi Code Python**
|No.|Criteria|Meet Expectations|Points|
|---|--- |--- |--- |
|a|Data Retrieve|Mampu memperoleh data dari GCP BigQuery menggunakan SQL| 5 pts |
|b|Central Tendency|Mampu menerapkan konsep central tendency pada data| 2 pts |
|c|Distribution|Mampu mengecek distribusi/skewness data menggunakan library| 2 pts |
|d|Extreme Value Analysis|Mampu menerapkan extreme value analysis di code| 2 pts |
|e|Hypothesis Testing|Mampu mendefinisikan hypothesis dan menerapkan konsep pengujian hipotesis di code| 4 pts |

### 2. Conceptual
**Menjawab Pertanyaan**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Central Tendency Concept|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |
|b|Distribution|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat | 5 pts |
|c|Extreme Value Analysis|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |
|d|Outlier Analysis|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |
|d|Hypothesis Testing|Mampu menjawab pertanyaan dengan singkat, jelas, dan padat| 5 pts |

### 3. Analysis

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Poin Analisis|Menarik Informasi/Kesimpulan Dari Analisa.| 13 pts |

### 4. Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 10 pts |

---

```{admonition} Total Points
**60**
```

---

## Score Reduction

Pengurangan poin akan diberlakukan jika Student terlambat mengumpulkan tugas yang telah diberikan. Adapun besarnya pengurangan adalah :

| Criteria | Max Points LC3 |
| --- | --- |
| Keterlambatan, mengumpulkan di antara 12.16 - 13.00 | 45 pts (75 %) |
| Keterlambatan, mengumpulkan di antara 13.01 - 18.00 | 30 pts (50 %) |
| Keterlambatan lebih dari 18.00 di hari yang sama | 0 pts (0 %) |

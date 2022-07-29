[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7940163&assignment_repo_type=AssignmentRepo)
# Live Code 2

# Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas
2. **Judul/Penanda Soal**\
    Sediakan *Cell* Markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan di tiap soalnya. Tiap soal mengikuti format nomor 2-6.
3. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
4. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana.
5. *Mathematical Calculations*\
   Bagian ini berisi proses pengolahan data dengan perhitungan matematis yang diperlukan.
6. Hasil\
   Pada bab terakhir ini berisi jawaban dari pertanyaan soal.

---

# Problems

## Problem 1
Salah satu ruang lingkup Natural Language Processing (NLP) adalah mengukur kesamaan konteks antar kalimat. Untuk mengetahui dua kalimat memiliki konteks yang sama atau tidak, kita mengukurnya dengan *cosine similarity*. Cosine similarity sejatinya mengukur 'jarak' antar dua vektor yang mana vektor-vektor tersebut berisikan angka-angka, sehingga kita perlu menerjemahkan kalimat menjadi list angka (encoding). Ada banyak metode encoding yang dapat digunakan untuk menerjemahkan kalimat ke angka, salah satunya adalah dengan menghitung frekuensi kemunculan kata pada setiap kalimat.

Kalimat 1: Julie loves me more than Linda loves me

Kalimat 2: Jane likes me more than Julie loves me

Berikut tabel yang berisikan frekuensi kata yang muncul pada kedua kalimat:

|Kata|Kalimat 1|Kalimat 2|
|--- |--- |--- |
| me  | 2  | 2 |
| Jane | 0 | 1 |
|Julie |  1 | 1 |
|Linda |  1 | 0 |
|likes |  0 | 1 |
|loves |  2 | 1 |
|more |  1 | 1 |
|than |  1 | 1 |

Buatlah vektor yang merupakan representasi masing-masing kalimat berdasarkan tabel di atas dan hitung cosine similarity antar kedua vektor. Kemudian *jawab pertanyaan berikut* di **markdown**:

a. Apakah kedua kalimat memiliki konteks yang serupa? jika iya, mengapa dan jika tidak, mengapa (jawab berdasarkan hasil perhitungan cosine similaritynya)?

b. Jika meninjau dua buah vektor dan dihitung cosine similaritynya (cos theta), jelaskan secara singkat, jelas, padat apa makna cosine similarity yang bernilai 0 dan 1 (tinjau dari posisi dua vektor di koordinat kartesian)?

c. Apa kekurangan dari perhitungan kemiripan menggunakan cosine similarity?

---
## Problem 2

### Dataset

* Pada problem 2, data diakses menggunakan `bigquery-public-data` pada Google Cloud Big Query.
* Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau klik link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=samples&page=dataset&_ga=2.245085957.1471931019.1642739417-486643658.1638156099) atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=geo_us_boundaries&t=states&page=table) untuk langsung menuju ke tabel.

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Gunakan tabel `states` pada dataset `geo_us_boundaries`.
2. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** negara bagian `Colorado` (Informasi nama negara bagian terdapat di kolom `state_name`).
3. Simpan dataset dalam bentuk csv, dengan nama `h8dsft_P0LC2_<nama-students>.csv`.
4. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook!
5. Tampilkan data pada notebook (Data hanya mengandung satu baris saja)!

Menggunakan konsep integral untuk menghitung luas dibawah kurva, tentukan luas negara bagian Colorado jika diketahui koordinat batas-batasnya pada data yang sudah kamu ambil dari big query. 

**PERLU DIPERHATIAN** bahwa data yang kamu ambil, masih belum siap dipakai untuk perhitungan integral. Gunakan fungsi berikut untuk membantu kamu agar data kamu siap digunakan dan tampilkan data yang sudah di-preprocess dengan fungsi tersebut. Kamu harus mengimport library `re` terlebih dahulu ke dalam pekerjaanmu. `Inputan argumen function berikut hanya berupa dataframe`.

```python
def data_preprocess(data):
   long = []
   lat = []
   for row in data['state_geom'][0].split(', '):
     row = re.sub('MULTIPOLYGON','',row)
     row = re.sub('POLYGON','',row)
     row = re.sub(r'\(','',row)
     row = re.sub(r'\)','',row)
     long.append(float(row.split(' ')[0]))
     lat.append(float(row.split(' ')[1]))
   return pd.DataFrame({'long':long,'lat':lat}).sort_values('long',ascending=True)
```

*Jawab pertanyaan berikut* di **markdown**:

a. Integral jenis apa yang diterapkan pada kasus ini? (Tertentu/Tak tentu) dan mengapa demikian? berikan alasan!

b. Untuk kasus ini, metode apa yang kamu pakai dalam perhitungan integral? secara simbolik atau numerik, dan mengapa?

c. Library Scipy menyediakan banyak function/modul untuk menghitung integral. Function apa yang kamu gunakan dan berikan alasan yang logis!


**Hint dan Note soal nomor 2**:
- Longitude (`long`) adalah sumbu x dan Latitude (`lat`) adalah sumbu y nya.
- Wilayah Colorado dapat dibagi menjadi dua bagian yaitu Northern dan Southern (dapat menggunakan acuan nilai tengah latitude dimana nilai maksimum ditambah nilai minimum lalu dibagi dua. Di atas nilai tengah northern dan di bawah nilai tengah southern) supaya mempermudah dalam menghitung Integral.
- Luas negara bagian Colorado bersatuan derajat kuadrat dan nilainya sekitar 28 derajat kuadrat.

---

## Assignment Rubrics

### 1. Code Review
**Impementasi Code Python**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Vector Implementation|Dapat membuat Vector menggunakan library Numpy| 2 pts |
|b|Linear Algebra Implementation|Mampu menerapkan konsep cosine similarity dengan library NumPy| 4 pts |
|c|SQL Queries|Mampu mengambil data dengan SQL dari Big Query GCP | 5 pts |
|d|Calculus Implementation|Mampu menerapkan konsep Integral dengan library Scipy| 4 pts |

### 2. Conceptual
**Menjawab Pertanyaan**
|No.|Criteria|Meet Expectations|Points|
|--- |--- |--- |--- |
|a|Linear Algebra Concept|Mampu menjawab pertanyaan secara singkat, padas, dan jelas menggunakan konsep matriks (masing-masing soal: 5 pt)| 15 pts |
|b|Calculus Concept|Mampu menjawab pertanyaan secara singkat, padas, dan jelas menggunakan konsep integral (masing-masing soal: 5 pt)| 15 pts |

### 3. Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 10 pts |

---

```{admonition} Total Points
**55**
```

---

## Score Reduction

Pengurangan poin akan diberlakukan jika Student terlambat mengumpulkan tugas yang telah diberikan. Adapun besarnya pengurangan adalah :

| Criteria | Max Points LC2 |
| --- | --- |
| Keterlambatan, mengumpulkan di antara 12.16 - 13.00 | 41,25 pts (75 %) |
| Keterlambatan, mengumpulkan di antara 13.01 - 18.00 | 27,5 pts (50 %) |
| Keterlambatan lebih dari 18.00 di hari yang sama | 0 pts (0 %) |

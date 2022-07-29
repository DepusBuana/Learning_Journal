[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7901357&assignment_repo_type=AssignmentRepo)
# Live Code 1

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
5. *Answer*\
   Bagian ini berisi proses dalam menjawab soal.
6. Hasil\
   Pada bab terakhir ini berisi jawaban pertanyaan soal.

---

## Problems

1. Kamu adalah seorang data scientist yang bekerja di salah satu perusahaan manufaktur baterai Lithium ion. Tim produksi meminta kamu untuk mengecek apakah baterai yang mereka buat dalam kondisi bagus atau tidak. Sebelum melakukan pengecekan lebih lanjut, kamu diminta untuk menghitung hambatan/resistansi dan Daya setiap detik:


<p align="center"><img src="https://latex.codecogs.com/png.latex?R=\frac{V}{I}" title="R=\frac{V}{I}" /></p>


<p align="center"><img src="https://latex.codecogs.com/png.latex?P=VI" title="P=VI" class="center" /></p>

- R adalah Kapasitas dalam satuan Ohm
- P adalah Daya dalam Watt
- I adalah kuat arus dalam satuan Ampere
- V adalah tegangan dalam satuan Volt

a. Buatlah dua fungsi eksplisit masing-masing memuat perhitungan hambatan (R) dan daya (P) yang nantinya akan digunakan untuk perhitungan

b. Buat kolom baru dengan nama kolom R/P berisikan hasil perhitungan daya/hambatan dengan kriteria untuk Kapasitas >=2.5 hitung daya, Kapasitas <2.5 hitung nilai hambatan. (**Hint:** Gunakan for loop dan if statement untuk mengerjakan perintah nomor b, kamu bisa menggunakan list untuk menyimpan perhitungan sementara, setelahnya dapat dimasukkan ke kolom R/P).

c. Hitunglah rata-rata nilai kapasitas untuk arus = 1 Ampere dan cycle ganjil.


## Dataset
Dataset dapat diakses pada link berikut: https://github.com/fahmimnalfrzki/Dataset/blob/main/NMC1-9.xlsx?raw=true

**Keterangan kolom:**
- time(s): Detik ke- pengukuran
- V_m: Voltage/tegangan yang terukur tiap waktu
- Current (A): Kuat arus terukur tiap waktu
- Cycle: Nomor siklus charge-discharge baterai
- Cap: Kapasitas baterai tiap waktu

---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Data Loading|Mampu memuat data dengan Pandas| 2 pts |
|Looping Implementation|Mampu menerapkan looping for dalam suatu kasus| 10 pts |
|Conditional If Implementation|Mampu menerapkan konsep conditional if dalam suatu kasus| 10 pts |
|Function Implementation|Mampu menerapkan function pada sebuah kasus| 10 pts |
|Pandas Query Implementation|Mampu mengimplementasikan pandas query dalam pengolahan data| 10 pts |

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 8 pts |


---

```{admonition} Total Points
**50**
```

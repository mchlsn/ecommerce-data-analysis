# 🛒 E-Commerce Sales Data Analysis

![Python](https://img.shields.io/badge/Python-3.12.7-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Project Overview
Analisis data transaksi e-commerce untuk menemukan insight bisnis
dan mempersiapkan data untuk model machine learning.

Dataset berisi **50.000 transaksi** dari toko online UK dengan informasi
produk, harga, quantity, dan data pelanggan.

## 🎯 Objectives
- Melakukan Exploratory Data Analysis (EDA) untuk memahami karakteristik data
- Membersihkan data dari missing values, duplikat, dan outlier
- Menemukan insight bisnis dari pola transaksi
- Mempersiapkan data yang siap digunakan untuk model ML

## 📊 Key Findings
- **90%+** transaksi berasal dari United Kingdom
- **REGENCY CAKESTAND 3 TIER** adalah produk dengan revenue tertinggi
- Ditemukan **17.881 transaksi** tanpa CustomerID (35.7% dari total data)
- Mayoritas produk berharga **£1-5** per unit
- Transaksi retur ditemukan dari nilai Quantity negatif

## 🛠️ Tools & Libraries
| Tool | Kegunaan |
|------|----------|
| Python 3.12.7 | Bahasa pemrograman utama |
| Pandas | Manipulasi & analisis data |
| NumPy | Operasi matematika |
| Matplotlib & Seaborn | Visualisasi data |

## 🔄 Preprocessing Steps
1. **Drop invalid rows** — Quantity negatif, UnitPrice = 0 atau >500
2. **Handle missing values** — Drop CustomerID & Description kosong
3. **Remove duplicates** — Hapus 537 baris duplikat
4. **Feature engineering** — Tambah kolom Revenue (Quantity × UnitPrice)
5. **Encoding** — Label encoding kolom Country
6. **Normalisasi** — StandardScaler untuk fitur numerik

## 📈 Results
| Kondisi | Jumlah Baris |
|---------|-------------|
| Data awal | 50.000 |
| Setelah cleaning | 30.711 |
| Kolom akhir | 9 kolom |

## 🚀 How to Run
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Jalankan preprocessing otomatis
cd preprocessing
python automate_MichaelSan.py
```

## 👤 Author
**MichaelSan**  
📧 michaelsanjaya633@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/mchlsn)
| Scikit-learn | Preprocessing & encoding |

## 📁 Project Structure

<div align="center">

<img src="https://img.shields.io/badge/Money%20Alfian-v3.8-6366f1?style=for-the-badge&logo=wallet&logoColor=white" alt="Money Alfian"/>

# 💰 Money Alfian
### *Smart Personal Finance Assistant*

> Aplikasi manajemen keuangan pribadi berbasis web yang cerdas, modern, dan responsif — dilengkapi asisten AI, grafik analitik, serta penyimpanan cloud.

<br/>

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Gemini AI](https://img.shields.io/badge/Gemini_AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.8-blue?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![Responsive](https://img.shields.io/badge/Responsive-Mobile%20%26%20Desktop-orange?style=flat-square)]()

<br/>

[🚀 Live Demo](#-demo) · [✨ Fitur](#-fitur) · [⚙️ Instalasi](#️-instalasi) · [📖 Cara Pakai](#-cara-pakai) · [📸 Screenshot](#-screenshot) · [📞 Kontak](#-kontak)

</div>

---

## 📌 Tentang Proyek

**Money Alfian** adalah aplikasi web keuangan pribadi yang dirancang untuk membantu pengguna mencatat, memantau, dan menganalisis pemasukan serta pengeluaran sehari-hari dengan cara yang mudah dan menyenangkan.

Dilengkapi dengan **asisten AI berbasis Google Gemini**, pengguna dapat bertanya langsung tentang kondisi keuangan mereka, meminta saran menabung, atau mendapatkan analisa otomatis dari data transaksi yang sudah dimasukkan.

Proyek ini dibuat sebagai bagian dari tugas **Mata Kuliah Pemrograman Web — Semester 4**.

---

## ✨ Fitur

### 🏠 Dashboard
- Tampilan ringkasan **total pemasukan**, **pengeluaran**, dan **sisa saldo** secara real-time
- Daftar **transaksi terkini** (5 data terakhir)
- Sapaan personal berdasarkan nama pengguna yang login

### ➕ Input Transaksi
- Catat transaksi **pemasukan** dan **pengeluaran** dengan mudah
- Input **nominal, keterangan, dan tanggal/waktu** secara fleksibel
- Format angka otomatis (Rupiah) saat mengetik
- Riwayat lengkap semua transaksi dengan tombol hapus

### 📊 Analisa & Grafik
- **Bar chart** interaktif pemasukan vs pengeluaran per hari (Chart.js)
- **Analisa otomatis** kondisi keuangan dengan narasi cerdas
- Visualisasi data yang bersih dan mudah dibaca

### 🤖 Tanya AI (Gemini)
- Chat langsung dengan **AI asisten keuangan** berbasis Google Gemini
- Tanya apa saja: *"Berapa saldo saya?"*, *"Bagaimana cara menabung?"*

### 📄 Laporan PDF & CSV
- Ekspor seluruh riwayat transaksi ke file **PDF** atau **CSV** dengan satu klik
- Laporan PDF berisi format tabel profesional, kartu ringkasan keuangan berwarna (Pemasukan, Pengeluaran, Saldo Bersih), penomoran halaman otomatis, dan header resmi
- Ekspor CSV berformat rapi dan lengkap (BOM UTF-8, metadata laporan, pemisah kolom aman, dan baris total)
- Powered by **jsPDF + AutoTable**

### ⚙️ Pengaturan
- Ganti **foto profil** (upload dari perangkat)
- Toggle **Dark Mode / Light Mode**
- Ganti **bahasa** antarmuka: 🇮🇩 Indonesia / 🇬🇧 English
- **Hapus semua data** dengan konfirmasi
- Tombol **Hubungi Pembuat** langsung via WhatsApp

### ☁️ Cloud Storage
- Data tersimpan di **Firebase Realtime Database** secara otomatis
- **Sinkronisasi lintas perangkat** — login dari HP atau laptop, data tetap sama
- **Offline fallback** menggunakan localStorage jika tidak ada internet
- Sistem **multi-user** — setiap akun memiliki data terpisah

### 🔐 Autentikasi
- Halaman **Login & Register** yang bersih dan aman
- Sistem **multi-user** berbasis username + password
- Proteksi halaman — tidak bisa diakses tanpa login

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan | Versi |
|-----------|----------|-------|
| **HTML5** | Struktur halaman web | Latest |
| **JavaScript (ES6+)** | Logika aplikasi & interaktivitas | ES2022 |
| **Tailwind CSS** | Styling & desain responsif | CDN Latest |
| **Chart.js** | Grafik bar pemasukan/pengeluaran | Latest |
| **Google Gemini AI** | Asisten keuangan berbasis AI | `gemini-2.0-flash` |
| **Firebase Realtime DB** | Penyimpanan data online | REST API |
| **jsPDF + AutoTable** | Ekspor laporan tabel ke PDF | 2.5.1 / 3.8.2 |
| **Font Awesome 6** | Ikon-ikon antarmuka | 6.4.0 |
| **Google Fonts (Outfit)** | Tipografi modern | Latest |

---

## 📁 Struktur Proyek

```
money-alfian/
│
├── 📄 index.html          # Halaman utama aplikasi (dashboard, transaksi, AI, dll)
├── 📄 login.html          # Halaman login & registrasi akun
├── 📄 README.md           # Dokumentasi proyek ini
│
├── 📂 .vercel/            # Konfigurasi deployment Vercel
│   ├── project.json
│   └── README.txt
│
└── 📂 money-alfian/       # Folder aset tambahan (jika ada)
```

---

## ⚙️ Instalasi & Menjalankan

### Cara 1 — Buka Langsung (Paling Mudah)
Tidak perlu install apapun. Cukup:
1. Download atau clone repository ini
2. Buka file `login.html` di browser (Chrome / Edge direkomendasikan)
3. Daftar akun baru → Login → Mulai gunakan!

```bash
# Clone repository
git clone https://github.com/USERNAME_ANDA/money-alfian.git

# Masuk ke folder
cd money-alfian

# Buka di browser (Windows)
start login.html

# Buka di browser (Mac/Linux)
open login.html
```

### Cara 2 — Pakai Live Server (VSCode)
1. Install ekstensi **Live Server** di VSCode
2. Klik kanan pada `login.html` → **"Open with Live Server"**
3. Browser akan otomatis terbuka

### Cara 3 — Deploy ke Vercel (Online)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Ikuti instruksi di terminal
```

---

## 🔥 Setup Cloud Storage (Firebase)

Agar data tersimpan online dan bisa diakses dari perangkat manapun:

1. Buka [console.firebase.google.com](https://console.firebase.google.com)
2. Klik **"Add project"** → beri nama `money-alfian` → **Create**
3. Di sidebar: **Build → Realtime Database → Create Database**
4. Pilih lokasi **`asia-southeast1`** → **Start in test mode** → **Enable**
5. Copy URL database Anda, contoh:
   ```
   https://money-alfian-abc123-default-rtdb.asia-southeast1.firebasedatabase.app
   ```
6. Buka `index.html`, cari baris ini:
   ```javascript
   const FIREBASE_URL = "GANTI_DENGAN_URL_FIREBASE_ANDA";
   ```
7. Ganti dengan URL database Anda → **Save**

> ✅ Selesai! Data kini otomatis tersimpan dan tersinkronisasi secara online.

---

## 📖 Cara Pakai

### 1. Daftar & Login
- Buka `login.html` → klik **"Daftar dulu"**
- Masukkan username (min. 3 karakter) dan password
- Klik **"Daftar Akun"** → Login dengan akun baru

### 2. Catat Transaksi
- Klik menu **Input Data** (ikon +)
- Pilih jenis: **Pemasukan** atau **Pengeluaran**
- Isi nominal, keterangan, dan tanggal
- Klik **"Simpan Data"**

### 3. Lihat Analisa
- Klik menu **Analisa** (ikon grafik)
- Lihat bar chart perbandingan pemasukan vs pengeluaran
- Baca narasi analisa kondisi keuangan otomatis

### 4. Tanya AI
- Klik menu **Tanya AI** (ikon bintang)
- Ketik pertanyaan seputar keuangan Anda
- AI akan menjawab berdasarkan data keuangan Anda

### 5. Download Laporan (PDF & CSV)
- Klik menu **Laporan** (ikon dokumen)
- Klik tombol **"Ekspor Tabel PDF"** untuk format laporan dokumen resmi
- Klik tombol **"Ekspor Tabel CSV"** untuk format spreadsheet Excel yang rapi dan lengkap

---

## 🌐 Demo

> 🔗 **Live Demo:** `https://USERNAME_ANDA.github.io/money-alfian` *(setelah deploy)*

Akun demo untuk mencoba:
```
Username : demo
Password : demo123
```

---

## 📸 Screenshot

| Dashboard | Input Transaksi | Tanya AI |
|-----------|----------------|----------|
| ![Dashboard](.github/screenshots/dashboard.png) | ![Input](.github/screenshots/input.png) | ![AI](.github/screenshots/ai.png) |

| Analisa Grafik | Laporan PDF | Pengaturan |
|----------------|-------------|------------|
| ![Analisa](.github/screenshots/analisa.png) | ![Laporan](.github/screenshots/laporan.png) | ![Settings](.github/screenshots/settings.png) |

> *Screenshot menyusul setelah deploy*

---

## 🗺️ Roadmap

- [x] Dashboard ringkasan keuangan
- [x] Input & hapus transaksi
- [x] Grafik analitik (Chart.js)
- [x] Asisten AI (Google Gemini)
- [x] Ekspor laporan PDF berformat tabel rapi & berwarna
- [x] Ekspor laporan CSV terstruktur (kompatibel Excel)
- [x] Dark mode
- [x] Multi bahasa (ID/EN)
- [x] Cloud storage (Firebase)
- [x] Multi-user system
- [ ] Notifikasi pengingat pengeluaran
- [ ] Fitur budgeting / anggaran bulanan
- [ ] Kategori transaksi (makanan, transportasi, dll)
- [ ] Export ke Excel / CSV
- [ ] Aplikasi mobile (PWA)

---

## 🤝 Kontribusi

Kontribusi sangat terbuka! Silakan ikuti langkah berikut:

1. **Fork** repository ini
2. Buat branch fitur baru
   ```bash
   git checkout -b fitur/nama-fitur-baru
   ```
3. Commit perubahan Anda
   ```bash
   git commit -m "feat: tambah fitur nama-fitur-baru"
   ```
4. Push ke branch
   ```bash
   git push origin fitur/nama-fitur-baru
   ```
5. Buat **Pull Request**

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License** — bebas digunakan, dimodifikasi, dan didistribusikan dengan mencantumkan kredit.

Lihat file [LICENSE](LICENSE) untuk detail lengkap.

---

## 📞 Kontak

<div align="center">

**Alfian Widhi**

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6285732491409)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/USERNAME_ANDA)

📱 **WA:** [085732491409](https://wa.me/6285732491409)  
🎓 **Prodi:** Teknik Informatika — Semester 4  
📚 **Mata Kuliah:** Pemrograman Web

</div>

---

<div align="center">

**Money Alfian** — *Kelola keuanganmu dengan cerdas & mudah* 💜

⭐ **Jangan lupa beri bintang jika project ini bermanfaat!** ⭐

<br/>

*Made with ❤️ by Alfian Widhi*

</div>

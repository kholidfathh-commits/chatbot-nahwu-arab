# 🕌 Abu Nahwiy — Chatbot Pembelajaran Nahwu & Sharaf

Chatbot pembelajaran **tata bahasa Arab (nahwu & sharaf)** berbasis AI. Chatbot
ini berperan sebagai **"Abu Nahwiy"**, seorang guru yang ramah dan sabar untuk
pemula yang baru belajar bahasa Arab.

Tersedia dalam **dua versi**:
- 💻 **Versi Terminal** (`chatbot.py`) — antarmuka percakapan di terminal.
- 🌐 **Versi Web** (`app.py`) — antarmuka chat modern di browser, mirip aplikasi website.

Dibuat sebagai proyek **Ujian Akhir Semester (UAS)** — Program Studi Pendidikan
Bahasa Arab.

---

## 👤 Identitas Mahasiswa

- **Nama:** Muhammad Kholid Fathurrohman
- **NIM:** 1232030143

---

## 🎯 Maharah & Level

- **Maharah:** Nahwu/Sharaf (tata bahasa Arab)
- **Level target pengguna:** Pemula

**Alasan pemilihan:** Nahwu dan sharaf adalah fondasi utama dalam memahami
bahasa Arab. Banyak pemula kesulitan karena kaidahnya terasa abstrak dan jarang
ada teman untuk bertanya kapan saja. Chatbot ini hadir sebagai "ustaz pribadi"
yang siap menjelaskan kaidah, menguraikan i'rab, men-tashrif kata kerja, dan
memberi latihan soal — dengan bahasa Indonesia yang sederhana dan contoh Arab
yang selalu berharakat agar mudah dibaca pemula.

---

## 🤖 Layanan API yang Digunakan

Chatbot ini menggunakan **Groq API** (gratis) dengan model `openai/gpt-oss-120b`.
Groq dipilih karena cepat, gratis, dan mudah didaftarkan tanpa kartu kredit.
Jika ingin respons lebih cepat dan lebih hemat, ganti model menjadi
`openai/gpt-oss-20b` di file `persona.py`.

> 🔒 API key disimpan di file `.env` dan **tidak diunggah ke GitHub** (lihat
> `.gitignore`). Pada versi web pun, API key tetap aman di sisi server dan tidak
> pernah terlihat di browser.

---

## ✨ Fitur

- 💬 **Dua antarmuka:** terminal (wajib) dan web modern (responsif, tampilan menarik)
- 🧠 Riwayat percakapan dalam satu sesi (chatbot mengingat konteks obrolan)
- 📚 **4 mode belajar** yang berbeda:
  1. **📖 Penjelasan Kaidah** — menjelaskan kaidah nahwu/sharaf
  2. **🔍 I'rab Kalimat** — menguraikan kedudukan tiap kata dalam kalimat
  3. **🔄 Tashrif (Sharaf)** — menampilkan tashrif kata kerja (madhi, mudhari', amr)
  4. **✏️ Latihan Soal** — memberi soal latihan dan mengoreksi jawaban
- 👋 Pesan pembuka (greeting) khas dari persona Abu Nahwiy
- 🚪 Perintah keluar kapan saja (versi terminal: `keluar` / `exit` / `quit`)
- 🔄 Pindah mode tanpa menutup aplikasi
- 🖌️ Tampilan web dengan dukungan teks Arab (RTL) dan render rapi
- 🛡️ Penanganan error yang rapi (tidak crash saat koneksi/API bermasalah)

---

## ⚙️ Cara Instalasi & Menjalankan

### 1. Siapkan Python
Pastikan Python **versi 3.8 ke atas** sudah terpasang:
```bash
python --version
```

### 2. Clone repositori ini
```bash
git clone https://github.com/USERNAME/chatbot-nahwu-arab.git
cd chatbot-nahwu-arab
```

### 3. Install library yang dibutuhkan
```bash
pip install -r requirements.txt
```

### 4. Siapkan API key
Daftar gratis dan ambil API key di **https://console.groq.com/keys**, lalu:
```bash
# Salin template menjadi file .env
cp .env.example .env
```
Buka file `.env`, isi API key kamu:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Jalankan aplikasi

**Versi Terminal:**
```bash
python chatbot.py
```

**Versi Web:**
```bash
python app.py
```
Lalu buka browser ke **http://127.0.0.1:5000**

---

## 🖥️ Contoh Penggunaan (Terminal)

```
Pilih mode belajar:
  1. 📖  Penjelasan Kaidah
  2. 🔍  I'rab Kalimat
  3. 🔄  Tashrif (Sharaf)
  4. ✏️  Latihan Soal
  5. 🚪 Keluar
Pilihan kamu (1-5): 1

Kamu: apa itu mubtada dan khabar?
Abu Nahwiy: ...penjelasan lengkap dengan contoh berharakat...
```

> 📸 _Tips: tambahkan screenshot tampilan terminal dan web di sini untuk nilai tambah._

---

## 📁 Struktur Proyek

```
chatbot-nahwu-arab/
├── chatbot.py          # Aplikasi versi terminal
├── app.py              # Aplikasi versi web (Flask)
├── persona.py          # Persona & mode belajar (dipakai bersama)
├── templates/
│   └── index.html      # Tampilan antarmuka web
├── requirements.txt    # Daftar library Python
├── .env.example        # Template variabel lingkungan
├── .gitignore          # Menyembunyikan .env dari Git
└── README.md           # Dokumentasi proyek
```

---

## 📝 Catatan

- File `.env` berisi API key **tidak boleh** diunggah ke GitHub (sudah diatur di `.gitignore`).
- Bila muncul error nama model, ganti nilai `MODEL` di `persona.py` dengan model
  Groq lain yang tersedia, misalnya `openai/gpt-oss-20b`
  (daftar lengkap: https://console.groq.com/docs/models).
- Versi web memuat font & pustaka tampilan dari internet (CDN), jadi pastikan
  perangkat terhubung internet saat menjalankannya.

---

_Semoga menjadi amal ilmu yang bermanfaat._ 🤲

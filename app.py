"""
Abu Nahwiy - Chatbot Pembelajaran Nahwu & Sharaf (VERSI WEB)
==============================================================================
Proyek UAS - Program Studi Pendidikan Bahasa Arab

Versi web dari Abu Nahwiy menggunakan Flask. Antarmuka chat tampil di browser
dengan desain modern. API key tetap AMAN di sisi server (dibaca dari .env), jadi
tidak pernah terlihat di browser.

Cara menjalankan:
    python app.py
Lalu buka di browser:  http://127.0.0.1:5000
"""

import os
import sys

# --- Cek kelengkapan library lebih dulu ---
try:
    import requests
    from flask import Flask, request, jsonify, render_template
    from dotenv import load_dotenv
except ImportError:
    print("Library belum lengkap. Jalankan dulu perintah ini di terminal:")
    print("    pip install -r requirements.txt")
    sys.exit(1)

# Persona, mode belajar, dan konfigurasi API diambil dari persona.py
from persona import PERSONA, MODES, API_URL, MODEL

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)


@app.route("/")
def index():
    """Menampilkan halaman utama (antarmuka chat)."""
    return render_template("index.html", modes=MODES)


@app.route("/chat", methods=["POST"])
def chat():
    """Menerima pesan dari browser, meneruskan ke AI, mengembalikan jawaban."""
    if not API_KEY:
        return jsonify(
            {
                "reply": "⚠️ API key belum diatur. Salin file .env.example menjadi "
                ".env lalu isi GROQ_API_KEY (gratis dari "
                "https://console.groq.com/keys), kemudian jalankan ulang."
            }
        )

    data = request.get_json(force=True)
    mode_key = str(data.get("mode", "1"))
    history = data.get("history", [])  # daftar {role, content}, termasuk pesan terbaru

    mode = MODES.get(mode_key, MODES["1"])

    # Susun percakapan: system prompt (persona + mode) lalu riwayat percakapan.
    messages = [{"role": "system", "content": PERSONA + "\n" + mode["instruksi"]}]
    messages.extend(history)

    try:
        resp = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={"model": MODEL, "messages": messages, "temperature": 0.6},
            timeout=60,
        )
        resp.raise_for_status()
        reply = resp.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError:
        reply = (
            f"⚠️ Kesalahan dari server API (kode {resp.status_code}). "
            "Coba cek kembali API key atau nama model."
        )
    except requests.exceptions.RequestException:
        reply = "⚠️ Gagal terhubung ke API. Coba lagi sebentar."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    print("=" * 55)
    print("  Abu Nahwiy (versi web) berjalan!")
    print("  Buka di browser: http://127.0.0.1:5000")
    print("  Tekan CTRL+C untuk berhenti.")
    print("=" * 55)
    app.run(debug=True, port=5000)

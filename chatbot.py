"""
Abu Nahwiy - Chatbot Pembelajaran Nahwu & Sharaf (VERSI TERMINAL)
==============================================================================
Proyek UAS - Program Studi Pendidikan Bahasa Arab

Chatbot tutor tata bahasa Arab (nahwu & sharaf) untuk PEMULA, dijalankan lewat
terminal. Persona & mode belajar diatur di file persona.py, koneksi AI memakai
Groq API.

Cara menjalankan:  python chatbot.py
"""

import os
import sys

# --- Cek kelengkapan library lebih dulu ---
# Supaya tidak muncul error panjang kalau ada library yang belum di-install.
try:
    import requests
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
except ImportError:
    print("Library belum lengkap. Jalankan dulu perintah ini di terminal:")
    print("    pip install -r requirements.txt")
    sys.exit(1)

# Persona, mode belajar, dan konfigurasi API diambil dari persona.py
from persona import PERSONA, MODES, API_URL, MODEL


# ============================================================================
# KONFIGURASI
# ============================================================================
load_dotenv()  # membaca API key dari file .env
API_KEY = os.getenv("GROQ_API_KEY")
console = Console()


# ============================================================================
# FUNGSI INTI
# ============================================================================
def panggil_ai(messages):
    """Mengirim seluruh percakapan ke API lalu mengembalikan jawaban teks."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"model": MODEL, "messages": messages, "temperature": 0.6}
    try:
        resp = requests.post(API_URL, headers=headers, json=data, timeout=60)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError:
        return (
            f"[Maaf, ada kesalahan dari server API (kode {resp.status_code}). "
            "Coba cek kembali API key atau nama model.]"
        )
    except requests.exceptions.RequestException:
        return "[Maaf, gagal terhubung ke internet/API. Coba lagi sebentar.]"


def greeting():
    """Pesan pembuka dari persona chatbot."""
    console.print(
        Panel.fit(
            "[bold green]السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ![/bold green]\n\n"
            "Saya [bold]Abu Nahwiy[/bold], teman belajar "
            "[bold]tata bahasa Arab[/bold] (nahwu & sharaf) untuk pemula.\n"
            "Yuk belajar pelan-pelan, insya Allah bisa!",
            title="🕌  Abu Nahwiy",
            border_style="green",
        )
    )


def tampilkan_menu():
    """Menampilkan menu mode dan mengembalikan pilihan user."""
    console.print("\n[bold cyan]Pilih mode belajar:[/bold cyan]")
    for kunci, mode in MODES.items():
        console.print(f"  [bold]{kunci}[/bold]. {mode['ikon']}  {mode['nama']}")
    console.print("  [bold]5[/bold]. 🚪 Keluar")
    return console.input("[yellow]Pilihan kamu (1-5): [/yellow]").strip()


def jalankan_mode(kunci):
    """Menjalankan satu sesi percakapan pada mode terpilih.

    Mengembalikan 'menu' (kembali ke menu) atau 'keluar' (berhenti).
    """
    mode = MODES[kunci]
    console.print(
        Panel(mode["pembuka"], title=f"Mode: {mode['nama']}", border_style="cyan")
    )
    console.print(
        "[dim](ketik 'menu' untuk ganti mode, 'keluar' untuk berhenti)[/dim]\n"
    )

    # Riwayat percakapan dalam satu sesi mode (dikirim utuh ke API tiap giliran).
    messages = [{"role": "system", "content": PERSONA + "\n" + mode["instruksi"]}]

    while True:
        user = console.input("[bold blue]Kamu:[/bold blue] ").strip()

        if user.lower() in ("keluar", "exit", "quit"):
            return "keluar"
        if user.lower() in ("menu", "/menu"):
            return "menu"
        if not user:
            continue

        messages.append({"role": "user", "content": user})
        with console.status("[green]Abu Nahwiy sedang berpikir...[/green]"):
            jawaban = panggil_ai(messages)
        messages.append({"role": "assistant", "content": jawaban})

        console.print(
            Panel(Markdown(jawaban), title="🧑‍🏫  Abu Nahwiy", border_style="green")
        )


def main():
    greeting()

    # Bila API key belum diisi, beri petunjuk setup lalu berhenti.
    if not API_KEY:
        console.print(
            Panel(
                "[red]API key belum diatur![/red]\n\n"
                "1. Salin file [bold].env.example[/bold] menjadi [bold].env[/bold]\n"
                "2. Isi [bold]GROQ_API_KEY[/bold] dengan API key kamu\n"
                "   (gratis dari https://console.groq.com/keys)\n"
                "3. Jalankan lagi: [bold]python chatbot.py[/bold]",
                title="Perlu Setup Dulu",
                border_style="red",
            )
        )
        return

    # Loop utama: tampilkan menu, jalankan mode, ulangi.
    while True:
        pilihan = tampilkan_menu()
        if pilihan == "5" or pilihan.lower() in ("keluar", "exit", "quit"):
            break
        if pilihan in MODES:
            if jalankan_mode(pilihan) == "keluar":
                break
        else:
            console.print("[red]Pilihan tidak ada. Ketik angka 1-5.[/red]")

    console.print(
        "\n[bold green]جَزَاكَ اللهُ خَيْرًا![/bold green] "
        "Sampai jumpa, semangat belajar! 👋"
    )


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        console.print("\n[dim]Keluar. Sampai jumpa![/dim]")

import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(1411012173)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1411012173)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Pembisuan anggota grup untuk bergabung dengan satu channel sebelum mengirim pesan ke dalam grup.\nSaya akan membisukan anggota jika mereka tidak bergabung dengan Channel Anda dan memberi tahu mereka untuk bergabung ke Channel dan menyuarakan diri mereka sendiri dengan menekan tombol.__",
        
        "**Pengaturan**\n__Pertama-tama tambahkan saya di grup sebagai admin dengan izin pengguna larangan dan di channel sebagai admin.\nCatatan: Hanya pemilik grup yang dapat mengatur saya dan saya akan meninggalkan obrolan jika saya bukan admin dalam obrolan.__",
        
        "**Perintah**\n__/ForceSubscribe - Untuk mendapatkan pengaturan saat ini.\n/ForceSubscribe no/off/disable - Untuk mematikan ForceSubscribe.\n/ForceSubscribe {channel username} - Untuk mengaktifkan dan menyiapkan channel.\n/ForceSubscribe clear - Untuk mengaktifkan semua anggota yang saya bisukan.\n\nCatatan: /FSub adalah perintah singkat /ForceSubscribe__",
        
        "**Developed by viperadnan**\n\n**Dihosting dan diterjemahkan ke Indonesia dari ❤️ @indoloaderproject **"
      ]

      START_MSG = "**Hai [{}](tg://user?id={})**\n__Saya dapat membisukan anggota untuk bergabung dengan satu channel agar mereka dapat dengan bebas berbicara diobrolan.\nPelajari lebih lanjut dengan /help__"
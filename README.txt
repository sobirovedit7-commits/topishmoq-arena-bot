TOPISHMOQ ARENA — /start bot

Bu loyiha /start bosilganda banner rasmi, xush kelibsiz matni va “🎮 O‘yinga kirish” tugmasini yuboradi.

MUHIM:
- BotFather tokenini hech kimga yubormang va kod ichiga yozmang.
- Hosting sozlamalarida Environment Variable qo‘shing:
  Name: BOT_TOKEN
  Value: BotFather bergan token
- Start tugmasidagi Web App tugmasi WEBAPP_URL manzilini ochadi.
- Bot doimiy ishlashi uchun uni internetdagi Python worker/background service sifatida deploy qilish kerak; telefon/Termuxda ishlatish shart emas.

Fayllar:
- bot.py — bot kodi
- banner.png — rasm
- requirements.txt — kerakli kutubxonalar

Hozircha bu bot faqat /start xabarini yuboradi. O‘yin sayti va Supabase bilan bog‘lanish alohida sozlanadi.

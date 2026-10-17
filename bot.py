import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = "https://dapper-bubblegum-396206.netlify.app"

WELCOME = (
    "🧠 <b>TOPISHMOQ ARENA 🏆</b>\n\n"
    "Assalomu alaykum! Xush kelibsiz! 👋\n\n"
    "🧩 Qiziqarli topishmoqlarni yeching va bilimingizni sinang!\n"
    "⭐ Har bir to‘g‘ri javob uchun +1 ball oling.\n"
    "🏆 TOP 100 reytingiga kirib, eng kuchli o‘yinchilar bilan bellashing!\n\n"
    "👇 O‘yinni boshlash uchun pastdagi tugmani bosing!"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🎮 O‘yinga kirish", web_app=WebAppInfo(url=WEBAPP_URL))
    ]])
    chat = update.effective_chat
    if not chat:
        return
    image_path = os.path.join(os.path.dirname(__file__), "banner.png")
    if os.path.exists(image_path):
        with open(image_path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=chat.id,
                photo=photo,
                caption=WELCOME,
                parse_mode="HTML",
                reply_markup=keyboard,
            )
    else:
        await context.bot.send_message(
            chat_id=chat.id,
            text=WELCOME,
            parse_mode="HTML",
            reply_markup=keyboard,
        )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing. Add your Telegram bot token in hosting Variables.")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Prende il token da variabile d'ambiente (TELEGRAM_BOT_TOKEN)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Ciao, il bot è attivo!")

def main():
    if not TOKEN:
        raise ValueError("❌ Manca la variabile TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

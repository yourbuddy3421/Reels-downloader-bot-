import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

AD_MESSAGE = "\n\n🔸 *Sponsored by XYZ*\n🔥 Get more tools at: t.me/YourSponsor"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to @downloaderprox_bot!\n\nJust send me any Instagram Reel link to download." + AD_MESSAGE, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "instagram.com" in text:
        await update.message.reply_text("⏬ Downloading your reel, please wait...")

        # Dummy download simulation (replace with real link or API)
        download_url = "https://example.com/reel.mp4"
        await update.message.reply_video(video=download_url, caption="✅ Here is your downloaded reel!" + AD_MESSAGE, parse_mode="Markdown")
    else:
        await update.message.reply_text("❌ Please send a valid Instagram reel link.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    app.run_polling()

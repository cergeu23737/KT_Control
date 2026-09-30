from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 KT Control\n"
        "версия: 0.1.0\n\n"
        "система управления KT готова к работе."
    )


def register(app):
    app.add_handler(CommandHandler("start", start))

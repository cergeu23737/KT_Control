from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"твой Telegram ID: {update.effective_user.id}"
    )


def register(app):
    app.add_handler(CommandHandler("id", get_id))

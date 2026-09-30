from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from config import OWNER_ID


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not user or user.id != OWNER_ID:
        await update.message.reply_text(
            "⛔ у вас нет доступа к этой команде."
        )
        return

    await update.message.reply_text(
        "🛑 система остановлена."
    )


def register(app):
    app.add_handler(CommandHandler("stop", stop))

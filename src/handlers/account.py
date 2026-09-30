from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from accounts import create_account


async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id

    kt_id = create_account(telegram_id)

    await update.message.reply_text(
        "🆔 ваш KT ID:\n"
        f"{kt_id}\n\n"
        "аккаунт KT prod создан."
    )


def register(app):
    app.add_handler(CommandHandler("account", account))

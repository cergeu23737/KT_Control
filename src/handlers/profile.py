from telegram import Update
from telegram.ext import ContextTypes

from database import get_connection


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id

    connection = get_connection()

    user = connection.execute(
        """
        SELECT kt_id, role, created_at
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,)
    ).fetchone()

    connection.close()

    if not user:
        await update.message.reply_text(
            "❌ у вас ещё нет KT ID.\n"
            "используйте /account"
        )
        return

    kt_id, role, created_at = user

    await update.message.reply_text(
        "👤 ваш KT аккаунт\n\n"
        f"🆔 KT ID: {kt_id}\n"
        f"👤 роль: {role}\n"
        f"📅 создан: {created_at}"
    )

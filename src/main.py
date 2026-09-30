from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN, APP_NAME, VERSION


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 {APP_NAME}\n"
        f"Версия: {VERSION}\n\n"
        "Система управления KT готова к работе."
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print(f"{APP_NAME} {VERSION} запущен.")

    app.run_polling()


if __name__ == "__main__":
    main()

from telegram.ext import (
    Application,
    CommandHandler,
)

from config import BOT_TOKEN, APP_NAME, VERSION
from database import init_db

from handlers.account import account
from handlers.profile import profile


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("account", account))
    app.add_handler(CommandHandler("profile", profile))

    print(f"{APP_NAME} {VERSION} запущен.")

    app.run_polling()


if __name__ == "__main__":
    main()

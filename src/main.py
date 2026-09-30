from telegram.ext import Application

from config import BOT_TOKEN, APP_NAME, VERSION
from database import init_db
from handler_loader import load_handlers


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    load_handlers(app)

    print(f"{APP_NAME} {VERSION} запущен.")

    app.run_polling()


if __name__ == "__main__":
    main()

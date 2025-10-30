import logging
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8331773910:AAE4HqX39-LYlHm1ZirdSqrnjZuut7trE1w"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = (
        f"👋 Привет, {user.first_name}!\n\n"
        "🎯 Для работы с мини-приложением перейдите по ссылке:\n"
        "🔗 t.me/hollyapp_bot/parser\n\n"
        "✨ Бот успешно запущен и готов к работе!\n"
        "Если ссылка не открывается, скопируйте ее и вставьте в браузер."
    )
    
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = (
        "📖 Доступные команды:\n"
        "/start - Запустить бота и получить ссылку на мини-приложение\n"
        "/help - Получить справку\n\n"
        "🔗 Ссылка на мини-приложение:\n"
        "t.me/hollyapp_bot/parser"
    )
    await update.message.reply_text(help_text)

async def post_init(application: Application) -> None:
    """Функция, выполняемая после инициализации бота"""
    # Устанавливаем команды бота для меню
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Помощь"),
    ]
    await application.bot.set_my_commands(commands)
    logger.info("Бот успешно инициализирован и готов к работе!")

def main() -> None:
    """Основная функция запуска бота"""
    try:
        # Создаем Application с обработчиком post_init
        application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))

        # Запускаем бота
        logger.info("Запуск бота...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "6723754514:AAFCcFtSWwwtrEC4B6u6G_I0ViB7PVKTZCg"
USERNAME_BOT = "@hisayanguwu_bot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Gunakan /help untuk melihat apa yang saya bisa.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Coba sapa saya... saya akan membalas..')

async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text

    print('Text diterima :', text_diterima)

    if 'halo' in text_diterima:
        return await update.message.reply_text('halo juga..')
    if "asalamualaikum" in text_diterima:
        return await update.message.reply_text('Maaf saya kristen..')
    if "siapa kamu?" in text_diterima:
        return await update.message.reply_text('Saya adalah bot')
    else:
        return await update.message.reply_text('Kamu bicara apa? Saya tidak paham')

async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("User mengirim gambar...")
    return await update.message.reply_text('Wah gambar anda bagus sekali')

async def location_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("User mengirim lokasi...")
    latlong = f'{str(update.message.location.latitude)},{update.message.location.latitude}'
    return await update.message.reply_text(f'https://maps.google.com/?q={latlong}')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'error: {context.error}')

if __name__ == '__main__':
    print('Bot dimulai...')
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))

    application.add_handler(MessageHandler(filters.TEXT, text_message))
    application.add_handler(MessageHandler(filters.PHOTO, photo_message))
    application.add_handler(MessageHandler(filters.LOCATION, location_message))

    application.add_error_handler(error)

    print('Pooling...')
    application.run_polling(poll_interval=1)
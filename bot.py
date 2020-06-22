import os
from uuid import uuid4
from telegram import InlineQueryResultPhoto
from telegram.ext import Updater, InlineQueryHandler
from make_brotendo import make_brotendo
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def query(update, context):
    q = update.inline_query.query
    id = update.inline_query.id
    results = [
        InlineQueryResultPhoto(
            id=uuid4(),
            photo_url='https://e3a4a858e59f.ngrok.io/?caption='+q)  # Update to actual url once noah fixes the stupid firewall
    ]
    os.remove(f'{id}.png')
    context.bot.answer_inline_query(update.inline_query.id, results)

updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)
dispatcher = updater.dispatcher
query_handler = InlineQueryHandler(query)
dispatcher.add_handler(query_handler)
print('running')
updater.start_polling()

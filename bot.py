import os

import urllib
from telegram import InlineQueryResultPhoto
from telegram.ext import Updater, InlineQueryHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def query(update, context):
    q = update.inline_query.query
    if len(q) == 0:
        return
    print(q)
    output = 'https://e3a4a858e59f.ngrok.io/'+urllib.parse.quote(q) +'.jpg'  # Update to actual url once noah fixes the stupid firewall
    results = list()
    results.append(
        InlineQueryResultPhoto(
            id='ranchitup',
            thumb_url=output,
            photo_url=output,
            photo_width=1920,
            photo_height=1080
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results, cache_time=15)


updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)
dispatcher = updater.dispatcher
query_handler = InlineQueryHandler(query)
dispatcher.add_handler(query_handler)
print('running')
updater.start_polling()

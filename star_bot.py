from decouple import config
import requests
from telegram.ext import Updater, MessageHandler, Filters

token = config('TOKEN')
request_url = config('REQUEST_URL')

updater = Updater(token=token)
dispatcher = updater.dispatcher


def handler(bot, update):
    api = requests.get(url=request_url)
    response = api.json()
    request = update.message.text
    result = ""
    for data in response:
        if data['name'] != request:
            continue
        result = "Repository '%s' has %d Stars." % (request, data['stargazers_count'])
        break
    if result == "":
        result = "Repository not found."
    update.message.reply_text(result)


dispatcher.add_handler(MessageHandler(Filters.text, handler))

updater.start_polling()
updater.idle()

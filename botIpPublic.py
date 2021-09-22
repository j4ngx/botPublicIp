#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
This a bot telegram for get my public ip
"""

import logging
import json

from requests import get
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def getIpPublic():
	response = get("https://api.ipify.org/?format=json")
	res = response.json()
	ipPublic = res['ip']
	return ipPublic

def ip_command(update: Update, context:CallbackContext):
	if str(update.message.chat_id) == '576384241':
		ip=getIpPublic()
		update.message.reply_text('This is your Public Ip ')
		update.message.reply_text(ip)
	else:
		update.message.reply_text('Invalid user')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2029674413:AAGCmkQSjXmgC94Sn7Yo5j2mwKdUFlspO4E")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ip",ip_command))



    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
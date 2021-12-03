from slackbot.bot import respond_to, listen_to
import re

@respond_to('\こんにちは')
def konnitiha(message, *something):
    message.reply('こんにちは。')

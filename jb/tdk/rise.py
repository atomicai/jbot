import os
from html import escape

import dotenv
from flask import Flask
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from teleflask import Teleflask
from teleflask.messages import HTMLMessage, TextMessage

dotenv.load_dotenv()

app = Flask(__name__)

bot = Teleflask(os.environ.get("BOT_TOKEN"), app)

# Register the /start command
@bot.on_command("start")
def start(update, text):
    # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
    # text is the text after the command. Can be empty. Type is str.
    return TextMessage("<b>Hello!</b> Thanks for using @" + bot.username + "!", parse_mode="html")


@bot.on_message("text")
def response(update, text):
    # // smart search
    query = "<QUERY>"
    response = "<ANSWER>"
    #
    return HTMLMessage(
        f"<u>Query:</u> {escape(query)}\n---\n<u>Response:</u> {escape(response)}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👌", callback_data="confirm_true"),
                ],
                [
                    InlineKeyboardButton('🤦', callback_data="confirm_false"),
                ],
            ]
        ),
    )

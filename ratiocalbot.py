import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

state = "waiting for AB"

@bot.message_handler(commands=['start'])
def start_message(message):
    global state
    state = "waiting for AB"
    bot.send_message(message.chat.id, "Hello! I am a ratio calculator. \nThis calculator is based on the formula A:B = C:D. \nLet's start by inputting A:B")

@bot.message_handler(content_types=['text'])
def input_value(message):
    global state, AB, C, A, B
    if state == "waiting for AB":
        try:
            AB = message.text
            A, B = map(float, AB.split(":"))
            state = "waiting for C"
            bot.send_message(message.chat.id, "Now input C")
        except:
            bot.send_message(message.chat.id, "Invalid ratio format. Please input in the format of A:B")
    elif state == "waiting for C":
        try:
            C = float(message.text)
            B = float(B)
            D = (C * B) / A
            D = round(D, 2) # round off D to 2 decimal places
            bot.send_message(message.chat.id, f"D = {D}")
            state = "waiting for AB"
            AB = None
            C = None
        except ValueError:
            bot.send_message(message.chat.id, "Invalid value for C. Please input a number")


bot.polling()




from random import randint, shuffle
from telegram import ext
# import os
# import dbm

#dat = dbm.open("main.db", "c")
#os.system("attrib +s +h main.db")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sim = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-',
        '+', '=', '{', '[', '}', ']', '|', '\\', ';', ':', '"', "'", '<', ',', ".", "<", '>', '/', '?']
alphabet_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def generate(update, context):
    passwords = ""
    for a in range(randint(1, 5)):
        passwords = passwords + (alphabet[randint(0, len(alphabet) - 1)])
    for b in range(randint(1, 5)):
        passwords = passwords + str((str(num[randint(0, len(num) - 1)])))
    for c in range(randint(1, 5)):
        passwords = passwords + (sim[randint(0, len(sim) - 1)])
    for d in range(randint(1, 5)):
        passwords = passwords + (alphabet_capital[randint(0, len(alphabet_capital) - 1)])
    new_passwords = list(passwords)
    for e in range(randint(1, 5)):
        shuffle(new_passwords)
    passwords = "".join(new_passwords)
    context.bot.send_message(chat_id=update.message.chat_id, text=passwords)

def store(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="CURRENTLY UNDER CONSTRUCTION!!!")

def view(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="CURRENTLY UNDER CONSTRUCTION!!!")

update = ext.Updater("1496732681:AAGqrEunWseS6eb8i5ygNPfC8dcoV-izOFk", use_context=True)
dispatch = update.dispatcher


ghandler = ext.CommandHandler("generate", generate)
shandler = ext.CommandHandler("store", store)
vhandler = ext.CommandHandler("view", view)
dispatch.add_handler(ghandler)
dispatch.add_handler(shandler)
dispatch.add_handler(vhandler)
update.start_polling()



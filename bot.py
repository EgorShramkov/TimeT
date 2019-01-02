import telepot
from telepot.loop import MessageLoop

TOKEN = '789534735:AAGB2gCq7AtVpQ-wLM3akVAKsCjsa4DTPEQ'

bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    answer = text
    bot.sendMessage(chat_id, "это написали вы: {}".format(answer))
    doc = open('/home/egor/primer.txt', 'rb')
    bot.sendDocument(chat_id, doc)
    bot.sendDocument(chat_id, "FILEID")

MessageLoop(bot, handle).run_as_thread()


# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break

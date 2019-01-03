import telepot
from telepot.loop import MessageLoop
from telepot.loop import OrderedWebhook

TOKEN = '770819628:AAFoiGUAI3mrhwgTSwCc_Ps0WPigqhslDBI'

bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    doc = open('/home/egor/primer.txt', 'rb')
    bot.sendDocument(chat_id, doc)
    bot.sendDocument(chat_id, "FILEID")
MessageLoop(bot, handle).run_as_thread()
webhook = OrderedWebhook(bot, handle)
webhook.run_as_thread()

while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break

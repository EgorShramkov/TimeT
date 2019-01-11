import telepot
from telepot.loop import MessageLoop
from telepot.loop import OrderedWebhook

TOKEN = '770819628:AAFoiGUAI3mrhwgTSwCc_Ps0WPigqhslDBI'
START = 'start.txt'
chat_id = '-1001368635243'
tt6 = 'NewTimeT6.txt'

bot = telepot.Bot(TOKEN)

while 1 > 0:
 ST = open(START,'r')
 test = ST.read(1)
 ST.close()
 if test == '1': 
    doc = open(tt6, 'r')
    bot.sendDocument(chat_id, doc)
    doc.close()
    ST = open(START,'w')
    ST.write('0')
    ST.close()

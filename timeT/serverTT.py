import telepot
from telepot.loop import MessageLoop
import tornado.ioloop
import tornado.web
import os
import re


chat_id_5 = '-1001368635243'
chat_id_6 = '-1001358437243'
chat_id_7 = '-1001445027946'
chat_id_8 = '-1001477729156'
chat_id_9 = '-1001364844389' 
chat_id_10 = '-1001208856454'
chat_id_11 = '-1001261650074'


TOKEN = '770819628:AAFoiGUAI3mrhwgTSwCc_Ps0WPigqhslDBI'
admin_password = "123456"
port = 8888
db_path = "./timetable.db"



Monlesson5 =['1_5_1','2_5_1','3_5_1','4_5_1','5_5_1','6_5_1','7_5_1']           
NewMonLesson5 = ['','','','','','','']

Monlesson6=['1_6_1','2_6_1','3_6_1','4_6_1','5_6_1','6_6_1','7_6_1', '8_6_1']
NewMonLesson6 = ['','','','','','','','']

Monlesson7=['1_7_1','2_7_1','3_7_1','4_7_1','5_7_1','6_7_1','7_7_1', '8_7_1']
NewMonLesson7 = ['','','','','','','','']

Monlesson8=['1_8_1','2_8_1','3_8_1','4_8_1','5_8_1','6_8_1','7_8_1', '8_8_1']
NewMonLesson8 = ['','','','','','','','']

Monlesson9=['1_9_1','2_9_1','3_9_1','4_9_1','5_9_1','6_9_1','7_9_1', '8_9_1', '9_9_1', '10_9_1']
NewMonLesson9 = ['','','','','','','', '', '', '']

Monlesson10=['1_10_1','2_10_1','3_10_1','4_10_1','5_10_1','6_10_1','7_10_1', '8_10_1', '9_10_1', '10_10_1']
NewMonLesson10 = ['','','','','','','','', '', '']

Monlesson11=['1_11_1','2_11_1','3_11_1','4_11_1','5_11_1','6_11_1','7_11_1', '8_11_1', '9_11_1', '10_11_1']
NewMonLesson11 = ['','','','','','','','', '', '']

pages = {
    "main_page": "./html/MAinEgor.html",
    "admin_page_mon": "./html/day1.html"
}

def save_send(bot, self,NewLesson, i, Lesson, NOM, MAX, chat_id):
     text = 'Измененное расписание для ' + NOM +' класса: \n'
     while i < MAX:
        lesson = self.get_argument(Lesson[i])
        if lesson == '1':
            NewLesson[i] = 'Математика\n' 
        if lesson == '2':
            NewLesson[i] = 'Английский язык\n'
        if lesson == '3':
            NewLesson[i] = 'Русский язык\n'
        if lesson == '4':
            NewLesson[i] = 'География\n'
        if lesson == '5':
            NewLesson[i] = 'Информатика\n'
        if lesson == '6': 
            NewLesson[i] = 'История\n'       
        if lesson == '7': 
            NewLesson[i] = 'Обществознание\n'
        if lesson == '8':    
            NewLesson[i] = 'Литература\n'
        if lesson == '9':
            NewLesson[i] = 'Физкультура\n'
        if lesson == '10':
            NewLesson[i] = 'Биология\n'
        if lesson == '11':
            NewLesson[i] = 'Второй иностранный\n'
        if lesson == '12':
            NewLesson[i] = 'Английский язык\n'
        if lesson == '13':
            NewLesson[i] = '"-"\n'
        if lesson == '14':
            NewLesson[i] = 'Риторика\n'
        if lesson == '15':
            NewLesson[i] = 'Алгебра\n'
        if lesson == '16':
            NewLesson[i] = 'Геометрия\n' 
        if lesson == '17':
            NewLesson[i] = 'ОГЭ Био/Ист/Англ\n'
        if lesson == '18':
            NewLesson[i] = 'ОГЭ Мат1/Мат2\n'
        if lesson == '19':
            NewLesson[i] = 'ОГЭ Общ\n'  
        if lesson == '20':
            NewLesson[i] = 'ОГЭ география/инф\n'  
        if lesson == '21':
            NewLesson[i] = 'ОГЭ русский\n'  
        if lesson == '22':
            NewLesson[i] = 'ОГЭ Геом Р/История Р/Лит-ра Р/Био Р\n'  
        if lesson == '23':
            NewLesson[i] = 'Геом Р/Биология Р\n'  
        if lesson == '24':
            NewLesson[i] = 'Общ(экон)/ русский ЕГЭ\n'  
        if lesson == '25':
            NewLesson[i] = 'Обществознание Р\n'  
        if lesson == '26':
            NewLesson[i] = 'Алгебра Р/ Геометрия Б\n'  
        if lesson == '27':
            NewLesson[i] = 'Алг Р/ Ист Р/ Лит Р/ Хим Р\n'
        if lesson == '28':
            NewLesson[i] = 'Инф Р/Физ-ра\n'  
        if lesson == '29':
            NewLesson[i] = 'Алгебра Б/Франц Р/Инф Р\n'  
        if lesson == '30':
            NewLesson[i] = 'Геом Р/ История Р/ Литература р\n'  
        if lesson == '31':
            NewLesson[i] = 'Алг Р/ Фин гр/ Общ Р\n'  
        if lesson == '32':
            NewLesson[i] = 'История Р/Б\n'  
        if lesson == '33':
            NewLesson[i] = 'Общество Р/Б\n'  
        if lesson == '34':
            NewLesson[i] = 'Алг Р/История Р\n'  
        if lesson == '35':
            NewLesson[i] = 'Алг Р/Лит Р/Олимп История\n'  
        if lesson == '36':
            NewLesson[i] = 'Алг Б/ Инф Р\n'  
        if lesson == '37':
            NewLesson[i] = 'Геом Б/ Инф Б/ Франц Р\n'  
        if lesson == '38':
            NewLesson[i] = 'Алгебра Р/Литература Р\n'  
        if lesson == '39':
            NewLesson[i] = 'Алгебра Р/ История Р\n'  
        if lesson == '40':
            NewLesson[i] = 'Общ Р/Био Р/Физ-ра\n'  
        if lesson == '41':
            NewLesson[i] = 'Литература/ Физ-ра\n'  

    
        x=str(i+1)
        text = text + x + '. ' + NewLesson[i]
        i=i+1
     bot.sendMessage(chat_id, text)
     return

class MainHandler(tornado.web.RequestHandler):
     def get(self):
        self.render(pages["main_page"], message="Доброго времени суток")
 

class PageHandler(tornado.web.RequestHandler):
     def post(self):
        password = self.get_argument("password", None)
        if not password == admin_password:
            self.render(pages["main_page"], message="Неверный пароль, попробуйте, пожалуйста, ещё раз.")
        elif  password == admin_password: 
            self.render(pages["admin_page_mon"], message_admin="Хорошей работы.")


class SaveHandler(tornado.web.RequestHandler):       
  
     def post(self):   

        bot = telepot.Bot(TOKEN)
        NOM = 'пятого'
        i=0
        MAX = 7
        save_send(bot, self,NewMonLesson5, i, Monlesson5, NOM, MAX, chat_id_5);
        
        NOM = 'шестого'
        i=0
        MAX = 8
        save_send(bot, self,NewMonLesson6, i, Monlesson6, NOM, MAX, chat_id_6);

        NOM = 'седьмого'
        i=0
        MAX = 8
        save_send(bot, self,NewMonLesson7, i, Monlesson7, NOM, MAX, chat_id_7);

        NOM = 'восьмого'
        i=0
        MAX = 8
        save_send(bot, self,NewMonLesson8, i, Monlesson8, NOM, MAX, chat_id_8);
        
        NOM = 'девятого'
        i=0
        MAX = 10
        save_send(bot, self,NewMonLesson9, i, Monlesson9, NOM, MAX, chat_id_9);
        
        NOM = 'десятого'
        i=0
        MAX = 10
        save_send(bot, self,NewMonLesson10, i, Monlesson10, NOM, MAX, chat_id_10);
        
        NOM = 'одинадцатого'
        i=0
        MAX = 10
        save_send(bot, self,NewMonLesson11, i, Monlesson11, NOM, MAX, chat_id_11);
        
        self.render(pages["main_page"], message="Спасибо за работу, изменения внесены.")
        


class BackHandler(tornado.web.RequestHandler):                   

     def post(self):   
        self.render(pages["main_page"], message="Спасибо за работу.")
        
               
def make_app():
    return tornado.web.Application([
         (r"/", MainHandler),
         (r"/back", BackHandler),
         (r"/page", PageHandler),
         (r"/save", SaveHandler),
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)



tornado_app = make_app()



if __name__ == "__main__":
    app = make_app()  # Создаем серверное приложение
    app.listen(port)  # Даем приложению сетевой порт для работы
    tornado.ioloop.IOLoop.current().start()  # Запускаем приложение


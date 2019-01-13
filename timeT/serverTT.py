import telepot
from telepot.loop import MessageLoop
import tornado.ioloop
import tornado.web
import os
import re


chat_id = '-1001368635243'
TOKEN = '770819628:AAFoiGUAI3mrhwgTSwCc_Ps0WPigqhslDBI'
admin_password = "123456"
port = 8888
db_path = "./timetable.db"



Monlesson6 =['1_5_1','2_5_1','3_5_1','4_5_1','5_5_1','6_5_1','7_5_1']           
NewMonLesson6 = ['','','','','','','','']





pages = {
    "main_page": "./html/MAinEgor.html",
    "admin_page_mon": "./html/day1.html"
}

def save(lesson, i):
        if lesson == '1':
            NewMonLesson6[i] = 'Математика\n' 
        if lesson == '2':
            NewMonLesson6[i] = 'Английский язык\n'
        if lesson == '3':
            NewMonLesson6[i] = 'Русский язык\n'
        if lesson == '4':
            NewMonLesson6[i] = 'География\n'
        if lesson == '5':
            NewMonLesson6[i] = 'Информатика\n'
        if lesson == '6': 
            NewMonLesson6[i] = 'История\n'       
        if lesson == '7': 
            NewMonLesson6[i] = 'Обществознание\n'
        if lesson == '8':    
            NewMonLesson6[i] = 'Литература\n'
        if lesson == '9':
            NewMonLesson6[i] = 'Физкультура\n'
        if lesson == '10':
            NewMonLesson6[i] = 'Биология\n'
        if lesson == '11':
            NewMonLesson6[i] = 'Второй иностранный\n'
        if lesson == '12':
            NewMonLesson6[i] = 'Английский язык\n'
        if lesson == '13':
            NewMonLesson6[i] = '"-"\n'
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
        lesson1_5_1 = self.get_argument("1_5_1",None)  
        self.render(pages["admin_page_mon"], message_admin="Изменения внесены") 


class BackHandler(tornado.web.RequestHandler):                   

     def post(self):   
        bot = telepot.Bot(TOKEN)
        text = 'Измененное расписание для шестого класса: \n'
        i=0
        while i < 7:
           lsn = self.get_argument(Monlesson6[i])
           save(lsn, i);
           x = str(i + 1)
           text = text + x + '. ' + NewMonLesson6[i]
           i=i+1
        bot.sendMessage(chat_id, text)
        self.render(pages["main_page"], message="Спасибо, изменения отправлены") 

        
               
def make_app():
    return tornado.web.Application([
         (r"/", MainHandler),
         (r"/back", BackHandler),
         (r"/page", PageHandler),
         (r"/save", SaveHandler),
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)


if __name__ == "__main__":
    app = make_app()  # Создаем серверное приложение
    app.listen(port)  # Даем приложению сетевой порт для работы
    tornado.ioloop.IOLoop.current().start()  # Запускаем приложение


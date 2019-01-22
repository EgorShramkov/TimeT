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

NOM_mass = ['пятого','шестого','седьмого','восьмого','девятого','десятого','одиннадцатого']
chat_id_mass = ['-1001368635243','-1001358437243','-1001445027946','-1001477729156','-1001364844389', '-1001208856454','-1001261650074']
MAX_mass=[7,8,8,8,10,10,10]
Monlesson =['1_5_1','2_5_1','3_5_1','4_5_1','5_5_1','6_5_1','7_5_1',
'1_6_1','2_6_1','3_6_1','4_6_1','5_6_1','6_6_1','7_6_1', '8_6_1','1_7_1','2_7_1','3_7_1','4_7_1','5_7_1','6_7_1','7_7_1', '8_7_1','1_8_1','2_8_1','3_8_1','4_8_1','5_8_1','6_8_1','7_8_1', '8_8_1','1_9_1','2_9_1','3_9_1','4_9_1','5_9_1','6_9_1','7_9_1', '8_9_1', '9_9_1','10_9_1','1_10_1','2_10_1','3_10_1','4_10_1','5_10_1','6_10_1','7_10_1', '8_10_1','9_10_1','10_10_1', '1_11_1','2_11_1','3_11_1','4_11_1','5_11_1','6_11_1','7_11_1', '8_11_1', '9_11_1', '10_11_1']          
NewMonLesson = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','', '', '', '','','','','','','','','', '', '','','','','','','','','', '', '']

allLesson = ['Математика\n', 'Английский язык\n', 'Русский язык\n', 'География\n', 'Информатика\n', 'История\n', 'Обществознание\n', 'Литература\n', 'Физкультура\n', 'Биология\n', 'Второй иностранный\n', 'Английский язык\n', '"-"\n', 'Риторика\n' , 'Алгебра\n', 'Геометрия\n' , 'ОГЭ Био/Ист/Англ\n', 'ОГЭ Мат1/Мат2\n', 'ОГЭ Общ\n', 'ОГЭ география/инф\n', 'ОГЭ русский\n', 'Геом Р/История Р/Лит-ра Р/Био Р\n' , 'Геом Р/Биология Р\n' , 'Общ(экон)/ русский ЕГЭ\n',  'Обществознание Р\n', 'Алгебра Р/ Геометрия Б\n', 'Алг Р/ Ист Р/ Лит Р/ Хим Р\n', 'Инф Р/Физ-ра\n', 'Алгебра Б/Франц Р/Инф Р\n', 'Геом Р/ История Р/ Литература р\n', 'Алг Р/ Фин гр/ Общ Р\n' , 'История Р/Б\n', 'Общество Р/Б\n','Алг Р/История Р\n', 'Алг Р/Лит Р/Олимп История\n' , 'Алг Б/ Инф Р\n'  
, 'Геом Б/ Инф Б/ Франц Р\n', 'Алгебра Р/Литература Р\n' , 'Алгебра Р/ История Р\n', 'Общ Р/Био Р/Физ-ра\n' ,'Литература/ Физ-ра\n', 'Физика\n', 'Химия\n']  

    

pages = {
    "main_page": "./html/MAinEgor.html",
    "admin_page_mon": "./html/day1.html",
    "admin_page_tue": "./html/day2.html",
    "admin_page_wed": "./html/day3.html",
    "admin_page_thu": "./html/day4.html",
    "admin_page_fri": "./html/day5.html",
    "all_day": "./html/all_day.html"
}

def save_send(bot, self,NewLesson,Lesson, NOM, MAX_mass,chat_id, day, allLesson):
   nclas=0
   nlesson=0
   for nclas in range(7):
     i=0
     MAX = MAX_mass[nclas]     
     text = 'Измененное расписание для ' + NOM[nclas] +' класса на ' + day + ' \n'
     while i < MAX:
        lesson = self.get_argument(Lesson[nlesson])
        les = int(lesson)
        les = les - 1
        y=0
        while y < 42:
            if les == y:
               NewLesson[nlesson] = allLesson[y]
               y = 42
            y = y + 1       
        x=str(i+1)
        text = text + x + '. ' + NewLesson[nlesson]   
        i=i+1 
        nlesson = nlesson + 1
     chat_id = chat_id_mass[nclas]
     bot.sendMessage(chat_id, text)
     
   return



class MainHandler(tornado.web.RequestHandler):
     def get(self):
        self.render(pages["main_page"], message="Доброго времени суток")
 


class Page_all_dayHandler(tornado.web.RequestHandler):
     def post(self):
        password = self.get_argument("password", None)
        if not password == admin_password:
            self.render(pages["main_page"], message="Неверный пароль, попробуйте, пожалуйста, ещё раз.")
        elif  password == admin_password: 
            self.render(pages["all_day"], message="Выберети, пожалуйста, день в который будут вноситься изменения.")


class SaveMonHandler(tornado.web.RequestHandler):       
  
     def post(self):   
        day = 'понедельник'
        bot = telepot.Bot(TOKEN)    
        save_send(bot,self,NewMonLesson,Monlesson,NOM_mass,MAX_mass,chat_id_5,day,allLesson);        
        self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")
        

class BackHandler(tornado.web.RequestHandler):                   

     def post(self):   
        self.render(pages["all_day"], message="Спасибо за работу.")
        

class MonPageHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["admin_page_mon"], admin_message="Можете вносить изменения. Не забудьте нажать кнопку 'отправить'.")

class TuePageHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["admin_page_tue"], admin_message="Можете вносить изменения. Не забудьте нажать кнопку 'отправить'.")


class WedPageHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["admin_page_wed"], admin_message="Можете вносить изменения. Не забудьте нажать кнопку 'отправить'.")


class ThuPageHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["admin_page_thu"], admin_message="Можете вносить изменения. Не забудьте нажать кнопку 'отправить'.")


class FriPageHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["admin_page_fri"], admin_message="Можете вносить изменения. Не забудьте нажать кнопку 'отправить'.")




        
        

def make_app():
    return tornado.web.Application([
         (r"/", MainHandler),
         (r"/mon_page", MonPageHandler),
         (r"/tue_page", TuePageHandler),
         (r"/wed_page", WedPageHandler),
         (r"/thu_page", ThuPageHandler),
         (r"/fri_page", FriPageHandler),
         (r"/back", BackHandler),
         (r"/page_all_day", Page_all_dayHandler),
         (r"/save_mon", SaveMonHandler),
         (r"/save_tue", SaveTueHandler),
         (r"/save_wed", SaveWedHandler),
         (r"/save_thu", SaveThuHandler),
         (r"/save_fri", SaveFriHandler),
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)


tornado_app = make_app()


if __name__ == "__main__":
    app = make_app()  # Создаем серверное приложение
    app.listen(port)  # Даем приложению сетевой порт для работы
    tornado.ioloop.IOLoop.current().start()  # Запускаем приложение


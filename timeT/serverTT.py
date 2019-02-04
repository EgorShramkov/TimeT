import telepot
from telepot.loop import MessageLoop
import tornado.ioloop
import tornado.web
import os
import json
import re

admin_password = 'Password' in os.environ
chat_id_teachers='-1001284124826'
options = json.load(open('TimeT/timeT/json/options.json', 'r'))
subjects = json.load(open('./json/subjects.json', 'r'))
days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
TOKEN = 'TOKEN' in os.environ
port = 8888
day_adm= ["NON", "понедельник" , "вторник", "среду", "четверг", "пятницу"]
NOM_mass = ['5-ого','6-ого','7-ого','8-ого','9-oго','10-ого','11-ого']
chat_id_mass = ['-1001368635243','-1001358437243','-1001445027946','-1001477729156','-1001364844389', '-1001208856454','-1001261650074']
Monlesson =['1_5_1','2_5_1','3_5_1','4_5_1','5_5_1','6_5_1','7_5_1',
'1_6_1','2_6_1','3_6_1','4_6_1','5_6_1','6_6_1','7_6_1', '8_6_1','1_7_1','2_7_1','3_7_1','4_7_1','5_7_1','6_7_1','7_7_1', '8_7_1','1_8_1','2_8_1','3_8_1','4_8_1','5_8_1','6_8_1','7_8_1', '8_8_1','1_9_1','2_9_1','3_9_1','4_9_1','5_9_1','6_9_1','7_9_1', '8_9_1', '9_9_1','10_9_1','1_10_1','2_10_1','3_10_1','4_10_1','5_10_1','6_10_1','7_10_1', '8_10_1','9_10_1','10_10_1', '1_11_1','2_11_1','3_11_1','4_11_1','5_11_1','6_11_1','7_11_1', '8_11_1', '9_11_1', '10_11_1']          
Tuelesson =['1_5_2','2_5_2','3_5_2','4_5_2','5_5_2','6_5_2','7_5_2',
'1_6_2','2_6_2','3_6_2','4_6_2','5_6_2','6_6_2','7_6_2','8_6_2','1_7_2','2_7_2','3_7_2','4_7_2','5_7_2','6_7_2','7_7_2', '8_7_2','1_8_2','2_8_2','3_8_2','4_8_2','5_8_2','6_8_2','7_8_2', '8_8_2','1_9_2','2_9_2','3_9_2','4_9_2','5_9_2','6_9_2','7_9_2', '8_9_2', '9_9_2','10_9_2','1_10_2','2_10_2','3_10_2','4_10_2','5_10_2','6_10_2','7_10_2', '8_10_2','9_10_2','10_10_2', '1_11_2','2_11_2','3_11_2','4_11_2','5_11_2','6_11_2','7_11_2', '8_11_2', '9_11_2', '10_11_2']          
Wedlesson =['1_5_3','2_5_3','3_5_3','4_5_3','5_5_3','6_5_3','7_5_3',
'1_6_3','2_6_3','3_6_3','4_6_3','5_6_3','6_6_3','7_6_3', '8_6_3','1_7_3','2_7_3','3_7_3','4_7_3','5_7_3','6_7_3','7_7_3', '8_7_3','1_8_3','2_8_3','3_8_3','4_8_3','5_8_3','6_8_3','7_8_3', '8_8_3','1_9_3','2_9_3','3_9_3','4_9_3','5_9_3','6_9_3','7_9_3', '8_9_3', '9_9_3','10_9_3','1_10_3','2_10_3','3_10_3','4_10_3','5_10_3','6_10_3','7_10_3', '8_10_3','9_10_3','10_10_3', '1_11_3','2_11_3','3_11_3','4_11_3','5_11_3','6_11_3','7_11_3', '8_11_3','9_11_3', '10_11_3']          
Thulesson =['1_5_4','2_5_4','3_5_4','4_5_4','5_5_4','6_5_4','7_5_4',
'1_6_4','2_6_4','3_6_4','4_6_4','5_6_4','6_6_4','7_6_4', '8_6_4','1_7_4','2_7_4','3_7_4','4_7_4','5_7_4','6_7_4','7_7_4', '8_7_4','1_8_4','2_8_4','3_8_4','4_8_4','5_8_4','6_8_4','7_8_4', '8_8_4','1_9_4','2_9_4','3_9_4','4_9_4','5_9_4','6_9_4','7_9_4', '8_9_4', '9_9_4','10_9_4','1_10_4','2_10_4','3_10_4','4_10_4','5_10_4','6_10_4','7_10_4', '8_10_4','9_10_4','10_10_4', '1_11_4','2_11_4','3_11_4','4_11_4','5_11_4','6_11_4','7_11_4', '8_11_4', '9_11_4', '10_11_4']          
Frilesson =['1_5_5','2_5_5','3_5_5','4_5_5','5_5_5','6_5_5','7_5_5',
'1_6_5','2_6_5','3_6_5','4_6_5','5_6_5','6_6_5','7_6_5', '8_6_5','1_7_5','2_7_5','3_7_5','4_7_5','5_7_5','6_7_5','7_7_5', '8_7_5','1_8_5','2_8_5','3_8_5','4_8_5','5_8_5','6_8_5','7_8_5', '8_8_5','1_9_5','2_9_5','3_9_5','4_9_5','5_9_5','6_9_5','7_9_5', '8_9_5', '9_9_5','10_9_5','1_10_5','2_10_5','3_10_5','4_10_5','5_10_5','6_10_5','7_10_5', '8_10_5','9_10_5','10_10_5', '1_11_5','2_11_5','3_11_5','4_11_5','5_11_5','6_11_5','7_11_5', '8_11_5', '9_11_5', '10_11_5']          
NewLesson = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','', '', '', '','','','','','','','','', '', '','','','','','','','','', '', '']
allLesson = ['Математика\n', 'Английский язык\n', 'Русский язык\n', 'География\n', 'Информатика\n', 'История\n', 'Обществознание\n', 'Литература\n', 'Физкультура\n', 'Биология\n', 'Второй иностранный\n', 'Английский язык\n', '"-"\n', 'Риторика\n' , 'Алгебра Р/Б \n', 'Геометрия Р/Б\n' , 'ОГЭ Био/Ист/Англ\n', 'ОГЭ Мат1/Мат2\n', 'ОГЭ Общ\n', 'ОГЭ география/инф\n', 'ОГЭ русский\n', 'Геом Р/История Р/Лит-ра Р/Био Р\n' , 'Геом Р/Биология Р\n' , 'Общ(экон)/ русский ЕГЭ\n',  'Обществознание Р\n', 'Алгебра Р/ Геометрия Б\n', 'Алг Р/ Ист Р/ Лит Р/ Хим Р\n', 'Инф Р/Физ-ра\n', 'Алгебра Б/Франц Р/Инф Р\n', 'Геом Р/ История Р/ Литература р\n', 'Алг Р/ Фин гр/ Общ Р\n' , 'История Р/Б\n', 'Общество Р/Б\n','Алг Р/История Р\n', 'Алг Р/Лит Р/Олимп История\n' , 'Алг Б/ Инф Р\n'  
, 'Геом Б/ Инф Б/ Франц Р\n', 'Алгебра Р/Литература Р\n' , 'Алгебра Р/ История Р\n', 'Общ Р/Био Р/Физ-ра\n' ,'Литература/ Физ-ра\n', 'Физика\n', 'Химия\n', 'Алгебра Р/ Алгебра Б \n']  

    

pages = {
    "main_page": "./html/MAinEgor.html",
    "admin_page": "./html/day.html",
    "all_day": "./html/all_day.html"
}

def save_send(bot, self,NewLesson,Lesson, NOM, MAX_mass,chat_id_mass, day, allLesson, chat_id_teachers):
   nclas=0
   nlesson=0   
   text_teacher = 'Изменное расписание на ' + day + '\n'
   for nclas in range(7):
     i=0
     MAX = MAX_mass[nclas]     
     text ='Измененное расписание для ' + NOM[nclas] +' класса на ' + day + ' \n'
     text_teacher =text_teacher +  '  ' +  'Для ' + NOM[nclas] +  'класса: \n' 
     while i < MAX:
        lesson = self.get_argument(Lesson[nlesson])
        les = int(lesson)
        les = les - 1
        y=0
        while y < 44:
            if les == y:
               NewLesson[nlesson] = allLesson[y]
               y = 42
            y = y + 1       
        x=str(i+1)
        text = text  +  '  '+ x + '. ' + NewLesson[nlesson]
        text_teacher = text_teacher +  '    '+ x + '. ' + NewLesson[nlesson]
        i=i+1 
        nlesson = nlesson + 1
     chat_id = chat_id_mass[nclas]
     bot.sendMessage(chat_id, text)
   bot.sendMessage(chat_id_teachers, text_teacher)
     
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


class SaveHandler(tornado.web.RequestHandler):      
            
     def post(self):  
        day_id_str = self.get_argument("day_id", default=0)
        day_id = int(day_id_str)
        day = days[day_id]
        bot = telepot.Bot(TOKEN) 
        if day_id == 0:
            self.render(pages["all_day"], message="Ошибка.Пишите Егору.")
        if day_id == 1:
            save_send(bot,self,NewLesson,Monlesson,NOM_mass,MAX_mass,chat_id_mass,day,allLesson, chat_id_teachers);
            self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")
        if day_id == 2:
            save_send(bot,self,NewLesson,Tuelesson,NOM_mass,MAX_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")
        if day_id == 3:
            save_send(bot,self,NewLesson,Wedlesson,NOM_mass,MAX_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")
        if day_id == 4:
            save_send(bot,self,NewLesson,Thulesson,NOM_mass,MAX_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")
        if day_id == 5:   
            save_send(bot,self,NewLesson,Frilesson,NOM_mass,MAX_mass,chat_id_mass,day,allLesson,  chat_id_teachers);        
            self.render(pages["all_day"], message="Спасибо за работу, изменения внесены.")

class BackHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["all_day"], message="Спасибо за работу.")

class BackMainHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["main_page"], message="Спасибо за работу.")                

class PageHandler(tornado.web.RequestHandler):                   
     def post(self): 
        day = self.get_argument("day_id", default=0)
        defaults = json.load(open('./json/defaults.json', 'r'))
        template = {
            'days':days,
            'day': day,
            'subjects': subjects,
            'defaults' : defaults,
            'options' : options
        }
        self.render('index.html', **template)

        

def make_app():
    return tornado.web.Application([
         (r"/back_main", BackMainHandler),
         (r"/", MainHandler),
         (r"/page", PageHandler),
         (r"/back", BackHandler),
         (r"/page_all_day", Page_all_dayHandler),
         (r"/sent", SentHandler),
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)


tornado_app = make_app()


if __name__ == "__main__":
    app = make_app()  # Создаем серверное приложение
    app.listen(port)  # Даем приложению сетевой порт для работы
    tornado.ioloop.IOLoop.current().start()  # Запускаем приложение


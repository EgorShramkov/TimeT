import telepot
from telepot.loop import MessageLoop
import tornado.ioloop
import tornado.web 
import os
import json   
import re
import redis

r = redis.from_url(os.environ.get("REDIS_URL"))
absolute_path = os.path.dirname(os.path.abspath(__file__))
options_path = absolute_path + '/options.json'
subjects_path = absolute_path + '/subjects.json'
admin_password =  os.getenv('Password')
TOKEN = os.getenv('TOKEN')
chat_id_teachers='-1001284124826'
options = json.load(open(options_path, 'r'))
subjects = json.load(open(subjects_path, 'r'))
days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
port = 8888
day_adm= ["NON", "понедельник" , "вторник", "среду", "четверг", "пятницу"]
NOM_mass = ['5-ого','6-ого','7-ого','8-ого','9-oго','10-ого','11-ого']
chat_id_mass = ['-1001368635243','-1001358437243','-1001445027946','-1001477729156','-1001364844389', '-1001208856454','-1001261650074']
Monlesson =['1_5_1','1_5_2','1_5_3','1_5_4','1_5_5','1_5_6','1_5_7','1_5_8','1_5_9','1_5_10','1_6_1','1_6_2','1_6_3','1_6_4','1_6_5','1_6_6','1_6_7','1_6_8','1_6_9','1_6_10','1_7_1','1_7_2','1_7_3','1_7_4','1_7_5','1_7_6','1_7_7','1_7_8','1_7_9','1_7_10','1_8_1','1_8_2','1_8_3','1_8_4','1_8_5','1_8_6','1_8_7','1_8_8','1_8_9','1_8_10','1_9_1','1_9_2','1_9_3','1_9_4','1_9_5','1_9_6','1_9_7','1_9_8','1_9_9','1_9_10','1_10_1','1_10_2','1_10_3','1_10_4','1_10_5','1_10_6','1_10_7','1_10_8','1_10_9','1_10_10','1_11_1','1_11_2','1_11_3','1_11_4','1_11_5','1_11_6','1_11_7','1_11_8','1_11_9','1_11_10']
Tuelesson =['2_5_1','2_5_2','2_5_3','2_5_4','2_5_5','2_5_6','2_5_7','2_5_8','2_5_9','2_5_10','2_6_1','2_6_2','2_6_3','2_6_4','2_6_5','2_6_6','2_6_7','2_6_8','2_6_9','2_6_10','2_7_1','2_7_2','2_7_3','2_7_4','2_7_5','2_7_6','2_7_7','2_7_8','2_7_9','2_7_10','2_8_1','2_8_2','2_8_3','2_8_4','2_8_5','2_8_6','2_8_7','2_8_8','2_8_9','2_8_10','2_9_1','2_9_2','2_9_3','2_9_4','2_9_5','2_9_6','2_9_7','2_9_8','2_9_9','2_9_10','2_10_1','2_10_2','2_10_3','2_10_4','2_10_5','2_10_6','2_10_7','2_10_8','2_10_9','2_10_10','2_11_1','2_11_2','2_11_3','2_11_4','2_11_5','2_11_6','2_11_7','2_11_8','2_11_9','2_11_10']
Wedlesson =['3_5_1','3_5_2','3_5_3','3_5_4','3_5_5','3_5_6','3_5_7','3_5_8','3_5_9','3_5_10','3_6_1','3_6_2','3_6_3','3_6_4','3_6_5','3_6_6','3_6_7','3_6_8','3_6_9','3_6_10','3_7_1','3_7_2','3_7_3','3_7_4','3_7_5','3_7_6','3_7_7','3_7_8','3_7_9','3_7_10','3_8_1','3_8_2','3_8_3','3_8_4','3_8_5','3_8_6','3_8_7','3_8_8','3_8_9','3_8_10','3_9_1','3_9_2','3_9_3','3_9_4','3_9_5','3_9_6','3_9_7','3_9_8','3_9_9','3_9_10','3_10_1','3_10_2','3_10_3','3_10_4','3_10_5','3_10_6','3_10_7','3_10_8','3_10_9','3_10_10','3_11_1','3_11_2','3_11_3','3_11_4','3_11_5','3_11_6','3_11_7','3_11_8','3_11_9','3_11_10']
Thulesson =['4_5_1','4_5_2','4_5_3','4_5_4','4_5_5','4_5_6','4_5_7','4_5_8','4_5_9','4_5_10','4_6_1','4_6_2','4_6_3','4_6_4','4_6_5','4_6_6','4_6_7','4_6_8','4_6_9','4_6_10','4_7_1','4_7_2','4_7_3','4_7_4','4_7_5','4_7_6','4_7_7','4_7_8','4_7_9','4_7_10','4_8_1','4_8_2','4_8_3','4_8_4','4_8_5','4_8_6','4_8_7','4_8_8','4_8_9','4_8_10','4_9_1','4_9_2','4_9_3','4_9_4','4_9_5','4_9_6','4_9_7','4_9_8','4_9_9','4_9_10','4_10_1','4_10_2','4_10_3','4_10_4','4_10_5','4_10_6','4_10_7','4_10_8','4_10_9','4_10_10','4_11_1','4_11_2','4_11_3','4_11_4','4_11_5','4_11_6','4_11_7','4_11_8','4_11_9','4_11_10']
Frilesson =['5_5_1','5_5_2','5_5_3','5_5_4','5_5_5','5_5_6','5_5_7','5_5_8','5_5_9','5_5_10','5_6_1','5_6_2','5_6_3','5_6_4','5_6_5','5_6_6','5_6_7','5_6_8','5_6_9','5_6_10','5_7_1','5_7_2','5_7_3','5_7_4','5_7_5','5_7_6','5_7_7','5_7_8','5_7_9','5_7_10','5_8_1','5_8_2','5_8_3','5_8_4','5_8_5','5_8_6','5_8_7','5_8_8','5_8_9','5_8_10','5_9_1','5_9_2','5_9_3','5_9_4','5_9_5','5_9_6','5_9_7','5_9_8','5_9_9','5_9_10','5_10_1','5_10_2','5_10_3','5_10_4','5_10_5','5_10_6','5_10_7','5_10_8','5_10_9','5_10_10','5_11_1','5_11_2','5_11_3','5_11_4','5_11_5','5_11_6','5_11_7','5_11_8','5_11_9','5_11_10']
NewLesson = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','', '', '', '','','','','','','','','', '', '','','','','','','','','', '', '']
allLesson = ["Математика", "Английский язык", "Русский язык", "География", "Информатика", "История", "Обществознание", "Литература", "Физкультура", "Биология", "Второй иностранный", "Английский язык", "'-'", "Риторика" , "Алгебра Р/Б ", "Геометрия Р/Б" , "ОГЭ Био/Ист/Англ", "ОГЭ Мат1/Мат2", "ОГЭ Общ", "ОГЭ география/инф", "ОГЭ русский", "Геом Р/История Р/Лит-ра Р/Био Р" , "Геом Р/Биология Р" , "Общ(экон)/ русский ЕГЭ",  "Обществознание Р", "Алгебра Р/ Геометрия Б", "Алг Р/ Ист Р/ Лит Р/ Хим Р", "Инф Р/Физ-ра", "Алгебра Б/Франц Р/Инф Р", "Геом Р/ История Р/ Литература р", "Алг Р/ Фин гр/ Общ Р" , "История Р/Б", "Общество Р/Б","Алг Р/История Р", "Алг Р/Лит Р/Олимп История" , "Алг Б/ Инф Р"  , "Геом Б/ Инф Б/ Франц Р", "Алгебра Р/Литература Р" , "Алгебра Р/ История Р", "Общ Р/Био Р/Физ-ра" ,"Литература/ Физ-ра", "Физика", "Химия", "Алгебра Р/ Алгебра Б ", "Алгебра", "Геометрия"] 
pages = {
    "admin_page_save": "./html/day_save.html",
    "all_day_save": "./html/all_day_save.html", 
    "main_page": "./html/MAinEgor.html",
    "admin_page": "./html/day.html",
    "allday": "./html/allday.html"
}

def save (day, self):
   for lesson in day:
     r = redis.from_url(os.environ.get("REDIS_URL"))
     check = self.get_argument(lesson)
     r.set(lesson, check) 
   return 
   

def save_send(bot, self,NewLesson,Lesson, NOM, chat_id_mass, day, allLesson, chat_id_teachers):
   nclas=0
   teacher_otvet = 0
   defaults_path = absolute_path + '/defaults.json'
   defaults = json.load(open(defaults_path, 'r'))
   RED = '\033[91m'
   UNDERLINE = '\033[4m'
   BOLD = '\033[1m' 
   nlesson=0    
   otvet = 0
   text_teacher = 'Изменное расписание на ' + day + '\n'
   for nclas in range(7):
     i=0
     MAX= 10     
     text ='Измененное расписание для ' + NOM[nclas] +' класса на ' + day + ' \n'
     text_teacher =text_teacher +  '  ' +  'Для ' + NOM[nclas] +  ' класса: \n' 
     while i < MAX:
        lesson = self.get_argument(Lesson[nlesson])
        les = int(lesson)
        y=0
        ok=0
        while y < 44:
            if les == y:
               NewLesson[nlesson] = allLesson[y]
               y = 44
            y = y + 1    
        if NewLesson[nlesson] != subjects[defaults[Lesson[nlesson]]]:
            otvet= 1
            ok=1
            teacher_otvet= 1
        x=str(i+1)
        if ok == 0:
            text = text  +  '  '+ x + '. ' + NewLesson[nlesson]+'\n'
            text_teacher = text_teacher +  '    '+ x + '. ' + NewLesson[nlesson]+'\n' 
        if ok == 1:
            text = text  +  '  *'+ x + '. '   +NewLesson[nlesson]+'\n'
            otvet= 1  
            text_teacher = text_teacher +  '    *'+ x + '. '+NewLesson[nlesson]+'\n'
            ok=0
        i=i+1 
        nlesson = nlesson + 1
     if otvet == 1:
       otvet = 0
       chat_id= chat_id_mass[nclas]
       bot.sendMessage(chat_id, text)
   if teacher_otvet  == 1:
     bot.sendMessage(chat_id_teachers, text_teacher)
     
   return


class SaveHandler(tornado.web.RequestHandler):
    def post(self):
        day_id_str = self.get_argument("day_id", default=0)
        day_id = int(day_id_str)
        if day_id == 1:
            save(Monlesson,self);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 2:
            save(Tuelesson,self);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 3:
            save(Wedlesson,self);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 4:
            save(Thulesson,self);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 5:   
            save(Frilesson,self);        
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")

    
class MainHandler(tornado.web.RequestHandler):
     def get(self):
        r.set('1_5_1',4)
        r.set('1_5_2',4)
        r.set('1_5_3',4)
        y = r.get('1_5_1')
        z = r.get('1_5_2')
        d = r.get('1_5_3')
        otvet = y + z + d
        self.render(pages["main_page"], message=otvet)

class Page_allday_saveHandler(tornado.web.RequestHandler):
     def post(self):
        self.render(pages["all_day_save"], message="Выберети, пожалуйста, день в который будут вноситься изменения.")
        

class PagealldayHandler(tornado.web.RequestHandler):
     def post(self):
        password = self.get_argument("password", None)
        if not password == admin_password:
            self.render(pages["main_page"], message="Неверный пароль, попробуйте, пожалуйста, ещё раз.")
        elif  password == admin_password: 
            self.render(pages["allday"], message="Выберети, пожалуйста, день в который будут вноситься изменения.")


class SentHandler(tornado.web.RequestHandler):      
            
     def post(self):  
        day_id_str = self.get_argument("day_id", default=0)
        day_id = int(day_id_str)
        day = days[day_id]
        bot = telepot.Bot(TOKEN) 
        if day_id == 0:
            
            self.render(pages["allday"], message="Ошибка.Пишите Егору.")
        if day_id == 1:
            save_send(bot,self,NewLesson,Monlesson,NOM_mass,chat_id_mass,day,allLesson, chat_id_teachers);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 2:
            save_send(bot,self,NewLesson,Tuelesson,NOM_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 3:
            save_send(bot,self,NewLesson,Wedlesson,NOM_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 4:
            save_send(bot,self,NewLesson,Thulesson,NOM_mass,chat_id_mass,day,allLesson,  chat_id_teachers);
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")
        if day_id == 5:   
            save_send(bot,self,NewLesson,Frilesson,NOM_mass,chat_id_mass,day,allLesson,  chat_id_teachers);        
            self.render(pages["allday"], message="Спасибо за работу, изменения внесены.")

class BackHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["allday"], message="Спасибо за работу.")

class BackMainHandler(tornado.web.RequestHandler):                   
     def post(self):   
        self.render(pages["main_page"], message="Спасибо за работу.")                

        
class PageSaveHandler(tornado.web.RequestHandler):                   
     def post(self): 
        r.set=('1_5_1',5)
        day_str = self.get_argument("day_id")
        day = int(day_str)
        template = {
            'days':days,
            'day': day,
            'subjects': subjects,
            'defaults' : r,
            'options' : options
        }
        self.render(pages["admin_page_save"], **template)

        
        
class PageHandler(tornado.web.RequestHandler):                   
     def post(self): 
        default = redis.from_url(os.environ.get("REDIS_URL"))
        r.set=('1_5_1',1)
        day_str = self.get_argument("day_id")
        day = int(day_str)
        template = {
            'days':days,
            'day': day,
            'subjects': subjects,
            'defaults' : r,
            'options' : options
        }
        self.render(pages["admin_page"], **template)

        

def make_app():
    return tornado.web.Application([
         (r"/back_main", BackMainHandler),
         (r"/", MainHandler),
         (r"/save", SaveHandler),
         (r"/page", PageHandler),
         (r"/back", BackHandler),
         (r"/page_save", PageSaveHandler),
         (r"/page_all_day", PagealldayHandler),
         (r"/sent", SentHandler),
         (r"/page_allday_save", Page_allday_saveHandler), 
         (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"})],
    debug=True)


tornado_app = make_app()


if __name__ == "__main__":
    app = make_app()  # Создаем серверное приложение
    app.listen(port)  # Даем приложению сетевой порт для работы
    tornado.ioloop.IOLoop.current().start()  # Запускаем приложение

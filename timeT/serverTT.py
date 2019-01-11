import tornado.ioloop
import tornado.web
import os
import re

admin_password = "123456"
port = 8888
db_path = "./timetable.db"
NewTimeT6 = 'NewTimeT6.txt'
START = 'start.txt'
lesson6 =['1_5_1','2_5_1','3_5_1','4_5_1','5_5_1','6_5_1','7_5_1']           

pages = {
    "main_page": "./html/MAinEgor.html",
    "admin_page_mon": "./html/day1.html"
}

def save(NewTT,lesson):
        if lesson == '1':
            NewTT.write('Математика\n') 
        if lesson == '2':
            NewTT.write('Английский язык\n')
        if lesson == '3':
            NewTT.write('Русский язык\n')
        if lesson == '4':
            NewTT.write('География\n')
        if lesson == '5':
            NewTT.write('Информатика\n')
        if lesson == '6': 
            NewTT.write('История\n')       
        if lesson == '7': 
            NewTT.write('Обществознание\n')
        if lesson == '8':    
            NewTT.write('Литература\n')
        if lesson == '9':
            NewTT.write('Физкультура\n')
        if lesson == '10':
            NewTT.write('Биология\n')
        if lesson == '11':
            NewTT.write('Второй иностранный\n')
        if lesson == '12':
            NewTT.write('Английский язык\n')
        if lesson == '13':
            NewTT.write('"-"\n')
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
        start = open(START, 'w')
        start.write('1')   
        start.close()
        NewTT6 = open(NewTimeT6,'w')        
        NewTT6.write('Измененное расписание для шестого класса\n')
        i=0
        while i < 7:
           lsn = self.get_argument(lesson6[i])
           save(NewTT6,lsn);
           i=i+1
        NewTT6.close()
        self.render(pages["main_page"], message="Спасибо, изменения внесены") 

        
               
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
    tornado.ioloop.IOLoop.current().start() # Запускаем приложениеapp = make_app()  # Создаем серверное приложени
    

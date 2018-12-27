import tornado.ioloop
import tornado.web
import sqlite3
import os

admin_password = "123456"
port = 8888
db_path = "./timetable.db"


           

pages = {
    "main_page": "./html/mainpage1.html",
    "admin_page_mon": "./html/day1.html"
}


class MainHandler(tornado.web.RequestHandler):
     def get(self):
        self.render(pages["main_page"], message="", lesson1_5_1="")
 

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
        lesson1_5_1 = self.get_argument("1_5_1",None)
        if lesson1_5_1 == None:
            self.render(pages["main_page"], message="Ошибка", lesson1_5_1="") 
        if lesson1_5_1 == '1':
            self.render(pages["main_page"], message="", lesson1_5_1="математика") 
        if lesson1_5_1 == '2':
            self.render(pages["main_page"], message="", lesson1_5_1="английский") 
        if lesson1_5_1 == '3':
            self.render(pages["main_page"], message="", lesson1_5_1="русский язык") 
        if lesson1_5_1 == '4':
            self.render(pages["main_page"], message="", lesson1_5_1="география") 
        if lesson1_5_1 == '5':
            self.render(pages["main_page"], message="", lesson1_5_1="информатика") 
        if lesson1_5_1 == '6':
            self.render(pages["main_page"], message="", lesson1_5_1="история") 
        if lesson1_5_1 == '7':
            self.render(pages["main_page"], message="", lesson1_5_1="обществознание") 
        if lesson1_5_1 == '8':
            self.render(pages["main_page"], message="", lesson1_5_1="литература") 
        if lesson1_5_1 == '9':
            self.render(pages["main_page"], message="", lesson1_5_1="биология") 
        if lesson1_5_1 == '10':
            self.render(pages["main_page"], message="", lesson1_5_1="второй иностранный") 
        if lesson1_5_1 == '11':
            self.render(pages["main_page"], message="", lesson1_5_1="английский/информатика") 
        if lesson1_5_1 == '12':
            self.render(pages["main_page"], message="", lesson1_5_1="NON") 
        

               
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


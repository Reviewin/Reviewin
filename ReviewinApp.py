from cProfile import run
from math import fabs
from os import access
from pickle import TRUE
from turtle import onclick
from unittest import removeResult
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton, MDFlatButton, MDFillRoundFlatIconButton, MDRoundFlatButton, MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.icon_definitions import md_icons
from kivy.uix.boxlayout import BoxLayout  
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.swiper import MDSwiper
import json 
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.image import Image
import requests
from kivy.properties import ObjectProperty 
import re 
import json
import random2
import random



pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

#fonts
LabelBase.register(name="OpenSans",fn_regular="OpenSans-Bold.ttf")
LabelBase.register(name="RSlab", fn_regular="RobotoSlab-VariableFont_wght.ttf")
LabelBase.register(name= "Popp",fn_regular="FontsFree-Net-Poppins-Bold.ttf")
LabelBase.register(name= "Inter", fn_regular= "FontsFree-Net-Inter-Regular.ttf") 



Window.size = (360,800)
 
#principale classe de l'application
class ReviewinApp(MDApp):
    def build(self):
        dialog = None
        self.title = "ReviewinApp"
        global sm 
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("accueil.kv"))
        sm.add_widget(Builder.load_file('conditions.kv'))
        sm.add_widget(Builder.load_file("register.kv"))
        sm.add_widget(Builder.load_file("faq.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("User2.kv"))
        sm.add_widget(Builder.load_file("rules.kv"))
        sm.add_widget(Builder.load_file("commentinput.kv"))
        sm.add_widget(Builder.load_file("UserInfo.kv"))
        sm.add_widget(Builder.load_file("recaptcha.kv"))
        return sm

    def on_start(self):
        Clock.schedule_once(self.accueil, 30)
        
    def accueil(*args):
        sm.current = "accueil"

    def color_characters_compteur(self):
        self.theme_cls.primary_palette = "Cyan"
    
    def show_alert_dialog(self):
        dialog = None        
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Exit ?",
                text="Really want to exit ?",
                buttons=[
                    MDFlatButton(
                        text="[u]Sure ! I'll come back ![/u]",
                        theme_text_color="Custom",
                        text_color=[1,1,1,1],
                        on_press= self.go_back()
                    ),
                    MDFlatButton(
                        text="No finally, I prefer to stay.",
                        theme_text_color="Custom",
                        text_color= [1,1,1,1],
                        on_press=  self.stay_app()
                    ),
                ],
            )
        self.dialog.open()
    
    def user2_go(self):
        sm.current = "user2"

    def login_go(self):
        sm.current = "login"
       
    def close_dialog(self, obj):
        self.dialog.dismiss()

    def go_back(self):
        sm.current = "accueil"

    def stay_app(self):
        self.dialog.dismiss()
    
    def go_recaptcha_page(self):
        MDDialog(
            title= "Recaptcha test.",
            text_color= [1,1,1,1],
            theme_text_color= 'Custom',
            Image=[
                Image(
                    source= 'test_recaptcha.png',
                    center_x= self.parent.center_x,
                    center_y= self.parent.center_y

                ),

            ],
            
        ),

    def recaptcha_test(self, image):
        image= [
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
            Image(
                source= 'test_recaptcha.png',
                center_x= self.parent.center_x,
                center_y= self.parent.center_y,   
            ),
        random.choice(image)

        ]
    def password_not_valid(self, password):
        password = self.root.current_screen.ids.password.text
        if len(password) < 8:
            alerte = [
                MDDialog(
                    title= 'Password not valid',
                    text_color= [1,1,1,1],
                    theme_text_color= 'Custom',
                    text= 'Please consider seeing the examples of good password. (But do not take them as password.)',
                    font_name= 'Popp',
                )
            ]



    def check_auth_user(self, e_mail):
        full_name_text = self.root.current_screen.ids.full_name.text
        age = int(self.root.current_screen.ids.age.text)
        e_mail = self.root.current_screen.ids.e_mail.text
        gender = str(self.root.current_screen.gender.text)
        country = self.root.current_screen.country.ids.text 
        pattern_verify = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

        if len(self.root.current_screen.ids.full_name.text) < 4:
            toast("Please enter a valid name.")
        else:
            return True
        if int(self.root.current_screen.ids.age.text)<16:
            toast("You need to be aged of at least sixteen-years-old to use this application.See more at RGPD website.")
        else:
            return True
        if self.root.current_screen.ids.gender.text != "M" or "F":
            toast("You need to mention your gender.")
        else:
            return True
        if re.search(pattern, e_mail):
            return True        
        else:
            toast("Please enter a valid e-mail. If needed, you can check an example of a valid password.")
        if len(country) < 4:
            toast("Country invalid.")
        else:
            return True
        if len(self.root.current_screen.ids.full_name.text) < 4 and int(self.root.current_screen.ids.age.text) and self.root.current_screen.ids.gender.text == 'M' or 'F' and re.search(pattern, e_mail) and len(country) < 4:
            recaptcha_test_succesfull()
        else:
            toast("Please sign up correctly. We advice you to see the register model.")

    def go_back_1(self):
        sm.current = "register"
    
    def test(self):
        if self.root.current_screen.ids.full_name.text == 'something':
            print(json.dumps(self.root.current_screen.ids.full_name.text))
        else:
            print("no")

    def recaptcha_test_succesfull(self):
        #variables de récupérations du text input
        full_name = str(self.root.current_screen.ids.full_name.text)
        gender = str(self.root.current_screen.ids.gender.text)
        age = str(self.root.current_screen.ids.age.text)
        country = str(self.root.current_screen.ids.country.text)
        e_mail = str(self.root.current_screen.ids.e_mail.text)
        password = str(self.root.current_screen.ids.password.text)


        #variable de serializations en objets json
        data_full_name = json.dumps(str(full_name))
        data_gender = json.dumps(str(gender))
        data_age = json.dumps(int(age))
        data_country = json.dumps(str(country))
        data_e_mail = json.dumps(str(e_mail))

        #requete post/signup à l'endpoint de l'API.
        url = 'http://127.0.0.1:2222/test_verification'
        data = {'full_name':json.dumps(full_name), 'age':json.dumps(age), 'country':json.dumps(country), 'e_mail':json.dumps(e_mail), 'gender':json.dumps(gender), 'password':json.dumps(password)}
        response = requests.post(url, json=data)




#fonction de secours dont on aura surement pas besoin p
    def create_user(self):
        full_name = str(self.root.current_screen.ids.full_name.text)
        gender = str(self.root.current_screen.ids.gender.text)
        age = int(self.root.current_screen.ids.age.text)
        country = self.root.current_screen.ids.country.text
        e_mail = self.root.current_screen.ids.e_mail.text
        try:
            connection = httplib.HTTPSConnection('http://localhost:8000/')
            connection.connect()
            connection.request('POST', 'http://127.0.0.1/register/',json.dumps({"full_name":full_name,"e_mail":e_mail,"age":age,"gender":gender,"country":country})), {
                "Content-type": "application/json"
            }
        except:
            MDDialog(
                title= "Error while trying to sign up. Please try gain",
                theme_text_color= 'Custom',
                font_name= "RSlab",
                font_size= "15",
                text_color= [1,1,1,1],
                buttons= [
                    MDFlatButton(
                        text="[u]Try again.[/u]",
                        theme_text_color="Custom",
                        text_color=[1,1,1,1],
                    ),

                ]
            )



        
#if re.search(pattern,full_name_text):
    #something()

        
#classes_de_tous_les_screens    
class Splash(Screen):
    def build(self):
        self.title = "Splash"
        global sp
        sp = Screen()
        sp = Builder.load_file("splash.kv")
        return sp

class Condition(Screen): 
    def build(self):
        self.title = "Conditions d'utilisations"
        global co        
        co = Screen()
        co = Builder.load_file('conditions.kv')
        return co




class Accueil(Screen):
    def build(self):
        self.title = "Accueil"
        global ac
        ac = Screen()
        ac =  Builder.load_file('accueil.kv')
        return ac


class Faq(Screen):
    def build(self):
        self.title = "FAQ"
        global fa
        fa = Screen()
        fa = Builder.load_file("faq.kv")
        return fa


class user(Screen):
    def build(self):
        self.title = "user"
        global us 
        us = Screen()
        us = Builder.load_file("person.kv")
        return us

 
class Rules(Screen):
    def build(self):
        self.title = "rules"
        global ru
        ru = Screen()
        re = Builder.load_file("rules.kv")
        return ru


class Help(Screen):
    def build(self):
        self.title = "help"
        global he
        he = Screen()
        he = Builder.load_file("help.kv")
        return he


class Login(Screen):
    def build(self):
        self.title  ="Login"
        global lo
        lo = Screen()
        lo = Builder.load_file("login.kv")
        return lo


class CommentInput(Screen):
    def build(self):
        self.title = "comment input"
        global comment
        comment = Screen()
        comment  = Builder.load_file("commentinput.kv")
        return comment


class UserInfo(Screen):
    def build(self):
        self.title = "User Informations"
        global UserInfo
        UserInfo  = Screen()
        UserInfo = Builder.load_file("UserInfo.kv")
        return UserInfo


class Recaptcha(Screen):
    def build(self):
        self.title = "Recaptcha"
        global rec
        rec  = Screen()
        rec = Builder.load_file("recaptcha.kv")
        return rec



if __name__=="__main__":
    ReviewinApp().run()












from cProfile import run
from math import fabs
from os import access
from pickle import TRUE
import re
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
from kivymd.app import App

LabelBase.register(name="OpenSans",fn_regular="OpenSans-Bold.ttf")
LabelBase.register(name="RSlab", fn_regular="RobotoSlab-VariableFont_wght.ttf")
LabelBase.register(name= "Popp",fn_regular="FontsFree-Net-Poppins-Bold.ttf")
LabelBase.register(name= "Inter", fn_regular= "FontsFree-Net-Inter-Regular.ttf")

something = True 

Window.size = (360,800)
 
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
        return sm


    def check_register(self, text):
        if len(text) < 5:
            toast("Please register correctly.")
        else:
            return text

    def check_register_e_mail(self, text):
        if not "@" and '.' in text and len(text) < 3:
            toast("Please give a valid e_mail")
        else:
            return text


    def check_register_address(self, text):
        if len(text) < 10:
            toast("Please enter a valid address")
        else:
            return text

    def check_register_password(self, text):
        if len(text) < 8 and not "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in text:
            toast("Your password must contain at least 8 characters and at least one number.")
        else:
            return text

    def on_start(self):
        Clock.schedule_once(self.accueil, 10)
        
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
 
    def check_text(self):
        screen = self.root.get_screen('register')
        e_mail = screen.ids.e_mail.text
        age = screen.ids.age.text
        full_name = screen.ids.full_name.text
        password = screen.ids.password.text
        address = screen.ids.address.text
        if (not '@' and '.' in e_mail) and len(e_mail) < 6:
            toast("Please enter a valid e-mail.")
        else:
            return e_mail
        if len(full_name) < 5:
            toast("Please enter yout full name.")
        else:
            return full_name
        if not "@" or "#" or '&' or '-' or '_' or "+" and not "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in password and len(password) < 8:
            toast("Please read the conditions for a secure password.")
        else:
            return password
        if len(password) < 8:
            toast("Please enter a valid password.")
        else:
            return password
        if len(address) < 10:
            toast("Please enter a valid address.")
        else:
            return address
        if int(age) < 15:
            toast("You need to be aged of at least 15 years old to use Reviewin.")
        else:
            return int(age)
        if len(address) < 10 and int(age) < 15 and len(password) < 8 and len(full_name) < 5 and not  "@" or "#" or '&' or '-' or '_' or "+" and not "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in password:
            toast("Please register correctly ! ")
        else:
            return something



    def win_points(self):
        screen_1 = self.root.get_screen('user2')
        points = screen_1.ids.points.text
        points+=5
        return points



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


class Register(Screen):
    def build(self):
        self.title = "Register part"
        global re
        re  = Screen()
        re  = Builder.load_file("register.kv")
        return re



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

if __name__=="__main__":
    ReviewinApp().run()






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
from kivy.uix.image import Image, AsyncImage
import requests
from kivy.properties import ObjectProperty, ListProperty, StringProperty 
import regex as re 
import json
import random2
import random as _random
import couchdb
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from captcha.image import ImageCaptcha
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.fitimage import FitImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.app import App
pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

#fonts
LabelBase.register(name="OpenSans",fn_regular="OpenSans-Bold.ttf")
LabelBase.register(name="RSlab", fn_regular="Rslab.ttf")
LabelBase.register(name= "Popp",fn_regular="FontsFree-Net-Poppins-Bold.ttf")
LabelBase.register(name= "Inter", fn_regular= "FontsFree-Net-Inter-Regular.ttf")
LabelBase.register(name= "wave", fn_regular= "Wavetosh.ttf")
LabelBase.register(name="Robold,", fn_regular="Robold.ttf")



Window.size = (360,800)
 
Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str('teeeeeeeeeeee')} for x in range(10)]
        self.data_ = [{'font_name':"Popp"}]

class RVE(RecycleBoxLayout):
    def __init__(self, **kwargs):
        super(RVE, self).__init__(**kwargs)
        self.data = [{
            'name.source':str(1) + '.png'
        } for x in range(10) ]
        

#principale classe de l'application
class ReviewinApp(MDApp):
    new_dialog = None
    notdialog = None
    dialog =None
    dialoge = None
    asyncimage = None
    data = ListProperty([{'source':str(i) + str('.png')} for i in range(10)])
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
        sm.add_widget(Builder.load_file("contact_true.kv"))
        sm.add_widget(Builder.load_file('myinfo.kv'))
        sm.add_widget(Builder.load_file('test.kv'))
        return sm
    

    def return_async(self):
        if not self.asyncimage:
            self.asyncimage = AsyncImage(
                source="http://127.0.0.1:2223/captcha",
                size_hint_y= None
            )
        self.asyncimage.open()




    def test_token(self):
        print(self.token)


    def dialog__(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="You were successfully registered by our services. We thank you for your confidence, Reviewin Team.",
                font_name="Popp",
                theme_text_color= 'Custom',
                buttons = [
                    MDFlatButton(
                        text="Log in.",
                        theme_text_color='Custom',
                        text_color= [1,1,1,1],
                    )
                ]
            )
        self.dialog.open()
    
    def test_entering(self):
        res = requests.get('http://127.0.0.1:2223/ver')
        print(res)
    
    def login__(self):
        e_mail = self.root.current_screen.ids.e_mail_1.text
        password = self.root.current_screen.ids.password_1.text
        ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        a = _random.choice(ac)
        b = _random.choice(ac)
        c = _random.choice(ac)
        d = _random.choice(ac)
        f = _random.choice(ac)
        g = _random.choice(ac)
        h = _random.choice(ac)
        i = _random.choice(ac)
        j = _random.choice(ac)
        k = _random.choice(ac)
        l = _random.choice(ac)
        m = _random.choice(ac)
        n = _random.choice(ac)
        o = _random.choice(ac)
        p = _random.choice(ac)
        q = _random.choice(ac)
        r = _random.choice(ac)
        s = _random.choice(ac)
        t = _random.choice(ac)
        u = _random.choice(ac)
        v = _random.choice(ac)
        w = _random.choice(ac)
        x = _random.choice(ac)
        y = _random.choice(ac)
        z = _random.choice(ac)
        token = a + b + c + d + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z
        json_datas = {"e_mail":e_mail, "password":password}
        json_to_load = {"e_mail":e_mail}
        url_load = 'http://127.0.0.1:2223/load'
        url = 'http://127.0.0.1:2223/loginn'
        url_session = 'http://127.0.0.1:2223/sessions'
        res = requests.post(url, json=json_datas)
        json_session = {"e_mail":e_mail, "password":password, "token":token}

        if res.json() == {"User":"exists"}:
            print("User exists")
            response = requests.post(url_session, json=json_session)
            sm.current = "user-interface"
        else:
            toast('Invalid password or e-mail.')
    
    def tttt(self):
        res = requests.get('http://127.0.0.1:2223/get')
    
    def load_e_mail(self):
        text = self.root.get_screen('login').ids.e_mail_1.text

    def load_password(self):
        text = self.root.get_screen('login').ids.password_1.text
    
    def load_gender_js(self):
        self.text = "aaa"
    

    def test_6(self):
        print('tttt')

    def test_enter(self):
        self.test_6()
    
    def current(self):
        sm.current = "login"

    def dialog_(self):
        if not self.notdialog:
            self.dialog = MDDialog(
                text="You were successfully registered ! We, The Reviewin Team, are pleased to welcome you as a Reviewin User. Enjoy !",
                font_name="Popp",
                font_size="17sp",
                theme_text_color='Custom',
                buttons=[
                    MDFlatButton(
                        text="Log In",
                        text_color= [0,0,0,0],
                        on_press= self.current()
                    )
                ]
            )
        self.dialog.open()


    def recaptcha__(self):
        age = self.root.get_screen('register').ids.age.text
        e_mail = self.root.get_screen('register').ids.e_mail.text
        country = self.root.get_screen('register').ids.country.text
        password = self.root.get_screen('register').ids.password.text
        gender = self.root.get_screen('register').ids.gender.text
        recaptcha_value = self.root.current_screen.ids.recaptcha.text
        points = 0

        url = 'http://127.0.0.1:2223/verify_captcha'
        url_register = 'http://127.0.0.1:2223/reviewin_users'
        payload = {"captcha_value":recaptcha_value}
        print(payload)
        user_data = {"gender":gender, "age":age, "country":country,"e_mail":e_mail, "password":password, "points":points} 
        res =  requests.post(url, json=payload)
        resp = requests.post(url_register, json=user_data)
        e_mail_1 = {"e_mail":e_mail}

        if res.json() == {"Captcha":"good"} and resp.json() == {"User":"registered"}:
            toast('Registered successfully', duration= 2.5)
            sm.current = "login"
            print('User registered')
        elif res.json() != {"Captcha":"good"} and resp.text == {"User":"registered"}:
            toast("Invalid captcha value.")
        else:
            toast("E-mail already used.", duration=3)


    def build_build(self):
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_once(self.accueil, 3)
        
    def accueil(*args):
        sm.current = "accueil"

    def color_characters_compteur(self):
        self.theme_cls.primary_palette = "Cyan"


    def test_input(self):
        if not self.dialog:
            self.dialog = MDInputDialog(
                title= "Recaptcha",
            )
        self.dialog.open()


    def test_2(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Recaptcha",
                text="Just copy the text you're seeing",
                images=[
                    Image(
                        source= 'captcha.png',
                        center_x = self.parent.center_x,
                        center_y = self.parent.center_y,
                        size_hint= (0.4, 0.3) 
                        ),
                    ],
                )
        self.dialog.open()


    def account(self):
        password = self.root.current_screen.ids.password_1.text
        e_mail = self.root.current_screen.ids.e_mail_1.text
        token = self.token
        url = 'http://admin:kolea21342@127.0.0.1:5984/reviewin_users/_design/design_users/_view/login?key=' + '"' + e_mail + '"'
        res = requests.get(url)
        doc = res.json()
        if e_mail in res.text and password in res.text:
            data = {"e_mail":e_mail, "password":password, "token": token, "gender":doc['rows'][1]['value']['gender'],'age':doc['rows'][1]['value']['age'], 'country':doc['rows'][1]['value']['country']}
            response = requests.post('http://admin:kolea21342@127.0.0.1:5984/sessions', json=data)
            sm.current = "user-interface"
        else:
            toast('Invalid password or e-mail.')
    
        
    def show_alert_dialog(self):      
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Exit ?",
                text="Really want to exit ?",
                images=[
                    Image(
                        source= 'captcha.png',
                        size_hint= (0.4, 0.3) 
                        ),
                    ],
                buttons=[
                    MDFlatButton(
                        text="[u]Sure ! I'll come back ![/u]",
                        theme_text_color="Custom",
                        text_color=[1,1,1,1],
                        on_press= self.go_back
                    ),
                    MDFlatButton(
                        text="No finally, I prefer to stay.",
                        theme_text_color="Custom",
                        text_color= [1,1,1,1],
                        on_press=  self.stay_app
                    ),
                ],
            )
        self.dialog.open()

    def test_ayoub(self):
        if self.root.current_screen.ids.full_name.text == 'ayoub':
            test_2()
        else:
            print("nnnnn")
    
    def do_something(self):
        full_name = self.root.current_screen.ids.full_name.text
        print(full_name)
    
    def test_rec(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Recaptcha",
                text="Just copy the text you're seeing",
                type="custom",
                height= "400dp",
                content_cls=Content()
            )
        self.dialog.open()
    
    def press(self):
        print('pressed')


    def logoutnew(self):
        token = self.token
        log_out_data = {"token":token}
        url = 'http://127.0.0.1:2223/logout'
        res = requests.post(url, json=log_out_data)
        print(res.text)
        if res.text == {"Status":"Done"}:
            sm.current = "login"
            toast('Successfully logged out.')
        else:
            toast('Failed to log out. Please verify your wifi connection or try again.')

        
    def log_out(self):
        if not self.new_dialog:
            self.new_dialog = MDDialog(
                title= "Log out",
                text= "Are you sure to log out ?",
                font_size= "18",
                font_name= "Robold",
                type= "custom",
                buttons = [
                    MDFlatButton(
                        text= "[u]Yes[/u]",
                        text_color= [1,1,1,1],
                        font_size= "17sp",
                        font_name= "Popp",
                        theme_text_color= "Custom",
                        on_release= self.logoutnew(),
                    ),
                    MDFlatButton(
                        text= "[u]No.[/u]",
                        text_color= [1,1,1,1],
                        font_size= "17sp",
                        font_name="Popp",
                        theme_text_color= "Custom",
                        on_relase= self.newdialog.dismiss(),
                    )
                ]
            )



    

    def recaptcha_de_wish(self):
        url = 'http://127.0.0.1:2223/captcha'
        if not self.dialog:
            self.dialog = MDDialog(
                title= "Recaptcha",
                text="Just copy the text you're seeing",
                type="custom",
                height= "400dp",
                buttons=[
                    MDFlatButton(
                        text="Submit",
                        theme_text_color="Custom",
                        text_color= [0,0,0,0],
                    )
                ],
                content_cls= AsyncImage(
                    source= 'http://127.0.0.1:2223/captcha',
                    size_hint_y= None,
                    ),
                )
        self.dialog.open()
    def verify(self):
        full_name = self.root.get_screen('register').ids.full_name.text
        print(full_name)

    def test_dialog(self):
        if not self.dialoge:
            self.dialoge = MDDialog(
                title= "Recaptcha",
                text="Just copy the text you're seeing",
                type="custom",
                height= "400dp",
                content_cls= AsyncImage(
                    source= 'http://127.0.0.1:8080/captchaa',
                    size_hint_y= None,
                )
            )
        self.dialoge.open()
    
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
    def on_enter_show_recaptcha(self):
        if not self.asyncimage:
            self.asyncimage = AsyncImage(
                source= 'http://127.0.0.1:2223/captcha',
                size_hint_y= None
            )
        self.asyncimage.texture_update()
    
    def go_to_screen_rec(self,*args):
        sm.current == "recaptcha"

    def verify_datas(self, *args):
        age = self.root.current_screen.ids.age.text
        country = self.root.current_screen.ids.country.text
        e_mail = self.root.current_screen.ids.e_mail.text
        password = self.root.current_screen.ids.password.text
        gender = self.root.current_screen.ids.gender.text
        pattern_verify = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        list_verify = [0,1,2,3]
        list_test = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]

        if int(str(age)) > 16 and len(country) not in list_verify and re.search(pattern_verify, e_mail) and len(password) > 8 and gender == "M"or gender == "F":
            sm.current = "recaptcha"
        else:
            toast("Please check your informations while signing up.")

        if len(age) == 0 or len(country) < 3 or len(e_mail) == 0 or len(password) == 0 or len(gender) == 0:
            toast("There is an empty field. Please check our conditions to register to the application.")

        
#fonctions_de_secours
    def test_3(self):
        list_test = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
        full_name = self.root.current_screen.ids.full_name.text
        age = self.root.current_screen.ids.full_name.text
        country = self.root.current_screen.ids.country.text
        e_mail = self.root.current_screen.ids.e_mail.text
        password = self.root.current_screen.ids.e_mail.text
        gender = self.root.current_screen.ids.gender.text
        pattern_verify = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        list_verify = [1,2,3]

        if int(age) < int(16):
            print("too low")
        elif not re.search(pattern, e_mail):
            print("bad e_mail")
        elif len(password) < 8:
            print("bad password")
    




#fonction recaptcha de secours
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



    def check_auth_user(self):
        full_name_text = self.root.current_screen.ids.full_name.text
        age = int(self.root.current_screen.ids.age.text)
        e_mail = self.root.current_screen.ids.e_mail.text
        gender = str(self.root.current_screen.ids.gender.text)
        country = self.root.current_screen.ids.country.text 
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
        if len(self.root.current_screen.ids.full_name.text) > 3 and self.root.current_screen.ids.age.text > 16 and self.root.current_screen.ids.gender.text == 'M' or 'F' and re.search(pattern, e_mail) and len(country) > 4:
            recaptcha_de_wish()
        else:
            toast("Please sign up correctly. We advice you to see the register model.")



    def go_back_1(self):
        sm.current = "register"
    
    def test(self):
        if self.root.current_screen.ids.full_name.text == 'something':
            print(json.dumps(self.root.current_screen.ids.full_name.text))
        else:
            print("no")


    def recaptcha(self):
        ac  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','10','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        a = random.choice(ac)
        b = random.choice(ac)
        c = random.choice(ac)
        d = random.choice(ac)
        f = random.choice(ac)
        g = random.choice(ac)
        h = random.choice(ac)
        random_string = a + b + c + d + f + g + h
        if not self.dialog:
            self.dialog = MDDialog(
                title= 'Recaptcha',
                text_color= [1,1,1,1],
                text= str(root.random_string),
                font_name= "wave",
                font_size= 18,
                type= 'confirmation',
                buttons=[
                    MDFlatButton(
                        text= 'Submit',
                        theme_text_color= 'Custom',
                        text_color= [1,1,1,1],
                        font_name= 'Popp',
                        on_release= self.verify_captcha(),                        
                    ),
                    MDFlatButton(
                        text= 'Cancel',
                        theme_text_color= 'Custom',
                        text_color= [1,1,1,1],
                        on_release= self.dismiss()
                    )
                ]
        ),
        self.dialog.open()


    def recaptcha_test_successfull(self):
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
        url = 'http://127.0.0.1:2223/user'
        data = {'full_name':json.dumps(full_name), 'age':json.dumps(age), 'country':json.dumps(country), 'e_mail':json.dumps(e_mail), 'gender':json.dumps(gender), 'password':json.dumps(password)}
        response = requests.post(url, json=data)

    def login(self):
        full_name_1 = str(self.root.current_screen.ids.full_name_1.text)
        e_mail_1 = str(self.root.current_screen.ids.e_mail_1.text)
        password_1 = str(self.root.current_screen.ids.password_1.text)
        url = 'http://127.0.0.1:8080/'
        res = requests.post()
    
    def load_personal_informations(self):
        token = self.token
        url = 'http://127.0.0.1:2223/load'
        json = {"token":token}
        res = requests.post(url, json=json)
        doc = res.json()
        print(doc)
        e_mail = doc['rows'][0]['value']['e_mail']
        password = doc['rows'][0]['value']['password']
        age = doc['rows'][0]['value']['age']
        location = doc['rows'][0]['value']['country']
        gender = doc['rows'][0]['value']['gender']
        self.root.current_screen.ids.age_1.text = age
        self.root.current_screen.ids.gender_1.text = gender
        self.root.current_screen.ids.country_1.text = location
        self.root.current_screen.ids.user_e_mail.text = e_mail
        self.root.current_screen.ids.password2.text = password

                

        
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






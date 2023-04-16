
from flet import *
import uuid
from flet import AppBar

#Sign Up
email = Ref[TextField]()
password = Ref[TextField]()
location = Ref[TextField]()
interests = Ref[TextField]()
age = Ref[TextField]()
gender = Ref[TextField]()
#captcha
captcha_value = Ref[TextField]()
points = 0
#signinw
signin_ref_email = Ref[TextField]()
signin_ref_password = Ref[TextField]()
image_ref = Ref[Image]()
#token
token = str(uuid.uuid4())
#Modify informations ref's
modify_email = Ref[TextField]()
modify_password = Ref[TextField]()
modify_age = Ref[TextField]()
modify_country = Ref[TextField]()
modify_gender = Ref[TextField]() #------>   #mouais on verra si on le laisse
#NavigationRailId
nav = Ref[NavigationRail]()
view_ref = Ref[View]()
def generate_token():
    global token
    token = str(uuid.uuid4())
    return token
class PersonalInformations(UserControl):
    def __init__(self):
        super().__init__()
    def append_view_modify(self):
        self.controls.append(
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextField(ref=modify_email,color=colors.WHITE,cursor_color=colors.WHITE, cursor_radius=20, hint_text="New E-mail", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE)),
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextField(ref=modify_password, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="New Password",border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False, color=colors.WHITE))]),
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextField(ref=modify_country, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="New Country", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False, color=colors.WHITE))]),
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextField(ref=modify_age, color=colors.WHITE,cursor_color=colors.WHITE, cursor_radius=20, hint_text="New age", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False, color=colors.WHITE))]),
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextButton('Apply')]),
            Row(vertical_alignment=CrossAxisAlignment.START, expand=True, alignment=MainAxisAlignment.CENTER, controls=[TextButton('Cancel')]),
            ]))
    def build(self):
        import requests
        import json
        response = requests.post('http://127.0.0.1:2223/load', json={"token":token})
        document = response.json()
        print(document)
        return View(
            "/@me/personal",
            bgcolor="#292222",
            controls=[
                Column(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[Text(f"Your e-mail is{document['email']}")]),
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[Text(f"Your password is{document['password']}")]),
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[Text(f"Your country is{document['country']}")]),
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[Text(f"You are {document['age']}")]),
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[Text(f"Your gender mentionned while you were registering :{document['gender']}")]),
                        Row(vertical_alignment=CrossAxisAlignment.START, expand=True, controls=[TextButton('Modify, (it will deconnect you from your session.)', on_click=self.append_view_modify())])
                    ]
                )
            ]
        )
class UserMainView(UserControl):
    def __init__(self):
        super().__init__()
        import requests
        import json
        self.mycontainer = Container(alignment=alignment.top_left, width=100, bgcolor="#292222", height=100, content=Text('Reviewin', weight='bold', color=colors.WHITE, size=16)),
        self.images = Column(expand=True, scroll="always",wrap=False, alignment=MainAxisAlignment.CENTER)
        self.response = requests.get('http://127.0.0.1:2223/products')
    def append_images(self):
        import requests
        import json
        for i in range(len(self.response.json())):
            self.images.controls.append(
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[Image(
                        ref=image_ref,
                        src=f"http://127.0.0.1:2223/products/{self.response.json()[i]}",
                        width=400,
                        height=400,
                        fit= ImageFit.SCALE_DOWN,
                        repeat= ImageRepeat.NO_REPEAT,
                        border_radius= border_radius.all(10)
                    ), TextButton('Yes', on_click= lambda e: e.page.go("/@me/personal"))]
                ))
    def build(self):
        import requests
        import json
        print(token)
        data = {"token":token}
        url = 'http://127.0.0.1:2223/products/list'
        images = Column(expand=True, scroll="always",wrap=False, alignment=MainAxisAlignment.CENTER)
        response = requests.get('http://127.0.0.1:2223/products')
        list_of_images = response.json()
        self.append_images()
        return View(
            "/@me",
            bgcolor="#292222",
            controls=[
                Row(alignment=MainAxisAlignment.END,controls=[Container(height=100,width=100, bgcolor="#292222", alignment=alignment.top_right, content=Dropdown(height=50,width=50, options=[dropdown.Option('My account'), dropdown.Option('F.A.Q'), dropdown.Option('Privacy Policy'), dropdown.Option('Log Out.')]))]),
                Container(width=100, bgcolor="#292222",height=100, content=Text('Reviewin', color=colors.WHITE, weight='bold', size=22), alignment=alignment.top_left),
                Column(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.images,
                    ]
                ),
            ]
        )
class Faq(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        faq_items = [
            Card(
                content=Container(width=600, height=400,content=Column(horizontal_alignment=CrossAxisAlignment.CENTER,expand=True, alignment=MainAxisAlignment.START, controls=[Text("Who are we ?", size=25, color=colors.WHITE, weight='bold')]), bgcolor="#292222"),
                elevation=5,
                margin=5,
            ),
            Card(
                content=Container(width=600, height=400,content=Text("About how we manage yout private datas."), bgcolor="#292222"),
                elevation=5,
                margin=10,),
            Card(
                content=Container(width=600, height=400,content=Text("Annexes"), bgcolor="#292222"),
                elevation=10,
                margin=10,
            )
        ]

        return View(
            "/faq",
            bgcolor="#292222",
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                AppBar(
                    leading=IconButton(
                        icon=icons.ARROW_BACK,
                        icon_color=colors.WHITE,
                        on_click=lambda e: e.page.go('/signup')
                    ),
                    leading_width=40,
                    center_title=True,
                    title=Text("F.A.Q", color=colors.WHITE),
                    bgcolor="#292222",
                ),
                Column(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    scroll="always",
                    wrap=False,
                    controls=[faq_items[0], faq_items[1], faq_items[2]]
                )
            ]
        )

class SignUp(UserControl):
    def __init__(self):
        super().__init__()
        self.age =TextField(ref=age, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Age", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.email = TextField(ref=email, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="E-mail", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.password = TextField(ref=password,password=True,can_reveal_password=True, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Password", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.location = TextField(ref=location, color=colors.WHITE,cursor_color=colors.WHITE, cursor_radius=20, hint_text="Location (country, not address)", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.interests = TextField(ref=interests, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Interests", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.gender = TextField(ref=gender, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Gender. M or F", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
    def verify_datas(self, e):
        import regex as re
        correct_genders = ['M', 'F']
        pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        if gender.current.value in correct_genders and re.search(pattern, email.current.value) and len(str(location.current.value)) != 0 and int(age.current.value) >= 16 and len(interests.current.value) != 0 and len(password.current.value) >= 8:
            e.page.go('/recaptcha2')
        else:
            print('no good info')
    def printsomething(self,e):
        e.page.go("/signin")

    def already_have_account(self,e):
        e.page.go('/signin')
    def show(self, e):
        pass

    def build(self):
        return View("/signup",
        bgcolor="#292222",
        controls=[
            AppBar(
                    leading_width=40,
                    title=Text(""),
                    center_title=False,
                    bgcolor="#292222",
                    actions=[
                        PopupMenuButton(items=[PopupMenuItem(text="F.A.Q", on_click=lambda e: e.page.go('/faq')),PopupMenuItem(text="Send us a message."),]),]),
            Column(
            alignment=MainAxisAlignment.CENTER,
            expand=True,
            controls=[
                Row(alignment=MainAxisAlignment.CENTER, controls=[Text("Join Reviewin Today.", color=colors.WHITE, size=17, weight='bold')]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.email]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.password]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.location]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.interests]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.age]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[self.gender]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[TextButton("Next Step", on_click=self.verify_datas)]),
                Row(alignment=MainAxisAlignment.CENTER, controls=[Text("Already Have an account ?", color=colors.WHITE, size=18, weight='bold'), TextButton('Sign in.', on_click=self.printsomething)]),
            ],)
        ])

class SignIn(UserControl):
    def __init__(self):
        super().__init__()
        self.email_ = TextField(ref=signin_ref_email, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="E-mail", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.password_ = TextField(ref=signin_ref_password,password=True,can_reveal_password=True, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Password", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
    def login(self,e):
        e_mail = signin_ref_email.current.value
        password = signin_ref_password.current.value
        import requests
        import json
        json_ = {"e_mail":e_mail, "password":password}
        url = 'http://127.0.0.1:2223/loginn'
        response = requests.post(url, json=json_)
        json_sessions = {"e_mail":e_mail, "password":password, "token":token}
        print(response.json())
        if response.json() == {"User":"exists"}:
            res = requests.post('http://127.0.0.1:2223/sessions', json=json_sessions)
            print(res.status_code)
            print("datas sent !")
            e.page.go('/@me')
        else:
            print(response.json(), response.text)
            print('Re-try or check your network connection.')
        
    def build(self):
        return View(
            "/signin",
            bgcolor="#292222",
            controls=[
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        Row(alignment=MainAxisAlignment.CENTER,controls=[Text("Sign in.", color=colors.WHITE), TextButton("Sign Up.", on_click=lambda e: e.page.go("/signup"))]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[self.email_]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[self.password_]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[TextButton('Log In.', on_click=self.login)])
                    ]
                )
            ]
        )
class Captcha_View(UserControl):
    def __init__(self):
        super().__init__()
        self.captcha_textfield = TextField(ref=captcha_value, color=colors.WHITE, border_color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20)
    def submit(self,e):
        import requests
        import json
        json_to_send = {"gender":gender.current.value, "age":age.current.value, "country":location.current.value, "email":email.current.value, "password": password.current.value, "points":points, "captcha_value":captcha_value.current.value}
        response = requests.post('http://127.0.0.1:2223/accounts', json=json_to_send)
        if response.text == {"Captcha":"good let sign up"}:
            e.page.go('/signin')
        else:
            print('Please try again.')
    def build(self):
        return View(
            '/recaptcha2',
            bgcolor="#292222",
            controls=[
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        Row(alignment=MainAxisAlignment.CENTER,controls=[Image(
                            src=f"http://127.0.0.1:2223/captcha",
                            height=400,
                            width=400,)]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[self.captcha_textfield]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[TextButton('Submit', on_click=self.submit)])
                    ]
                )
            ]
        )

def main(page: Page):
    page.title = "Reviewin"
    page.bgcolor = "#292225"
    def route_change(route):
        page.views.clear()
        if page.route == "/signin":
            page.views.append(SignIn().build())
        if page.route == "/signup":
            page.views.append(SignUp().build())
        if page.route == "/recaptcha2":
            page.views.append(Captcha_View().build())
        if page.route == "/@me":
            page.views.append(UserMainView().build())
        if page.route == "/@me/personal":
            page.views.append(PersonalInformations().build())
        if page.route == "/faq":
            page.views.append(Faq().build())
        page.update()
    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    #page.views.append(SignIn("E-mail", 'Yep').build())
    page.views.append(SignUp().build())
    page.update()

flet.app(target=main, port=4000, view=WEB_BROWSER)
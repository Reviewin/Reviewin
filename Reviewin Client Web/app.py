import flet
from flet import Column
from flet import MainAxisAlignment
from flet import Page
from flet import Row
from flet import TextField
from flet import Ref
from flet import TextButton
from flet import colors
from flet import ButtonStyle
from flet import Text
from flet import *
from flet import TextStyle
from flet import Image
from flet import WEB_BROWSER
class Register(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        pass


def main(page: Page):
    page.bgcolor = "#292222"
    page.title = "Reviewin"
    e_mail = Ref[TextField]()
    password = Ref[TextField]()
    def login(e):
        import json
        import regex as re
        import requests
        import uuid
        regex = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        json_to_send = {"e_mail":str(e_mail.current.value), "password":password.current.value}
        token = str(uuid.uuid4())
        json_sessions = {"e_mail":e_mail.current.value, "password":password.current.value, "token":token}
        if re.search(regex, e_mail.current.value):
            response = requests.post('http://127.0.0.1:2223/loginn', json=json_to_send)
            print(response.json())
            if response.json() == {"User":"exists"}:
                res = requests.post('http://127.0.0.1:2223/sessions', json=json_sessions)
                if res.json() == {"Session":"created"}:
                    print('Done')
                else:
                    print('not done')
            else:
                print('Bad password or e-mail')
        else:
            print('Please verify email entered.')
    page.add(
        Column(
            expand=True,
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text('Connection', color=colors.WHITE, weight='bold', size=22)
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        TextField(ref=e_mail,color=colors.WHITE, value="",border_color=colors.WHITE, cursor_color= colors.WHITE, hint_text="example@domain.com", hint_style=TextStyle(weight='bold', color=colors.WHITE, italic=True)),
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        TextField(ref= password,value="",color=colors.WHITE, border_color=colors.WHITE, password=True, can_reveal_password=True, cursor_color=colors.WHITE, cursor_radius=20, focused_border_color=colors.WHITE, hint_text="Password",  hint_style=TextStyle(size=15, weight='bold', italic=True, color=colors.WHITE)),
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls= [
                        TextButton("Log In.", style=ButtonStyle(color=colors.BLUE) ,on_click=login)
                    ]
                )
            ],
        ),
    )
    page.update()

flet.app(target=main, port=2000, view=WEB_BROWSER)

import flet as ft
import json 
from flet import *


class UserInput(UserControl):
    def __init__(self):
        super().__init__()
    def build(self):
        return ft.Container(
            width= 320,
            height= 40,
            border= border.only(border.BorderSide(0.5, "white54"))
        )
def main(page: ft.Page):
    page.title = "Reviewin"
    page.bgcolor = "#292222"
    page.horizontal_alignment = 'center'
    e_mail = ft.Ref[ft.TextField](),
    password = ft.Ref[ft.TextField]()
    my_card = ft.Card(
        width= 408,
        elevation= 15,
        height= 600,
        margin= 2,
        content= ft.Container(
            bgcolor='#23262a',
            border_radius= 6,
            content= ft.Column(
                horizontal_alignment =ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Divider(height=40,color='transparent'),
                    ft.Column(
                        alignment= ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls= [
                            ft.Text(
                                "Sign In.",
                                size= 22, 
                                weight= 'bold',
                                color= ft.colors.WHITE
                            )
                        ]
                    )
                ]
            ),
        )
    )
    page.add(my_card)
   
ft.app(target=main, port=8000, view= ft.WEB_BROWSER)
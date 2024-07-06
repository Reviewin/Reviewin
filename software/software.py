#Littéralement un copier collé de la version web
import flet 
from flet import *
signin_ref_email = Ref[TextField]()
signin_ref_password = Ref[TextField]()
import passlib
from passlib.hash import pbkdf2_sha256 as sh
class SignIn(UserControl):
    def __init__(self):
        super().__init__()
        self.email_ = TextField(ref=signin_ref_email, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="E-mail", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.password_ = TextField(ref=signin_ref_password,password=True,can_reveal_password=True, color=colors.WHITE, cursor_color=colors.WHITE, cursor_radius=20, hint_text="Password", border_color=colors.WHITE, hint_style=TextStyle(size=15, weight='bold', italic=False,color=colors.WHITE))
        self.hash = sh.hash(self.password.value)
    def login(self,e):
        data = {"email": str(signin_ref_email.value), "password": str(signin_ref_password.value)}
        import requests
        import json
    def go_page(self,e):
        e.page.go("/admin")
    def build(self):
        return View(
            "/signin",
            bgcolor="#292222",
            controls=[
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        Container(content=Row(alignment=MainAxisAlignment.CENTER, controls=[Text('Reviewin Admin', size=40, color=colors.WHITE, weight=FontWeight.BOLD, italic=False, )], expand=True),margin=40, height=100),
                        Row(alignment=MainAxisAlignment.CENTER,controls=[Text("Sign in.", color=colors.WHITE)]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[self.email_]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[self.password_]),
                        Row(alignment=MainAxisAlignment.CENTER, controls=[TextButton('Log In.',on_click=self.go_page)
                    ]
                )
            ]
        )])
class ReviewinSponsor(UserControl):
    def build(self):
        self.page.drawer = NavigationDrawer(
            controls=[
                ElevatedButton("My Account")
            ]
        )
        def show_drawer(self,e):
            self.page.drawer.open = True
            self.page.drawer.update()

        return View(
            f"/admin",
            bgcolor="#292222",
            controls=[
                IconButton(icon=icons.VIEW_SIDEBAR, on_click=self.show_drawer)
            ]
        )

def main(page):
    page.title = "Reviewin Admin"
    page.bgcolor = "#292225"
    def route_change(route):
        page.views.clear()
        if page.route == "/admin":
            page.views.append(ReviewinSponsor().build())
        page.update()
    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    #page.views.append(SignIn("E-mail", 'Yep').build())
    page.views.append(SignIn().build())
    page.update()
flet.app(target=main)
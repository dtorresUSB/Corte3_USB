from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from models.main import User


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui",self)
        self.show()
        self.initGui()


    def initGui(self):
        self.login_btn.clicked.connect(self.login)
        self.register_btn.clicked.connect(self.register)


    def login(self):
        email = self.email.toPlainText()
        password = self.password.toPlainText()

        user = User.login(email, password)
        print(user)


    def register(self):
        self.close()


class RegisterView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/register.ui",self)
        self.show()
        self.initGui()


    def initGui(self):
        self.register_btn.clicked.connect(self.register)
        self.login_btn.clicked.connect(self.login)


    def register(self):
        name = self.name.toPlainText()
        email = self.email.toPlainText()
        password = self.password.toPlainText()

        User(name, email, password)

        self.login()


    def login(self):
        self.login_view = LoginView()
        self.login_view.show()

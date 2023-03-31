
import pyrebase
import kivy
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.app import App
import requests
import json

Window.size = (310, 580)
 
kv = ''' 
   
  <ForgotDialog> 
      orientation: "vertical" 
       spacing: "12dp" 
      size_hint_y: None 
      height: "120dp" 
      MDTextField: 
           hint_text: "Enter your Email" 

   '''
   
config = {
       "apiKey": "AIzaSyB8f5Py7E60rlCtpAaqXzpmWSgHN9vxfrc",
       "authDomain": "fir-python-demo-39212.firebaseapp.com",
       "databaseURL": "https://fir-python-demo-39212-default-rtdb.firebaseio.com",
       "storageBucket": "fir-python-demo-39212.appspot.com",
   }
class MyApp(App):
    error_message = StringProperty('')

    try:
    # code that might raise an error
    except Exception as ex:
        self.error_message = str(ex)

  
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
   
class MyFirebaseSignup:
        def sign_up(self, username, email, password, login_message:None):
            try: 
               user = auth.create_user_with_email_and_password(email, password)
               data = {"email": email, "password": password, "idToken": True}
               info = auth.get_account_info(user["idToken"])
               auth.send_email_verification(user["idToken"])
               password = data.get("password")
               print("Successfully created account")
               app = App.get_running_app()
               app.root.current = 'login'
            
            except: 
                print("Invalid")
            

               #app..... id: login_message  ---- display error message on signin page
              
   
           #app.my_firebasesignup.sign_up(login_username.text, login_email.text, login_password.text)
   
class MyFirebaseLogin():
       def login(self, email, password):
           try:
               login = auth.sign_in_with_email_and_password(email, password)
               info = auth.get_account_info(login["idToken"])
               print("Successfully Logged in")
               app = App.get_running_app()
               app.root.current = 'profile'
           except:   
               print("Invalid")

user = auth.refresh(user.uid["refreshToken"])
           #print("Login!!")
   
class MainScreen(Screen):
        pass
   
class LoginScreen(Screen):
        pass
   
class SignupScreen(Screen):
        pass
   
class AccountsScreen(Screen):
        pass
      
class ProfileScreen(Screen):
        pass   
class ForgotDialog(BoxLayout):
        pass
   
class LoginSignup(MDApp):
     dialog = None
 
     def build(self):
            screen_manager = ScreenManager()
            screen_manager.add_widget(Builder.load_file("main.kv"))
            screen_manager.add_widget(Builder.load_file("signup.kv"))
            screen_manager.add_widget(Builder.load_file("login.kv"))
            screen_manager.add_widget(Builder.load_file("accounts.kv"))
            screen_manager.add_widget(Builder.load_file("profile.kv"))
            self.my_firebasesignup = MyFirebaseSignup()
            self.my_firebaselogin = MyFirebaseLogin()
            return screen_manager
  
     def PasswordResetDialog(self):
          if not self.dialog:
              self.dialog = MDDialog(
                  title="Forgot Password",
                  type="custom",
                  content_cls=ForgotDialog(),
                  buttons=[
                      MDFlatButton(
                          text="SUBMIT",
                          on_release=self.neat_dialog,
                      ),
                  ],
              )
  
     def neat_dialog(self, obj):
                  self.dialog.dismiss()
                  email = self.dialog.ids.email.text
                  forgot = auth.send_password_reset_email(email)
  
                  self.dialog.open()
  
  
  
  
if __name__ == "__main__":
      LabelBase.register(name="MPoppins", fn_regular="/Users/crystal/PycharmProjects/loginsingup/Poppins/Poppins-Medium.ttf")
      LabelBase.register(name="BPoppins", fn_regular="/Users/crystal/PycharmProjects/loginsingup/Poppins/Poppins-SemiBold.ttf")
  
      LoginSignup().run()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class MyFirebase():
    def __init__(self):
        
        cred = firebase_admin.Certificate("path/to/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    
    def sign_up(self, username,email,password):
        user = self.auth.create_user(email=email, password=password)
        self.auth.update_user(user.uid, display_name=username)
        print(f'User {username} has been created with email {email}')
        
    def login(self, email, password):
        try:
            # verify the user's email and password
            user = auth.get_user_by_email_and_password(email, password)
            return True, user.uid
        except Exception as e:
            return False, str(e)

    def send_password_reset_email(self, email):
        try:
            # send the password reset email
            auth.send_password_reset_email(email)
            return True
        except Exception as e:
            return False, str(e)


    
import json
import pyrebase


class FireBase:

    config = json.load(open("firebase.json"))

    def __init__(self):
        self.firebase = pyrebase.initialize_app(FireBase.config).database()

    def test(self):
        all_users = self.firebase.child("users").get()
        for user in all_users.each():
            print(user.key()) 
            print(user.val()) 

    def fetch_user_image_urls(self, username):
        all_users = self.firebase.child("users").get()
        for user in all_users.each():
            if(user.val()["username"] == username):
                return user.val()["images"]

    def save(self, data, username):
        all_users = self.firebase.child("users").get()
        for user in all_users.each():
            if(user.val()["username"] == username):
                self.firebase.child("users").child(user.key()).child("output").set(data)

import pyperclip
import threading
import pyrebase

#firebase configuration
config = {
    "apiKey": "AIzaSyD59NCDicwl1TDGFRWB-EZwYhukt0YLHlE",
    "authDomain": "copylater-dc926.firebaseapp.com",
    "databaseURL": "https://copylater-dc926.firebaseio.com",
    "projectId": "copylater-dc926",
    "storageBucket": "copylater-dc926.appspot.com",
    "messagingSenderId": "812089921591",
    "appId": "1:812089921591:web:4d720ba57b10aacf2d2fb2",
    "measurementId": "G-8760W021S9"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def get_data():
    return db.child('test').get()

def check_if_exists(link):
    links = get_data()
    if links.val():
        for l in links.each():
            if l.val()==link:
                return True
        return False

def store_data():
    threading.Timer(3.0,store_data).start()
    if not check_if_exists(pyperclip.paste()):
        db.child('test').push(pyperclip.paste())

store_data()




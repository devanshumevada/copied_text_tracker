import subprocess
import threading
import pyrebase

#firebase configuration
config = {
    #you can get your firebase configurations from the firebase console
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def get_data():
    return db.child('test').get()

def read_from_clipboard():
    return subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def check_if_exists(link):
    links = get_data()
    if links.val():
        for l in links.each():
            if l.val()==link:
                return True
        return False

def store_data():
    threading.Timer(3.0,store_data).start()
    if not check_if_exists(read_from_clipboard()):
        db.child('test').push(read_from_clipboard())

store_data()




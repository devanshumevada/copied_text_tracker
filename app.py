from flask import Flask, render_template, request, redirect, url_for
import pyrebase
import pyperclip

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
app = Flask(__name__)


def get_data():
    return db.child('test').get()


@app.route('/')
def index():
    links = get_data()
    return render_template('index.html', links=links)

@app.route('/copy_data', methods=['POST'])
def copy_data():
    data = request.form['linkval']
    if data:
        pyperclip.copy(data)
    return redirect(url_for('index'))

@app.route('/delete_data/<string:id>',methods=['GET'])
def delete_data(id):
    db.child('test').child(id).remove()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)






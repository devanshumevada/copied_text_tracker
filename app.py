from flask import Flask, render_template, request, redirect, url_for
import pyrebase
import subprocess

#firebase configuration
config = {
   #you can get your firebase configurations from your firebase console
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)


def get_data():
    return db.child('test').get()
   
   
def copy_to_clipboard(text):
     process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
     process.communicate(text.encode('utf-8'))
   


@app.route('/')
def index():
    links = get_data()
    return render_template('index.html', links=links)

@app.route('/copy_data', methods=['POST'])
def copy_data():
    data = request.form['linkval']
    if data:
        copy_to_clipboard(data)
    return redirect(url_for('index'))

@app.route('/delete_data/<string:id>',methods=['GET'])
def delete_data(id):
    db.child('test').child(id).remove()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)






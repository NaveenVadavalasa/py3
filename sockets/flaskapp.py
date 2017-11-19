from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/home')
def fun():
    #return  'this is my home page'
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

if __name__ == '__main__':
    app.run()
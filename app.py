from flask import Flask, jsonify, request, url_for, redirect, session, render_template
from random import randint

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'thisisasecret' # we need the secret key to use a session


# export FLASK_APP=whatever.py
# use this if your app name is not app.py

@app.route('/')
def index():
    #return '<h1>Hello </h1>'
    return render_template('home.html')

@app.route('/home', methods = ['GET', 'POST'], defaults ={ 'name' : "Guest"})
@app.route('/home/<name>', methods = ['GET', 'POST'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False, mylist=['one', 'two', 'three'],
    listofdict=[{"key": 22}, {"key":55}])
    # return '<h1{}>Hello {}</h1>'.format(name)

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    s = a+b
    return '<h1>{}</h1>'.format(s)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    return jsonify({ 'key1' : 'value1', 'key2' : [1,2,3], "name" : name})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return 'Hi {}. You are from {}'.format(name, location)

@app.route('/theform')
def theform():
    # return '''<form method = "POST" action="/process">
    #         <input type="text" name = "name">
    #         <input type="text" name = "location">
    #         <input type="submit">
    #         </form>'''
    return render_template('form.html')

@app.route('/process', methods=["POST"])
def process():
    print("I am here")
    name = request.form['name']
    location = request.form['location']
    return 'Hi {}. You are from {}'.format(name, location)

@app.route('/thesum', methods=["POST", "GET"])
def thesum():
    if request.method == "GET":
            n1 = randint(0, 11)
            n2 = randint(0, 11)
            rightanswer = n1+n2
            return '''            
            <form method = "POST" action="/thesum">
            <input type="hidden" name="n1" value={}></input>
            <input type="hidden" name="n2" value={}></input>
            <h1>{} + {}  is :<h1>
            <input type="text" name = "sumanswer">
            <input type="submit">            
            </form>'''.format(n1,n2,n1,n2)

    if request.method == "POST":
            sumanswer = request.form['sumanswer']
            n1=request.form['n1']
            n2=request.form['n2']
            rightanswer = int(n1) + int(n2)
            return '''
                    <h1>{} + {}  is :{}. </br>You typed {}<h1>
                    '''.format(n1,n2, rightanswer, sumanswer)


@app.route('/processjson')
def processjson():
    data = request.get_json()
    return jsonify([{"Key":"Value"}])



# use this if you want to start flask app using python3 app.py command
# this block is not required for just running using flask run command
if __name__ == '__main__':
    app.run(debug=True) # this will help with not restarting server everytime you make a change
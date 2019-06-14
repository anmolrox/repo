from flask import Flask,request,jsonify,json,render_template,session,redirect,url_for
import random
from flask_sqlalchemy import SQLAlchemy
from qw import Example
from qw import db
import requests
from random import randint
app=Flask(__name__)
app.secret_key = "12ddc"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:anmolrox@localhost/project'
db = SQLAlchemy(app)

    

a=0


@app.route('/')
def index():
  return render_template("home.html")
  
@app.route('/loginpage')
def index12():
  return render_template("login.html")
   
@app.route('/login',methods=['POST','GET'])
def bs():


    username=request.form['username']
    password=request.form['password']




    
   
    if Example.search(password,username):
      session['username']=username
      if Example.admin_check(password,username):
        return render_template('adminfile1.html',username=session['username'])

      else:
        return render_template('success.html',username=session['username'])

      
    else:
      return render_template('fail.html')

     	


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/urlparser',methods=['POST','GET'])
def os():
  return render_template('githubusername.html',username =session['username'])

@app.route('/details', methods=['POST'])
def details():
    global username,d

    username = request.form['username']
    d=[]
    r = requests.get('https://api.github.com/users/'+username+'')
    json_object = r.json()
    name = str(json_object['name'])
    email=str(json_object['email'])
    location=str(json_object['location'])
    company=str(json_object['company'])
    followers=str(json_object['followers'])
    following=str(json_object['following'])
    hireable=str(json_object['hireable'])
    return render_template('githubresult.html',name=name,email=email,location=location,company=company,followers=followers,following=following,hireable=hireable)

@app.route('/repos')
def repos():
    global username,d
    d=[]
    a = requests.get('https://api.github.com/users/'+username+'/repos')
    json=a.json()
    for i in json:
        d.append(str(i['name']))
    return str(d)
@app.route('/adduser', methods=['POST','GET'])
def kirti():
  return render_template('adduser1.html')

@app.route('/adding',methods=['POST','GET'])
def aditya():
  username=request.form['username']
  password=request.form['password']
  new_ex =Example(str(password),str(username),'N')
  db.session.add( new_ex)
  db.session.commit()
  return redirect(url_for('kirti'))  

@app.route('/edituser', methods=['POST','GET'])
def kirti1():
  return render_template('editpassword.html')


@app.route('/checkusers', methods=['POST','GET'])
def kirti2():
  examples=Example.query.all()
  a=[]
  for ex in examples:
      a.append([str(ex.username),str(ex.password)])
  print(a)    

  return render_template("checkusers.html",a=a)







@app.route('/changing',methods=['POST','GET'])
def aditya1():

  password=request.form['password']
  new_ex =Example(str(password),str(session['username']),'N')
  db.session.add( new_ex)
  db.session.commit()
  return redirect(url_for('kirti'))  

@app.teardown_appcontext
def shutdown_session(exception=None):
  db.session.remove()

@app.route('/details12',methods=['POST','GET'])
def details12():
    global username,d
    r = requests.get('https://www.instagram.com/pune.photographers/?__a=1&format=xml')
    json_object = r.json()
    name = str(json_object["graphql"]["user"]["edge_followed_by"]["count"])
    return name

 
 


if  __name__=='__main__':
   app.debug=True
   app.run()
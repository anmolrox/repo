from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:anmolrox@localhost/project'
db = SQLAlchemy(app)



class Example(db.Model):
	__tablename__ = 'loginpage'
	username  = db.Column('username', db.Unicode,primary_key=True)
	password = db.Column('password', db.Unicode)
	admin=db.Column('admin',db.Unicode)
   

	def __init__(self,p,u,a):
		self.username=u
		self.password=p
		self.admin=a


	
	def search(p,u):
		examples=Example.query.all()
		for ex in examples:
			if ex.username==u:
				if ex.password==p:

					return True
		return False	

	def admin_check(p,u):
		examples=Example.query.all()
		for ex in examples:
			if ex.username==u:
				if ex.password==p:
					if str(ex.admin)=='Y':
						return True
					else:
						return False

					
				else :
					return False
			else :
				return False	




		
        





		
           
        
                           


        
        



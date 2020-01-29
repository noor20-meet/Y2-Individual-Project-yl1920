from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		if query_user(request.form['username'], request.form['pass']) == True:
			login_session['logged_in']=request.form['username']
			# bio = request.form['bio']
			return render_template("homepage.html")
		else:
			return render_template('login.html', msg="username and password don't match")
	else:
		return render_template('login.html')
   

@app.route('/signup', methods=['POST','GET'])
def signup():
	if request.method == 'POST': 
		username = request.form['name']
		email = request.form['email']
		password = request.form['password']
		birthdate = request.form['birthday']
		gender = request.form['gender']
		bio = request.form['bio']
		try:
			add_user(username, email, password, birthdate, gender, bio)
			return render_template('login.html')
		except IntegrityError:
			# print(query_all())
			return render_template('signup.html', msg = "username already taken")
		except: 
			return render_template('signup.html', genmsg = "Please fill this field")
	else:
		return render_template('signup.html')

@app.route('/home')
def homepage():
	return render_template('homepage.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/profile', methods =["GET","POST"])
def profile():
	# if request.method == "POST":
		
	# else:  
		if 'logged_in' in login_session:
			username = login_session['logged_in']
			bio = query_one(username).bio
			return render_template('profile.html', username = username, bio = bio)
		else: 
			return render_template('profile.html')

@app.route('/snake')
def snake():
	return render_template('snake.html')

@app.route('/tictactoe')
def tic():
	return render_template('tic.html')

@app.route('/hangman')
def hangman():
	return render_template('hangman.html')

@app.route('/hit-the-dot')
def hit():
	return render_template('hit-the-dot.html')


if __name__ == '__main__':
    app.run(debug=True, threaded = False)
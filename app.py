from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/login')
def login():
	return render_template('login.html')
    # return render_template('home.html', students=query_all())

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
	{
		'author': 'youssef nasrallah',
		'title': 'Blog Post 1',
		'content': 'first Post Content',
		'date_posted': 'April, 20, 2023'
	},
	{
		'author': 'Iliass Fokhar',
		'title': 'Blog Post 2',
		'content': 'second Post Content',
		'date_posted': 'April, 19, 2023'
	},
	{
		'author': 'Abdo Elkhomsi',
		'title': 'Blog Post 3',
		'content': 'third Post Content',
		'date_posted': 'April, 18, 2023'
	}
]

@app.route("/")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))

	return render_template('register.html', title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')

	return render_template('login.html', title='login', form=form)
from flask import render_template, url_for, flash, redirect
from flaskblog import app, bcrypt, db
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
		# hashed user password
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)

		# add the new user to a database
		with app.app_context():
			db.session.add(user)
			db.session.commit()

		flash('Your account has been created! you are now able to login', 'success')
		return redirect(url_for('login'))

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
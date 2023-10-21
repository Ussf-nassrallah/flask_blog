from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '6dc4a7059cf17118fafe84a7815dc063'

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

if __name__ == '__main__':
	app.run(debug=True)
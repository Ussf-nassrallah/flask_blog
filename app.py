from flask import Flask, render_template
app = Flask(__name__)

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

# home page
@app.route("/")
def home():
	return render_template('home.html', posts=posts)

# about page
@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
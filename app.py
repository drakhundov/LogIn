from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None

	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please, try again.'
		else:
			pass # redirect to home page

	return render_template('login.html', error=error)


if __name__ == '__main__':
	app.run(debug=True)
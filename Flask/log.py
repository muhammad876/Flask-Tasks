from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)


# app.config['SECRET_KEY'] = 'c6a4a8a7799e0a47d7ad55340da1ca8f'
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/register")
def registration():

    return render_template('registration.html')

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('registration.html', title='Register', form=form)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


# if __name__ == '__main__':
#     app.run(debug=True)
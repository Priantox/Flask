from Models import User,Post 


@app.route('/')
def index():
    return render_template('home.html')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '486a440762160cd1032b6b88a8e90e8c'

data = [
    {
        'author': 'Ahamudul hasan',
        'title': 'Blog post 1'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 2'
    }
]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html', posts=data)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = login()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
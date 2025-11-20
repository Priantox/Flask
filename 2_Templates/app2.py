from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', posts=data)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="../static",    # static folder relative to this file
    template_folder="../templates"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'
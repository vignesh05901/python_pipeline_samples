from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['text']
        return render_template('echo.html', user_input=user_input)
    return render_template('index.html')

@app.route('/greet')
def greet():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
